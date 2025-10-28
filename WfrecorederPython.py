import os
import subprocess
import time
from datetime import datetime

# === SETTINGS ===
SAVE_DIR = os.path.expanduser("~/CODES/openeyesvideos")
FPS = 1
DURATION = 15
CODEC = "libx264"
GEOMETRY = "960x540+0,0"  # reduced resolution for lower CPU

os.makedirs(SAVE_DIR, exist_ok=True)

def record_clip():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(SAVE_DIR, f"record_{timestamp}.mp4")

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

    time.sleep(DURATION)  # record for 15 seconds

    # stop wf-recorder gracefully
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()

    print(f"[INFO] Saved clip: {filename}")

def main():
    print("Starting continuous 15s 1fps screen capture (low CPU)...")
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
