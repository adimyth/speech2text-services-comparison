import boto3
import time
import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = "ap-south-1"
AUDIO_URL = "s3://ss-lankesh002-dev/roleplay/user_response_audio/1705473842647_52721_Sample_30_sec_english.mp3"

overall_time = 0


def transcribe_audio(audio_url):
    global overall_time

    """Transcribe the given audio file using AWS Transcribe"""
    transcribe_client = boto3.client(
        "transcribe",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION,
    )
    job_name = f"transcription-{int(time.time())}"

    start_time = time.time()

    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={"MediaFileUri": audio_url},
        MediaFormat="mp3",
        LanguageCode="en-US",
    )

    while True:
        status = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        if status["TranscriptionJob"]["TranscriptionJobStatus"] in [
            "COMPLETED",
            "FAILED",
        ]:
            break
        time.sleep(0.5)

    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    overall_time += total_time

    if status["TranscriptionJob"]["TranscriptionJobStatus"] == "COMPLETED":
        print(
            "Transcription: ",
            status["TranscriptionJob"]["Transcript"]["TranscriptFileUri"],
            end="\n\n",
        )
        print("Time elapsed: ", total_time, " seconds", end="\n\n")
    else:
        print("Transcription failed", end="\n\n")
        print("Time elapsed: ", total_time, " seconds", end="\n\n")


def main():
    transcribe_audio(AUDIO_URL)


if __name__ == "__main__":
    for _ in range(5):
        main()
    print("Average time: ", round(overall_time / 5, 2), " seconds", end="\n\n")
