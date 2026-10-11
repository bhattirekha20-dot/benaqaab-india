import http.server
import socketserver
import json
import os
import sys
import subprocess
import urllib.parse
import mimetypes
from datetime import datetime

PORT = 8765
WORKSPACE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DASHBOARD_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(DASHBOARD_ROOT, "static")
COMMAND_QUEUE_FILE = os.path.join(DASHBOARD_ROOT, "command_queue.json")
LOG_FILE = os.path.join(DASHBOARD_ROOT, "activity_log.json")

def load_json(filepath, default_val):
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return default_val
    return default_val

def save_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def log_activity(action, details):
    logs = load_json(LOG_FILE, [])
    logs.insert(0, {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,
        "details": details
    })
    # Keep last 100 entries
    save_json(LOG_FILE, logs[:100])

class StudioServerHandler(http.server.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Connection', 'close')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def send_json(self, data, code=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        self.wfile.flush()


    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        if path == "/" or path == "/index.html":
            self.serve_file(os.path.join(DASHBOARD_ROOT, "index.html"), "text/html; charset=utf-8")
        elif path == "/api/status":
            self.handle_api_status()
        elif path == "/api/commands":
            commands = load_json(COMMAND_QUEUE_FILE, [])
            self.send_json({"commands": commands})
        elif path == "/api/logs":
            logs = load_json(LOG_FILE, [])
            self.send_json({"logs": logs})
        elif path == "/api/projects":
            self.handle_api_projects()
        elif path == "/api/project_data":
            project_id = query.get("project", ["sh13_aeps_fingerprint_fraud"])[0]
            self.handle_api_project_data(project_id)
        elif path.startswith("/static/"):
            rel_path = path[len("/static/"):]
            file_path = os.path.join(STATIC_DIR, rel_path)
            self.serve_file(file_path)
        elif path.startswith("/workspace/"):
            rel_path = path[len("/workspace/"):]
            file_path = os.path.normpath(os.path.join(WORKSPACE_ROOT, rel_path))
            if file_path.startswith(WORKSPACE_ROOT) and os.path.isfile(file_path):
                self.serve_file(file_path)
            else:
                self.send_error(404, "File Not Found in Workspace")
        elif path.startswith("/projects/") or path.startswith("/brand/"):
            rel_path = path.lstrip("/")
            file_path = os.path.normpath(os.path.join(WORKSPACE_ROOT, rel_path))
            if file_path.startswith(WORKSPACE_ROOT) and os.path.isfile(file_path):
                self.serve_file(file_path)
            else:
                self.send_error(404, f"Project File Not Found: {rel_path}")
        else:
            # Check workspace root first, then dashboard root
            ws_file = os.path.normpath(os.path.join(WORKSPACE_ROOT, path.lstrip("/")))
            if ws_file.startswith(WORKSPACE_ROOT) and os.path.isfile(ws_file):
                self.serve_file(ws_file)
            else:
                file_path = os.path.join(DASHBOARD_ROOT, path.lstrip("/"))
                if os.path.exists(file_path) and os.path.isfile(file_path):
                    self.serve_file(file_path)
                else:
                    self.send_error(404, f"Not Found: {path}")

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get('Content-Length', 0))
        body_bytes = self.rfile.read(length) if length > 0 else b'{}'
        try:
            payload = json.loads(body_bytes.decode('utf-8'))
        except Exception:
            payload = {}

        if path == "/api/command":
            cmd_text = payload.get("command", "").strip()
            if not cmd_text:
                self.send_json({"error": "Empty command"}, 400)
                return
            
            entry = {
                "id": int(datetime.now().timestamp() * 1000),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "command": cmd_text,
                "status": "QUEUED_FOR_AGENT",
                "source": "WEB_UI_DIRECT"
            }
            commands = load_json(COMMAND_QUEUE_FILE, [])
            commands.insert(0, entry)
            save_json(COMMAND_QUEUE_FILE, commands)
            log_activity("USER_COMMAND_SUBMITTED", cmd_text)

            # Auto-responder / local action triggers
            feedback = f"Command received and queued for Antigravity AI: '{cmd_text}'"
            self.send_json({"success": True, "entry": entry, "message": feedback, "commands": commands})

        elif path == "/api/analyze_video":
            video_path = payload.get("video_path", "").strip()
            if not video_path:
                self.send_json({"error": "Missing video_path"}, 400)
                return
            
            # Resolve video path
            if not os.path.isabs(video_path):
                video_path = os.path.normpath(os.path.join(WORKSPACE_ROOT, video_path))
            
            if not os.path.exists(video_path):
                self.send_json({"error": f"Video not found at: {video_path}"}, 404)
                return
            
            result = self.extract_video_keyframes(video_path, max_frames=payload.get("max_frames", 16))
            log_activity("VIDEO_ANALYZED", f"Extracted {len(result.get('frames', []))} frames from {os.path.basename(video_path)}")
            self.send_json(result)
        else:
            self.send_error(404, "Unknown endpoint")

    def extract_video_keyframes(self, video_path, max_frames=16):
        out_dir = os.path.join(STATIC_DIR, "extracted_frames")
        os.makedirs(out_dir, exist_ok=True)
        # Clean older frames
        for f in os.listdir(out_dir):
            if f.endswith((".jpg", ".png")):
                try:
                    os.remove(os.path.join(out_dir, f))
                except Exception:
                    pass

        # Probe video
        probe_cmd = [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration:stream=width,height,r_frame_rate,codec_name",
            "-of", "json", video_path
        ]
        duration = 0.0
        width, height = 1920, 1080
        try:
            p = subprocess.run(probe_cmd, capture_output=True, text=True, check=True)
            probe_data = json.loads(p.stdout)
            duration = float(probe_data.get("format", {}).get("duration", 0))
            if "streams" in probe_data and len(probe_data["streams"]) > 0:
                width = probe_data["streams"][0].get("width", 1920)
                height = probe_data["streams"][0].get("height", 1080)
        except Exception as e:
            print(f"ffprobe error: {e}")

        # Compute interval
        interval = max(1.0, duration / max_frames) if duration > 0 else 2.0
        
        # Extract frames using ffmpeg with hardware acceleration if available
        ffmpeg_cmd = [
            "ffmpeg", "-y", "-i", video_path,
            "-vf", f"fps=1/{interval:.2f}",
            "-q:v", "2",
            os.path.join(out_dir, "frame_%03d.jpg")
        ]
        try:
            subprocess.run(ffmpeg_cmd, capture_output=True, check=True)
        except Exception as e:
            print(f"ffmpeg extraction error: {e}")

        frames = []
        for idx, filename in enumerate(sorted(os.listdir(out_dir))):
            if filename.startswith("frame_") and filename.endswith(".jpg"):
                ts = idx * interval
                mins = int(ts // 60)
                secs = ts % 60
                frames.append({
                    "filename": filename,
                    "url": f"/static/extracted_frames/{filename}",
                    "timestamp": round(ts, 2),
                    "timestamp_formatted": f"{mins:02d}:{secs:05.2f}"
                })

        return {
            "success": True,
            "video_name": os.path.basename(video_path),
            "video_path": video_path,
            "duration": round(duration, 2),
            "duration_formatted": f"{int(duration//60):02d}:{duration%60:05.2f}",
            "resolution": f"{width}x{height}",
            "frame_count": len(frames),
            "interval_seconds": round(interval, 2),
            "frames": frames
        }

    def handle_api_status(self):
        active_proj = "projects/sh13_aeps_fingerprint_fraud"
        status_data = {
            "channel": "Benaqaab India (बेनाक़ाब इंडिया)",
            "motto": "SACH · SABOOT · BEBAK",
            "active_project": {
                "id": "SH-13",
                "title": "AePS Aadhaar Fingerprint Fraud (Silicone Ungli Scam)",
                "format": "YouTube Short / Reel (9:16 Vertical, 1080x1920)",
                "target_duration": "48s–50s",
                "status": "IN_PRODUCTION",
                "current_step": "Step 2: Script & Visual Assets Choreography",
                "folder": active_proj
            },
            "hardware": {
                "cpu": "13th Gen Intel Core i7-1355U (10 Cores / 12 Threads)",
                "gpu": "Intel(R) Iris(R) Xe Graphics (QuickSync h264_qsv + MediaFoundation enabled)",
                "fps_target": "60 FPS Master Clock"
            },
            "channel_charter": "ALL-IN-ONE Global & National Media Powerhouse (World News, ISRO/Space, Infra, Economy, Tech, Climate, Exposés)",
            "pipeline_stages": [
                {"step": 0, "name": "Gate 0: Topic & Format Confirm", "status": "COMPLETED"},
                {"step": 1, "name": "Step 1: Fact Ledger & Research Dossier", "status": "COMPLETED"},
                {"step": 2, "name": "Step 2: Script & Master Audio (-14 LUFS)", "status": "IN_PROGRESS"},
                {"step": 3, "name": "Step 3: 30 Visual Cuts & comp.html", "status": "UP_NEXT"},
                {"step": 4, "name": "Step 4: Chromium QA (10 Snapshots)", "status": "PENDING"},
                {"step": 5, "name": "Step 5: User Approval Gate", "status": "PENDING"},
                {"step": 6, "name": "Step 6: Master Render & High-CTR Thumbs", "status": "PENDING"}
            ],
            "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.send_json(status_data)

    def handle_api_projects(self):
        projects_dir = os.path.join(WORKSPACE_ROOT, "projects")
        projs = []
        if os.path.exists(projects_dir):
            for d in os.listdir(projects_dir):
                full_d = os.path.join(projects_dir, d)
                if os.path.isdir(full_d):
                    has_comp = os.path.exists(os.path.join(full_d, "comp.html"))
                    has_script = os.path.exists(os.path.join(full_d, "SCRIPT.md"))
                    has_ledger = os.path.exists(os.path.join(full_d, "FACT_LEDGER.json"))
                    mp4s = [f for f in os.listdir(full_d) if f.endswith(".mp4")]
                    projs.append({
                        "name": d,
                        "path": f"projects/{d}",
                        "has_comp": has_comp,
                        "has_script": has_script,
                        "has_ledger": has_ledger,
                        "mp4_count": len(mp4s),
                        "mp4_files": mp4s
                    })
        self.send_json({"projects": projs})

    def handle_api_project_data(self, project_id):
        proj_dir = os.path.join(WORKSPACE_ROOT, "projects", project_id)
        if not os.path.exists(proj_dir):
            self.send_json({"error": "Project not found"}, 404)
            return

        data = {
            "project_id": project_id,
            "script": "",
            "fact_ledger": None,
            "research_dossier": "",
            "files": os.listdir(proj_dir)
        }

        script_p = os.path.join(proj_dir, "SCRIPT.md")
        if os.path.exists(script_p):
            with open(script_p, "r", encoding="utf-8") as f:
                data["script"] = f.read()

        dossier_p = os.path.join(proj_dir, "RESEARCH_DOSSIER.md")
        if os.path.exists(dossier_p):
            with open(dossier_p, "r", encoding="utf-8") as f:
                data["research_dossier"] = f.read()

        ledger_p = os.path.join(proj_dir, "FACT_LEDGER.json")
        if os.path.exists(ledger_p):
            try:
                with open(ledger_p, "r", encoding="utf-8") as f:
                    data["fact_ledger"] = json.load(f)
            except Exception:
                pass

        self.send_json(data)

    def serve_file(self, filepath, content_type=None):
        if not os.path.exists(filepath) or not os.path.isfile(filepath):
            self.send_error(404, "File Not Found")
            return

        if not content_type:
            mime, _ = mimetypes.guess_type(filepath)
            content_type = mime or "application/octet-stream"

        try:
            with open(filepath, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            self.wfile.flush()
        except Exception as e:

            self.send_error(500, f"Error reading file: {e}")

class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

def run():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    os.chdir(WORKSPACE_ROOT)
    server_address = ('', PORT)
    httpd = ThreadingHTTPServer(server_address, StudioServerHandler)
    print(f">> Benaqaab Studio Live Server running at http://localhost:{PORT}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

if __name__ == '__main__':
    run()
