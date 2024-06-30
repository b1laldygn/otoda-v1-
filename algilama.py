import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Bir şeyler söyleyin...")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='tr-TR') 
        print("Söylediğiniz: " + text)
    except sr.UnknownValueError:
        print("Ne dediğinizi anlayamadım.")
    except sr.RequestError as e:
        print("Ses tanıma servisine ulaşılamıyor; {0}".format(e))
        