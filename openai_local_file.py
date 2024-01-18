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
        "Do product detailing with a cardiac surgeon.mp3": "/Users/adimyth/Downloads/1705512467720_62496_Do_product_detailing_with_a_cardiac_surgeon.mp3",
        "Explain integration capabilities to the IT SPOC.mp3": "/Users/adimyth/Downloads/1705512530981_72025_Explain_integration_capabilities_to_the_IT_SPOC.mp3",
        "Handle questions on claim settlement ratio.mp3": "/Users/adimyth/Downloads/1705512568972_4263_Handle_questions_on_claim_settlement_ratio.mp3",
        "Illustrate TCO of a commercial vehicle to an SME owner.mp3": "/Users/adimyth/Downloads/1705512605311_26623_Illustrate_TCO_of_a_commercial_vehicle_to_an_SME_owner_.mp3",
        "Pitch a credit card to a salaried employee.mp3": "/Users/adimyth/Downloads/1705512632966_23786_Pitch_a_credit_card_to_a_salaried_employee.mp3",
    }

    for audio_name, audio_file in audio_files.items():
        main(audio_name, audio_file)
