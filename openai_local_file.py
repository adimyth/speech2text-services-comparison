import time
import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()


client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

AUDIO_FILE = "/Users/adimyth/Downloads/1705473842647_52721_Sample_30_sec_english.mp3"

overall_time = 0


def main():
    global overall_time

    audio_file = open(AUDIO_FILE, "rb")

    start_time = time.time()
    transcript = client.audio.transcriptions.create(
        model="whisper-1", file=audio_file, response_format="text", language="en"
    )
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    print("Transcription: ", transcript, end="\n\n")
    print("Time elapsed: ", total_time, " seconds", end="\n\n")
    overall_time += total_time


if __name__ == "__main__":
    # run the main function 5 times to get an average time
    for i in range(5):
        main()
    print("Average time: ", round(overall_time / 5, 2), " seconds", end="\n\n")
