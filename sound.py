from gtts import gTTS
import os

# Kullanıcıdan hangi sesi istediğini seçmesini isteyelim
giris = int(input("""Hangi sesi istersiniz?
          -1 = Merhaba
          -2 = Selam
          -3 = Tamam
          -4 = Başarısız oldu
          -5 = çıkış
          Cevabınız: """))

while True:# Seçilen sesi oluşturalım ve kaydedelim (sadece bir kere)
    if giris == 1:
        tts = gTTS(text='merhaba', lang='tr')
        tts.save("merhaba.mp3")
    elif giris == 2:
        tts = gTTS(text='selam', lang='tr')
        tts.save("selam.mp3")
    elif giris == 3:
        tts = gTTS(text='tamam', lang='tr')
        tts.save("tamam.mp3")
    elif giris == 4:
        tts = gTTS(text='başarısız oldu', lang='tr')
        tts.save("basarisiz.mp3")
    elif giris == 5:
        break
    else:
        print("Lütfen 1-4 arasında bir seçim yapınız")
        exit()

# Dosyayı oynatmak için ise burada os.system() kullanabiliriz
    os.system("start {}.mp3".format("merhaba" if giris == 1 else 
                                "selam" if giris == 2 else 
                                "tamam" if giris == 3 else 
                                "basarisiz"))
