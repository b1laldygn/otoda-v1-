import speech_recognition as sr

def speech_to_text():
    # Recognizer ve Microphone nesnelerini oluştur
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Mikrofonu kullanarak ses kaydı başlat
    with microphone as source:
        print("Lütfen konuşun...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Ses kaydını metne dönüştür
    try:
        text = recognizer.recognize_google(audio, language="tr-TR")
        print("Söyledikleriniz: " + text)
    except sr.UnknownValueError:
        print("Anlaşılamayan bir konuşma.")
    except sr.RequestError as e:
        print(f"Google Speech Recognition servisinden sonuç alınamadı; {e}")

if __name__ == "__main__":
    speech_to_text()
