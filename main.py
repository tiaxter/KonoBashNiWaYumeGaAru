import os
import subprocess
import signal
import pathlib
from threading import Timer

executing_path = str(pathlib.Path(__file__).parent.absolute())
video_path = "konogiornogiovanna.mp4"
midi_path = "untitled.mid"
audio_process = "audio_process"
video_process = "video_process"


def main():
    signal.signal(signal.SIGINT, signal_handler)
    global audio_process
    global video_process
    video_process = subprocess.Popen("DISPLAY= mpv -vo caca --quiet " + executing_path + "/" + video_path,
                                     shell=True, preexec_fn=os.setsid)
    audio_process = subprocess.Popen(executing_path + "/" + "midi-beeper.py " + executing_path + "/" + midi_path,
                                     shell=True, preexec_fn=os.setsid)


def signal_handler():
    video_process.kill()
    audio_process.kill()


if __name__ == "__main__":
    main()
