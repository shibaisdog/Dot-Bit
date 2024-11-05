import pygame,ctypes
from Class import json
from encryption import mod
config = json.read('config.json')
u32 = ctypes.windll.user32
resolution = u32.GetSystemMetrics(0), u32.GetSystemMetrics(1)
if config['screen_size']['FULL_SCREEN']:
    #screen = pygame.display.set_mode(resolution,pygame.FULLSCREEN)
    screen = pygame.display.set_mode((config['screen_size']['w'],config['screen_size']['h']),pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((config['screen_size']['w'],config['screen_size']['h']))
UwU = {
    "press" : [
        pygame.K_a,
        pygame.K_s,
        pygame.K_k,
        pygame.K_l
    ],
    "range" : screen.get_height() - 65
}
score = {
    "scores" : 0,
    "success": 0.0,
    "last_cn" : "",
    "last_c" : 0,
    "last" : None,
    "max-combo" : 0,
    "combo" : 0,
    "perfect" : 0,
    "great" : 0,
    "good" : 0,
    "miss" : 0
}
music = {
    "start" : 0,
    "playing" : {}
}
music_list = mod.u_read('music/list.smf') #json.read('music/list.json')
music_choice_s = 0
FPS = pygame.time.Clock()
notes = []
key_B = {}
running = True
FFT = {
    "low" : -1,
    "high" : -1,
    "value" : 0,
    "reval" : 0
}
__SCREEN = 'choice'
pygame.font.init()
def font(size):
    return pygame.font.Font("./app_data/DungGeunMo.ttf",size)