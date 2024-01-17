import os
import time

from deepgram import DeepgramClient, PrerecordedOptions
from dotenv import load_dotenv

load_dotenv()


AUDIO_URL = {
    "url": "https://cdn-lankesh002-dev.enparadigmtech.com/roleplay/user_response_audio/1705473842647_52721_Sample_30_sec_english.mp3"
}

overall_time = 0


def main():
    global overall_time

    deepgram = DeepgramClient(os.getenv("DEEPGRAM_API_KEY"))
    options = PrerecordedOptions(smart_format=True, model="nova-2", language="en-US")

    start_time = time.time()
    response = deepgram.listen.prerecorded.v("1").transcribe_url(AUDIO_URL, options)
    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    print(
        "Transcription: ",
        response["results"].channels[0].alternatives[0].transcript,
        end="\n\n",
    )
    print("Time elapsed: ", total_time, " seconds", end="\n\n")
    overall_time += total_time


if __name__ == "__main__":
    # run the main function 5 times to get an average time
    for i in range(5):
        main()
    print("Average time: ", round(overall_time / 5, 2), " seconds", end="\n\n")
