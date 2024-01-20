import os
import time

from deepgram import DeepgramClient, PrerecordedOptions
from dotenv import load_dotenv

load_dotenv()


def main(audio_name, audio_url, model):
    print("=" * 60)
    print("Audio name: ", audio_name)
    print("Audio url: ", audio_url)
    overall_time = 0

    deepgram = DeepgramClient(os.getenv("DEEPGRAM_API_KEY"))
    options = PrerecordedOptions(smart_format=True, model=model, language="en-US")

    for _ in range(5):
        start_time = time.time()
        response = deepgram.listen.prerecorded.v("1").transcribe_url(
            {"url": audio_url}, options
        )
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        print(
            "Transcription: ",
            response["results"].channels[0].alternatives[0].transcript,
            end="\n\n",
        )
        print("Time elapsed: ", total_time, " seconds", end="\n\n")
        overall_time += total_time
    print("Average time: ", round(overall_time / 5, 2), " seconds", end="\n\n")
    print("=" * 60)


if __name__ == "__main__":
    audio_urls = {
        "1.mp3": "https://cdn-aditya-dev.enparadigmtech.com/mp3/1.mp3",
        "2.mp3": "https://cdn-aditya-dev.enparadigmtech.com/mp3/2.mp3",
        "3.mp3": "https://cdn-aditya-dev.enparadigmtech.com/mp3/3.mp3",
        "4.mp3": "https://cdn-aditya-dev.enparadigmtech.com/mp3/4.mp3",
        "5.mp3": "https://cdn-aditya-dev.enparadigmtech.com/mp3/5.mp3",
        "6.mp3": "https://cdn-aditya-dev.enparadigmtech.com/mp3/6.mp3",
        "7.mp3": "https://cdn-aditya-dev.enparadigmtech.com/mp3/7.mp3",
        "8.mp3": "https://cdn-aditya-dev.enparadigmtech.com/mp3/8.mp3",
        "9.mp3": "https://cdn-aditya-dev.enparadigmtech.com/mp3/9.mp3",
        "10.mp3": "https://cdn-aditya-dev.enparadigmtech.com/mp3/10.mp3",
    }

    for audio_name, audio_url in audio_urls.items():
        main(audio_name, audio_url, model="nova-2")
