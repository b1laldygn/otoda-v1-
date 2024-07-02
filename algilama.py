import speech_recognition as sr

# SpeechRecognition objesi oluştur
recognizer = sr.Recognizer()

# Mikrofondan ses al
with sr.Microphone() as source:
    print("Konuşun...")
    audio = recognizer.listen(source)

    # Konuşmayı metne dönüştür
    try:
        text = recognizer.recognize_google(audio, language="tr-TR")  # Türkçe olarak tanıma yap
        print("Söylediğiniz: ", text)
    except sr.UnknownValueError:
        print("Anlaşılamadı")
    except sr.RequestError as e:
        print(f"Sistem hatası: {e}")
