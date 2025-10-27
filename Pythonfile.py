import subprocess
from datetime import datetime

def record_screen(duration=15, fps=1):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"record_{timestamp}.mp4"

    cmd = [
        "ffmpeg",
        "-f", "xdg-desktop-portal",
        "-framerate", str(fps),
        "-t", str(duration),
        "-i", "default",          # 👈 THIS was missing before
        "-an",
        "-c:v", "libx264",
        "-preset", "ultrafast",
        filename
    ]

    subprocess.run(cmd)

if __name__ == "__main__":
    print("Recording via Wayland portal — screen picker may appear...")
    record_screen()
    print("Done! Check your folder for the video file.")
    print("cart")
