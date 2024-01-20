import time
import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()


client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def main(audio_name, audio_file):
    print("=" * 60)
    print("Audio name: ", audio_name)
    print("Audio file: ", audio_file)
    overall_time = 0

    audio_file = open(audio_file, "rb")

    for _ in range(5):
        start_time = time.time()
        transcript = client.audio.transcriptions.create(
            model="whisper-1", file=audio_file, response_format="text", language="en"
        )
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        print("Transcription: ", transcript, end="\n\n")
        print("Time elapsed: ", total_time, " seconds", end="\n\n")
        overall_time += total_time

    print("Average time: ", round(overall_time / 5, 2), " seconds", end="\n\n")
    print("=" * 60)


if __name__ == "__main__":
    audio_files = {
        "1.mp3": "/Users/adimyth/Downloads/mp3/1.mp3",
        "2.mp3": "/Users/adimyth/Downloads/mp3/2.mp3",
        "3.mp3": "/Users/adimyth/Downloads/mp3/3.mp3",
        "4.mp3": "/Users/adimyth/Downloads/mp3/4.mp3",
        "5.mp3": "/Users/adimyth/Downloads/mp3/5.mp3",
        "6.mp3": "/Users/adimyth/Downloads/mp3/6.mp3",
        "7.mp3": "/Users/adimyth/Downloads/mp3/7.mp3",
        "8.mp3": "/Users/adimyth/Downloads/mp3/8.mp3",
        "9.mp3": "/Users/adimyth/Downloads/mp3/9.mp3",
        "10.mp3": "/Users/adimyth/Downloads/mp3/10.mp3",
    }

    for audio_name, audio_file in audio_files.items():
        main(audio_name, audio_file)
