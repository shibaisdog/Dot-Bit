import pygame,threading
import Class.note.FFT
from data import config
pygame.mixer.init()
def play(path,start_ = 0):
    path = f"./app_data/music/source/{path}"
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(int(config['volume']) / 100)
    pygame.mixer.music.play(start=start_)
    threading.Thread(target=Class.note.FFT.audio_stream_thread).start()
def non_play(path,start_ = 0):
    path = f"./app_data/music/source/{path}"
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(int(config['volume']) / 100)
    pygame.mixer.music.play(start=start_)
    Class.note.FFT._reset()