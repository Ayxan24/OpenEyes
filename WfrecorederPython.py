import os
import subprocess
import time
from datetime import datetime

# === READ CONFIG ===
def read_config(config_file="CONFIG.cfg"):
    config = {}
    with open(config_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                try:
                    exec(line, {"os": os}, config)
                except:
                    pass
    return config

config = read_config()

# === SETTINGS ===
SAVE_DIR = config.get('SAVE_DIR', os.path.expanduser("~/CODES/openeyesvideos"))
FPS = config.get('FPS', 1)
DURATION = config.get('DURATION', 15)
CODEC = config.get('CODEC', 'libx264')
FILEFORMAT = config.get('FILEFORMAT', 'mp4')
VIDEO_RESOLUTION = config.get('VIDEO_RESOLUTION', (1280, 720))
GEOMETRY = f"{VIDEO_RESOLUTION[0]}x{VIDEO_RESOLUTION[1]}+0,0"

os.makedirs(SAVE_DIR, exist_ok=True)

def record_clip():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(SAVE_DIR, f"record_{timestamp}.{FILEFORMAT}")

    cmd = [
        "nice", "-n", "19",
        "wf-recorder",
        "-f", filename,
        "--framerate", str(FPS),
        "--codec", CODEC,
        "--geometry", GEOMETRY,
    ]

    print(f"[INFO] Recording new clip: {filename}")
    proc = subprocess.Popen(cmd)

    time.sleep(DURATION)  # record for configured duration

    # stop wf-recorder gracefully
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()

    print(f"[INFO] Saved clip: {filename}")

def main():
    print(f"Starting continuous {DURATION}s {FPS}fps screen capture (low CPU)...")
    while True:
        record_clip()
        print("next clip...")
        # if you want a pause between clips, add a small sleep
        # time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Recording stopped by user.")
