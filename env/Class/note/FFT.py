import pygame
import numpy as np
import scipy.fftpack
import sounddevice as sd
import Class.note.note
import data,math,threading
font_14 = data.font(14)
class FFT:
    LOW = 999
    HIGH = 0
    samplerate = 44100
    buffer_size = 1024
    def reset():
        FFT.LOW = 999
        FFT.HIGH = 0
    @staticmethod
    def callback(indata, frames, time, status):
        mono_signal = np.mean(indata, axis=1)
        fft_result = scipy.fftpack.fft(mono_signal)
        magnitude = np.abs(fft_result)
        magnitude_half = magnitude[:len(magnitude)//2]
        average_magnitude = np.mean(magnitude_half)
        if FFT.LOW > average_magnitude:
            FFT.LOW = average_magnitude
        if FFT.HIGH < average_magnitude:
            FFT.HIGH = average_magnitude
        if average_magnitude * math.pow((FFT.LOW + FFT.HIGH) / 2,2) * 10 >= math.pow((FFT.LOW + FFT.HIGH) / 2,2):
            Class.note.note.add_dot()
        #data.FFT['low'] = FFT.LOW
        #data.FFT['high'] = FFT.HIGH
        #data.FFT['value'] = average_magnitude * math.pow((FFT.LOW + FFT.HIGH) / 2,2) * 10
        #data.FFT['reval'] = average_magnitude
audio = FFT
current_thread = None
def _reset():
    global current_thread
    if current_thread and current_thread.is_alive():
        current_thread.do_run = False
        current_thread.join()
    audio.reset()
def audio_stream_thread():
    global current_thread
    if current_thread and current_thread.is_alive():
        current_thread.do_run = False
        current_thread.join()
    audio.reset()
    new_thread = threading.Thread(target=run_audio_stream)
    new_thread.do_run = True
    new_thread.start()
    current_thread = new_thread
def run_audio_stream():
    t = threading.currentThread()
    with sd.InputStream(callback=audio.callback, channels=2, samplerate=FFT.samplerate, blocksize=FFT.buffer_size):
        try:
            while getattr(t, "do_run", True) and pygame.mixer.music.get_busy():
                pygame.time.wait(100)
        except KeyboardInterrupt:
            print("-----END-----")
#def audio_stream_thread():
#    audio.reset()
#    with sd.InputStream(callback=audio.callback, channels=2, samplerate=FFT.samplerate, blocksize=FFT.buffer_size):
#        try:
#            while pygame.mixer.music.get_busy():
#                pygame.time.wait(100)
#        except KeyboardInterrupt:
#            print("-----END-----")