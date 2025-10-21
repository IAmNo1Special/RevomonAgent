import speech_recognition as sr

r = sr.Recognizer()


def listen(listen_for: list[str] = None) -> tuple[str, bytes] | None:
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")

        try:
            audio = r.listen(source)
        except sr.WaitTimeoutError:
            print("No speech detected")
            return None

    try:
        text: str = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(
                e
            )
        )
        return None

    if listen_for is None:
        return (text.lower(), audio.get_wav_data())
    else:
        for phrase in listen_for:
            if phrase.lower() in text.lower():
                return (text.lower(), audio.get_wav_data())
        return None


if __name__ == "__main__":
    while True:
        audio_query = listen(listen_for=["tasha"])
        if audio_query:
            query, audio_bytes = audio_query
            print(f"[User][QUERY] >>> [Tasha]: {query}")
