import webbrowser
import urllib.request
import subprocess
import time
import sys
import os

URL = "http://localhost:8765"
SERVER_SCRIPT = os.path.join(os.path.dirname(__file__), "studio_dashboard", "server.py")

def is_server_running():
    try:
        urllib.request.urlopen(f"{URL}/api/status", timeout=1.5)
        return True
    except Exception:
        return False

def main():
    if not is_server_running():
        print("Starting Benaqaab Studio Live Server in background...")
        subprocess.Popen([sys.executable, SERVER_SCRIPT], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == 'nt' else 0)
        # Wait up to 3 seconds for server to start
        for _ in range(6):
            time.sleep(0.5)
            if is_server_running():
                break

    print(f">> Opening Benaqaab Mission Control Dashboard at {URL} ...")
    webbrowser.open(URL)

if __name__ == "__main__":
    main()
