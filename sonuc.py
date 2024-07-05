from gtts import gTTS
import os
import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Lütfen konuşun...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        text = recognizer.recognize_google(audio, language="tr-TR")
        print("Söyledikleriniz: " + text)
        if text == "bilgisayar":
            os.system("start yusuf_dovus.mp3")
        if text.lower() == "yusuf":
            os.system("start tetek.mp3")
        if text.lower() == "anne":
            os.system("start anne.mp3")
        if text.lower() == "baba":
            os.system("start baba.mp3")
    except sr.UnknownValueError:
        print("Anlaşılamayan bir konuşma.")
    except sr.RequestError as e:
        print(f"Google Speech Recognition servisinden sonuç alınamadı; {e}")

if __name__ == "__main__":
    speech_to_text()