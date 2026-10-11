import json, os, glob

folders = glob.glob('video_learning_database/*/')
total_frames = 0
insights = []

for folder in sorted(folders):
    json_path = os.path.join(folder, 'EVERY_FRAME_ANALYSIS.json')
    if not os.path.exists(json_path): continue
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    frames = data.get('frames', [])
    total_frames += len(frames)
    vid_name = os.path.basename(os.path.dirname(folder))
    if not vid_name: 
        vid_name = os.path.basename(folder.strip('/\\'))
    
    # Find the most drastic cut in the video (highest delta)
    max_delta_frame = max(frames, key=lambda x: x.get('metrics', {}).get('delta_from_prev', 0))
    
    static_frames = [f for f in frames if f.get('forensics', {}).get('event') == 'STATIC_OR_MICRO_DRIFT']
    static_frame = static_frames[len(static_frames)//2] if static_frames else frames[0]

    insights.append(f"--- VIDEO: {vid_name} ---")
    insights.append(f"Total Frames: {len(frames)}")
    insights.append(f"PEAK IMPACT FRAME (Frame {max_delta_frame['frame_no']}, {max_delta_frame['timestamp']})")
    insights.append(f"  Audio: {max_delta_frame.get('audio_lockstep', {}).get('spoken_context', '')}")
    insights.append(f"  Visual Delta: {max_delta_frame.get('metrics', {}).get('delta_from_prev')} (Massive Context Switch)")
    
    insights.append(f"PEAK RETENTION HOLD (Frame {static_frame['frame_no']}, {static_frame['timestamp']})")
    insights.append(f"  Audio: {static_frame.get('audio_lockstep', {}).get('spoken_context', '')}")
    insights.append(f"  Event: {static_frame.get('forensics', {}).get('event')}")
    insights.append("")

print(f"TOTAL FRAMES PROCESSED: {total_frames}")
print("\n".join(insights))
