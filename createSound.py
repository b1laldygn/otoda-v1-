from gtts import gTTS
import os
tts = gTTS(text='selam',lang='tr')
tts.save("selam.mp3")
tts1 = gTTS(text='tamam',lang='tr')
tts1.save("tamam.mp3")
tts2 = gTTS(text='başarısız oldu',lang='tr')
tts2.save("basarisiz.mp3")
tts3= gTTS(text='yusufu dövücem',lang='tr')
tts3.save("yusuf_dovus.mp3")
tts4= gTTS(text='tetek',lang='tr')
tts4.save("tetek.mp3")
anne = gTTS(text='nasılsın',lang='tr')
anne.save("anne.mp3")