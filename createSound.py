from gtts import gTTS
import os
tts = gTTS(text='selam',lang='tr')
tts.save("selam.py")
tts1 = gTTS(text='tamam',lang='tr')
tts1.save("tamam.py")
tts2 = gTTS(text='başarısız oldu',lang='tr')
tts2.save("basarisiz.py")
