import subprocess

output_file = "recording.mp4"
duration = 15  # seconds
fps = 1        # frame per second

# Get your screen size (you can hardcode e.g. 1920x1080)
screen_size = "1920x1080"

cmd = [
    "ffmpeg",
    "-f", "x11grab",
    "-r", str(fps),
    "-s", screen_size,
    "-i", ":0.0",       # display, may differ (use echo $DISPLAY)
    "-t", str(duration),
    "-an",              # no audio
    "-c:v", "libx264",
    "-preset", "ultrafast",
    "-pix_fmt", "yuv420p",
    output_file
]

print("[INFO] Recording 15s at 1 FPS...")
subprocess.run(cmd)
print("[INFO] Done:", output_file)
