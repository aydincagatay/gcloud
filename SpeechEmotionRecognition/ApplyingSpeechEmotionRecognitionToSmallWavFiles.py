import soundfile
import os, glob, pickle
import numpy as np
from scipy.io import wavfile
import pickle
import os
from google.cloud import speech
import scipy.io.wavfile
import math  
import numpy
from pydub import AudioSegment
from datetime import datetime, timedelta
import librosa


#Extract features (mfcc, chroma, mel) from a sound file
def extract_feature(file_name, mfcc, chroma, mel):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        if chroma:
            stft=np.abs(librosa.stft(X))
        result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result=np.hstack((result, mfccs))
        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result=np.hstack((result, chroma))
        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            result=np.hstack((result, mel))
    return result

filename = 'modelForPrediction1.sav'
loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
feature=extract_feature("trsample111.9.wav", mfcc=True, chroma=True, mel=True)
feature=feature.reshape(1,-1)
prediction=loaded_model.predict(feature)


import os
import glob
filename = 'modelForPrediction1.sav'
for file in glob.glob("C:/Users/Cagi/Desktop/testt/*.wav"):
    if os.path.getsize(file) > 1601:
        file_name=os.path.basename(file)
        #a = os.path.getsize(file)
        feature=extract_feature(file_name, mfcc=True, chroma=True, mel=True)
        feature=feature.reshape(1,-1)
        prediction=loaded_model.predict(feature)
        print(file_name+" - "+str(prediction))
 



