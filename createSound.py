from gtts import gTTS
import os
tts = gTTS(text='selam',lang='tr')
tts.save("selam.mp3")
tts1 = gTTS(text='tamam',lang='tr')
tts1.save("tamam.mp3")
tts2 = gTTS(text='başarısız oldu',lang='tr')
tts2.save("basarisiz.mp3")
