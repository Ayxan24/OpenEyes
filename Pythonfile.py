import os
import subprocess

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
SCREEN_RESOLUTION = config.get('SCREEN_RESOLUTION', (1920, 1080))
DISPLAY = config.get('DISPLAY', '0.0')

os.makedirs(SAVE_DIR, exist_ok=True)

# Convert resolution tuple to string
screen_size = f"{SCREEN_RESOLUTION[0]}x{SCREEN_RESOLUTION[1]}"
output_file = os.path.join(SAVE_DIR, f"recording.{FILEFORMAT}")

cmd = [
    "ffmpeg",
    "-f", "x11grab",
    "-r", str(FPS),
    "-s", screen_size,
    "-i", f":{DISPLAY}",
    "-t", str(DURATION),
    "-an",              # no audio
    "-c:v", CODEC,
    "-preset", "ultrafast",
    "-pix_fmt", "yuv420p",
    output_file
]

print(f"[INFO] Recording {DURATION}s at {FPS} FPS to {output_file}...")
subprocess.run(cmd)
print("[INFO] Done:", output_file)
