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
media_file_name_mp3 ='testsample2.wav'
#media_file_name_wav = 'videoplayback.wav'

with open(media_file_name_mp3 ,'rb') as f1:
    byte_data_mp3 = f1.read()
audio_mp3= speech.RecognitionAudio(content = byte_data_mp3)


#with open(media_file_name_wav ,'rb') as f2:
#    byte_data_wav = f2.read()
#audio_wav = speech.RecognitionAudio(content = byte_data_wav)

#step 2 configure

config_mp3 = speech.RecognitionConfig(
    sample_rate_hertz=8000,
    enable_automatic_punctuation = True,
    enable_word_time_offsets= True,
    language_code = 'en-US'
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
    enable_word_time_offsets= True,
    language_code = 'tr-tr',
    use_enhanced = True
    )

operation = speech_client.long_running_recognize(
    config = config_mp3,
    audio  = long_audio)

print("Waiting for operation to complete...")
result = operation.result(timeout=90)

for result in response_standart_mp3.results:
    alternative = result.alternatives[0] 

    for word_info in alternative.words:
        word = word_info.word
        start_time = word_info.start_time
        end_time = word_info.end_time

        print(
            f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}"
        )









 