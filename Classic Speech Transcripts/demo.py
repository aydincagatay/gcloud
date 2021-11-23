# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 23:03:53 2021

@author: Cagi
"""

import os
from google.cloud import speech

os.environ ['GOOGLE_APPLICATION_CREDENTIALS'] = 'api-key.json'
speech_client = speech.SpeechClient()


#örnek 1 ses dosyasını transkript etme
#dosya boyutu: <10mbs, length < 1 min


#step 1 dosya yükleme
media_file_name_mp3 ='videoplayback.mp3'
#media_file_name_wav = 'videoplayback.wav'

with open(media_file_name_mp3 ,'rb') as f1:
    byte_data_mp3 = f1.read()
audio_mp3= speech.RecognitionAudio(content = byte_data_mp3)


#with open(media_file_name_wav ,'rb') as f2:
#    byte_data_wav = f2.read()
#audio_wav = speech.RecognitionAudio(content = byte_data_wav)

#step 2 configure

config_mp3 = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation = True,
    language_code = 'tr-TR'
    )

#config_wav = speech.RecognitionConfig(
#   sample_rate_hertz=44100,
#    enable_automatic_punctation = True,
#    language_code = 'tr-TR',
#    audio_channel_count = 2
#    )


##step3 ses dosyalarını transkript etme

response_standart_mp3 = speech_client.recognize(
    config=config_mp3,
    audio =audio_mp3
    )

#response_standart_wav = speech_client.recognize(
#    config=config_wav,
#    audio =audio_wav
#    )

print(response_standart_mp3)





media_uri ='gs://gcspeechmetadata/videoplayback.mp3'

long_audio = speech.RecognitionAudio(uri=media_uri)

speech.RecognitionConfig(
    sample_rate_hertz = 48000,
    enable_automatic_punctuation = True,
    language_code = 'tr-TR',
    use_enhanced = True,
    model ='video'
    )

operation = speech_client.long_running_recognize(
    config = config_mp3,
    audio  = long_audio)

response = operation.result(timeout = 90)
print(response)










 