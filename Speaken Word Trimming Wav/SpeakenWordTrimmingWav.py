# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:27:18 2021

@author: Cagi
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 15:45:22 2021

@author: Cagi
"""
 
import os
from google.cloud import speech
import scipy.io.wavfile
import math  
import numpy
from pydub import AudioSegment
from datetime import datetime, timedelta
import librosa
os.environ ['GOOGLE_APPLICATION_CREDENTIALS'] = 'api-key.json'
speech_client = speech.SpeechClient()
 
media_file_name_mp3 ='trsample1.wav' 

with open(media_file_name_mp3 ,'rb') as f1:
    byte_data_mp3 = f1.read()
audio_wav = speech.RecognitionAudio(content = byte_data_mp3)


fs1, y1 = scipy.io.wavfile.read(media_file_name_mp3)

config_mp3 = speech.RecognitionConfig(
    sample_rate_hertz=8000,
    enable_automatic_punctuation = True,
    enable_word_time_offsets= True,
    language_code = 'tr-tr'
    )

response_standart_mp3 = speech_client.recognize(
    config=config_mp3,
    audio =audio_wav
    )

print(response_standart_mp3)
#result = response_standart_mp3.result(timeout=90)
 
print(response_standart_mp3)
l1 = numpy.array([0,0])
for result in response_standart_mp3.results:
    alternative = result.alternatives[0] 

    for word_info in alternative.words:
        word = word_info.word
        start_time = word_info.start_time.total_seconds()
        end_time = word_info.end_time.total_seconds()
        print(
            f"Word: {word}, start_time: {start_time}, end_time: {end_time}"
        )
        wp = r'trsample1.wav' 
        trim_wav(wp, wp.replace(".wav", str(word_info.start_time.total_seconds())+".wav"), start_time,end_time)
         

from scipy.io import wavfile
 
def trim_wav( originalWavPath, newWavPath , start, end ):
    '''
    :param originalWavPath: the path to the source wav file
    :param newWavPath: output wav file * can be same path as original
    :param start: time in seconds
    :param end: time in seconds
    :return:
    '''
    sampleRate, waveData = wavfile.read( originalWavPath )
    startSample = int( start * sampleRate )
    endSample = int( end * sampleRate )
    wavfile.write( newWavPath, sampleRate, waveData[startSample:endSample])















