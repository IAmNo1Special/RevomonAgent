import time

import pyaudio
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


def generate_voice(text: str):

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name="Kore",
                    )
                )
            ),
        ),
    )

    return response.candidates[0].content.parts[0].inline_data.data


def play_audio(audio_data):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RECEIVE_SAMPLE_RATE = 24000

    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RECEIVE_SAMPLE_RATE, output=True
    )

    try:
        # Write the audio data in chunks to avoid blocking
        chunk_size = 1024
        for i in range(0, len(audio_data), chunk_size):
            chunk = audio_data[i : i + chunk_size]
            stream.write(chunk)
    except Exception as e:
        print(f"Error during audio playback: {e}")
    finally:
        # Clean up
        time.sleep(1.0)
        stream.stop_stream()
        stream.close()
        p.terminate()


def speak(text: str):
    audio_data = generate_voice(text)
    play_audio(audio_data)


if __name__ == "__main__":
    speak("In a sad, deep voice, say: I'm sorry, but I can't help you with that.")
