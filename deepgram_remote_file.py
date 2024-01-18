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
        "Do product detailing with a cardiac surgeon.mp3": "https://cdn-lankesh002-dev.enparadigmtech.com/roleplay/user_response_audio/1705512467720_62496_Do_product_detailing_with_a_cardiac_surgeon.mp3",
        "Explain integration capabilities to the IT SPOC.mp3": "https://cdn-lankesh002-dev.enparadigmtech.com/roleplay/user_response_audio/1705512530981_72025_Explain_integration_capabilities_to_the_IT_SPOC.mp3",
        "Handle questions on claim settlement ratio.mp3": "https://cdn-lankesh002-dev.enparadigmtech.com/roleplay/user_response_audio/1705512568972_4263_Handle_questions_on_claim_settlement_ratio.mp3",
        "Illustrate TCO of a commercial vehicle to an SME owner.mp3": "https://cdn-lankesh002-dev.enparadigmtech.com/roleplay/user_response_audio/1705512605311_26623_Illustrate_TCO_of_a_commercial_vehicle_to_an_SME_owner_.mp3",
        "Pitch a credit card to a salaried employee.mp3": "https://cdn-lankesh002-dev.enparadigmtech.com/roleplay/user_response_audio/1705512632966_23786_Pitch_a_credit_card_to_a_salaried_employee.mp3",
    }

    for audio_name, audio_url in audio_urls.items():
        main(audio_name, audio_url, model="base")
