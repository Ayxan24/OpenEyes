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
    cmd = [
    "nice", "-n", "19",
    "gpu-screen-recorder",
    "-w", "screen",
    "-f", "1",
    "-q", "medium",
    "-bm", "auto",
    "-fm", "vfr",
    "-k", "h264",
    "-tune", "performance",
    "-encoder", "gpu",
    "-cursor", "yes",
#    "-ro", SAVE_DIR,
    "-o", "clip_%Y-%m-%d_%H-%M-%S.mkv",
    "-keyint","2.0",
    "-c", "mkv",
    "-a", "",
#    "-r", "15",
#    "-replay-storage", "disk",
#    "-restart-replay-on-save", "yes"
    ]
    print(f"[INFO] Recording GPU-based 15s clips to {SAVE_DIR}")
    proc = subprocess.Popen(cmd)

    try:
        proc.wait()
    except KeyboardInterrupt:
        proc.terminate()
        print("\n[INFO] Stopped.")


def main():
    print("Starting continuous 15s 1fps screen capture (low CPU)...")
#    while True:
    record_clip()
    print("next clip...")
        # if you want a pause between clips, add a small sleep
        # time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Recording stopped by user.")
