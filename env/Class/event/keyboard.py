import pygame,sys
import data
import Class.music_start
def GET_KEY(key):
    if not key in data.key_B:
        return False
    else:
        return data.key_B[key]
def run_play():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if data.__SCREEN == 'end':
                    data.__SCREEN = 'UwU'
                    Class.music_start.stop()
                elif data.__SCREEN == 'play':
                    data.__SCREEN = 'UwU'
                    Class.music_start.stop()
                else:
                    pygame.quit()
                    sys.exit()
            data.key_B[event.key] = True
        if event.type == pygame.KEYUP:
            data.key_B[event.key] = False