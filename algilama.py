import speech_recognition as sr

# Tanıma nesnesi oluşturma
recognizer = sr.Recognizer()

# Mikrofonu seçme
with sr.Microphone() as source:
  print("Konuşmaya başlayın...")
  
  # Ses kaydı alma
  audio = recognizer.listen(source)

# Konuşmayı tanıma
try:
  # Google Web Speech API kullanarak konuşmayı metne dönüştür
  text = recognizer.recognize_google(audio)
  print("Söylediğiniz:", text)
except sr.UnknownValueError:
  print("Konuşmanızı anlayamadım.")
except sr.RequestError as e:
  print("Servis hatası:", e)  