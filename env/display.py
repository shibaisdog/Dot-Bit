import pygame,threading
import Class.event.keyboard
import Class.audio as audio
from Class.screen import end
from Class.screen import play
from Class.screen import choice
import data,_class_init
pygame.init()
pygame.display.set_caption("Dot-Bit")
pygame.display.set_icon(pygame.image.load("./app_data/image/icon.png"))
audio.non_play(data.music_list[data.music_choice_s]['source']['mp3'],data.music_list[data.music_choice_s]['info']['seek'])
_class_init.BK.set(data.music_list[data.music_choice_s]['source']['background-image'],((data.screen.get_width() / 2) - 160,0),(10,10))
pygame.mouse.set_visible(False)
font_14 = data.font(14)
while data.running:
    #Class.event.keyboard.run_play()
    threading.Thread(target=Class.event.keyboard.run_play()).start()
    data.screen.fill((0,0,0))
    if data.__SCREEN == 'play':
        play.doing()
    elif data.__SCREEN == 'choice':
        choice.doing()
    elif data.__SCREEN == 'end':
        end.doing()
    if data.config['fps-view'] == True:
        text = font_14.render("fps : "+str(int(data.FPS.get_fps())), True, (255,255,255)) #208,252,92
        surface = pygame.Surface((text.get_width() + 4,20), pygame.SRCALPHA)
        surface.fill((60,179,113,175))
        data.screen.blit(surface, (data.screen.get_width() - 77,10))
        data.screen.blit(text,(data.screen.get_width() - 75,10))
    pygame.display.flip()
    data.FPS.tick(data.config['fps'])