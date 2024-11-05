import Class.event.keyboard as keyboard
import Class.screen.play
import Class.audio as audio
import Class.music_start
import Class.effect.choice
import pygame,data,time,_class_init
font_20 = data.font(20)
last = time.time()
def key_render():
    global last
    if keyboard.GET_KEY(pygame.K_UP):
        if time.time() - last <= 0.15:
            return
        if data.music_choice_s <= 0:
            data.music_choice_s = len(data.music_list) - 1
        else:
            data.music_choice_s -= 1
        last = time.time()
        #data.key_B[pygame.K_UP] = False
        pygame.mixer.music.stop()
        audio.non_play(data.music_list[data.music_choice_s]['source']['mp3'],data.music_list[data.music_choice_s]['info']['seek'])
        _class_init.BK.set(data.music_list[data.music_choice_s]['source']['background-image'],((data.screen.get_width() / 2) - 160,0),(10,10))
    elif keyboard.GET_KEY(pygame.K_DOWN):
        if time.time() - last <= 0.15:
            return
        if data.music_choice_s >= len(data.music_list) - 1:
            data.music_choice_s = 0
        else:
            data.music_choice_s += 1
        last = time.time()
        #data.key_B[pygame.K_DOWN] = False
        pygame.mixer.music.stop()
        audio.non_play(data.music_list[data.music_choice_s]['source']['mp3'],data.music_list[data.music_choice_s]['info']['seek'])
        _class_init.BK.set(data.music_list[data.music_choice_s]['source']['background-image'],((data.screen.get_width() / 2) - 160,0),(10,10))
    elif keyboard.GET_KEY(13):
        pygame.mixer.music.stop()
        Class.music_start.start(data.music_list[data.music_choice_s])
        data.key_B[13] = False
        _class_init.EFFECT_LAST.reset()
        _class_init.BK.set(data.music_list[data.music_choice_s]['source']['background-image'],(data.screen.get_width() - ((data.screen.get_width() / 2) + Class.screen.play._RESIZE_LINE * 120),0),((data.screen.get_width() / 2) + Class.screen.play._RESIZE_LINE * 120 - 10,10))
def render():
    #for i,v in enumerate(data.music_list):
    #    if data.music_choice_s == i:
    #        text = font_20.render(v['name'],True,(0,64,255))
    #    else:
    #        text = font_20.render(v['name'],True,(255,255,255))
    #    text_rect = text.get_rect()
    #    text_rect.center = ((data.screen.get_width() / 2),i*20 + 20)
    #    data.screen.blit(text,text_rect)
    Class.effect.choice.render()
    surface = pygame.Surface((_class_init.BK.get_size()[0] + _class_init.BK.get_location()[0] + 10,_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 50), pygame.SRCALPHA)
    surface.fill((129,159,247,195))
    data.screen.blit(surface, (0,0))
    _class_init.BK.draw()
    text = font_20.render(data.music_list[data.music_choice_s]['name'], True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.center = ((_class_init.BK.get_size()[0] + _class_init.BK.get_location()[0]) / 2,_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 10)
    data.screen.blit(text,text_rect)
    text = font_20.render(data.music_list[data.music_choice_s]['composer'], True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.center = ((_class_init.BK.get_size()[0] + _class_init.BK.get_location()[0]) / 2,_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 27)
    data.screen.blit(text,text_rect)
def doing():
    key_render()
    render()