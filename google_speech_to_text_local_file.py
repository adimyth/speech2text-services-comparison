import time
from google.cloud import speech
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Path to the local audio file
AUDIO_FILE = "/Users/adimyth/Downloads/1705473842647_52721_Sample_30_sec_english.mp3"

overall_time = 0


def transcribe_audio(file_path):
    global overall_time
    """Transcribe the given audio file using Google Cloud Speech-to-Text"""
    client = speech.SpeechClient()

    # Loads the audio into memory
    with open(file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=8000,
        language_code="en-US",
        use_enhanced=True,
        model="default",
    )

    start_time = time.time()
    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)
    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    if not response.results:
        print("No results returned.")
        return

    overall_time += total_time

    print(
        ".".join(
            [result.alternatives[0].transcript for result in response.results],
        )
    )
    print("\n")
    print("Time elapsed: ", total_time, " seconds", end="\n\n")


def main():
    transcribe_audio(AUDIO_FILE)


if __name__ == "__main__":
    for i in range(5):
        main()
    print("Average time: ", round(overall_time / 5, 2), " seconds", end="\n\n")
