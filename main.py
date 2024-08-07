from google.cloud import texttospeech
import os

# Specify the path to your credentials file
api_keys = "path-to-credentials/GOOGLE_APPLICATION_CREDENTIALS.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = api_keys


def synthesize_text(text):
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Specify US English Studio voice
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Studio-O",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE  # Adjust gender as needed
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

if __name__ == "__main__":
    text = "This setup should allow you to synthesize speech in Afrikaans with a voice that has a South African accent. If you want to choose a specific voice name or further customize the voice options, you may need to look at the documentation or list the available voices via the API to find specific voice names supported for Afrikaans."  # "Hello world" in Afrikaans
    synthesize_text(text)