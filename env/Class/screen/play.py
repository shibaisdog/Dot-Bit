import pygame,time,threading
import Class.event.keyboard as keyboard
import Class.music_start
import Class.effect.text
import Class.effect.score
import data,_class_init
_RESIZE_LINE = 1.3
font_14 = data.font(14)
font_20 = data.font(20)
font_28 = data.font(28)
font_48 = data.font(48)
EFFECT_SCORE = Class.effect.score.New()
LAST_C = 0
def in_range(item):
    return data.UwU['range'] - 25 <= item["location"] <= data.UwU['range'] + 25
def success_render():
    _count = 0
    _count += data.score['perfect']
    _count += data.score['great']
    _count += data.score['good']
    _count += data.score['miss']
    _weight = 0.0
    _weight += data.score['perfect']
    _weight += data.score['great'] * 0.9
    _weight += data.score['good'] * 0.5
    if _count == 0:
        data.score['success'] = 0
    else:
        data.score['success'] = round(_weight / _count * 100,2)
def render():
    if not data.notes:
        return
    for v in data.notes:
        v['location'] += (v['speed']) / (data.config['fps'] / 60)
        if v['location'] >= data.screen.get_height():
            data.notes.remove(v)
            data.score['last'] = 'miss'
            data.score['miss'] += 1
            data.score['combo'] = 0
            data.score['last_c'] += 1
        else:
            if v['type'] == 'basic':
                #Notes = [
                #    (data.screen.get_width() / 2) - _RESIZE_LINE * 50,
                #    (data.screen.get_width() / 2) - _RESIZE_LINE ,
                #    (data.screen.get_width() / 2) + _RESIZE_LINE * 50,
                #    (data.screen.get_width() / 2) + _RESIZE_LINE * 100
                #]
                if v['index'] == 0:
                    pygame.draw.rect(data.screen,(255,255,255),(int((data.screen.get_width() / 2) - _RESIZE_LINE * 100),int(v['location'] - 4),int(_RESIZE_LINE * 50),8))
                elif v['index'] == 1:
                    pygame.draw.rect(data.screen,(255,255,255),(int((data.screen.get_width() / 2) - _RESIZE_LINE * 50),int(v['location'] - 4),int(_RESIZE_LINE * 50),8))
                elif v['index'] == 2:
                    pygame.draw.rect(data.screen,(255,255,255),(int((data.screen.get_width() / 2) - _RESIZE_LINE),int(v['location'] - 4),int(_RESIZE_LINE * 50),8))
                else:
                    pygame.draw.rect(data.screen,(255,255,255),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 50),int(v['location'] - 4),int(_RESIZE_LINE * 50),8))
                #pygame.draw.rect(data.screen,(255,255,255),(int(Notes[v['index']] - _RESIZE_LINE * 50) + 2,int(v['location'] - 4),int(_RESIZE_LINE * 50) - 2,8))
            else:
                if v['index'] == 0:
                    pygame.draw.rect(data.screen,(255,250,129),(int((data.screen.get_width() / 2) - _RESIZE_LINE * 100),int(v['location'] - 4),int(_RESIZE_LINE * 100),8))
                else:
                    pygame.draw.rect(data.screen,(255,250,129),(int((data.screen.get_width() / 2)),int(v['location'] - 4),int(_RESIZE_LINE * 100),8))
def cking_key(in_key,_index):
    if in_key == None:
        return
    else:
        for v in in_key:
            if int(v['index']) == _index and v['type'] == "basic":
                try:
                    data.notes.remove(v)
                except:
                    pass
                rg = data.screen.get_height() - 65 - v['location']
                if abs(rg + data.config['latency']) <= 9:
                    data.score['last'] = 'perfect'
                    data.score['combo'] += 1
                    data.score['perfect'] += 1
                    EFFECT_SCORE.add(2000)
                elif abs(rg + data.config['latency']) <= 15:
                    if rg + data.config['latency'] > 0:
                        data.score['last'] = 'fast great'
                    else:
                        data.score['last'] = 'slow great'
                    data.score['combo'] += 1
                    data.score['great'] += 1
                    EFFECT_SCORE.add(1000)
                else:
                    if rg + data.config['latency'] > 0:
                        data.score['last'] = 'fast good'
                    else:
                        data.score['last'] = 'slow good'
                    data.score['combo'] = 0
                    data.score['good'] += 1
                    EFFECT_SCORE.add(500)
                data.score['last_c'] += 1
                if data.score['max-combo'] < data.score['combo']:
                    data.score['max-combo'] = data.score['combo']
def cking_key_s(in_key):
    if in_key == None:
        return
    else:
        for v in in_key:
            if v['type'] == "long" and (v['index'] == 0 and keyboard.GET_KEY(data.UwU['press'][0]) and keyboard.GET_KEY(data.UwU['press'][1])) or (v['index'] == 1 and keyboard.GET_KEY(data.UwU['press'][2]) and keyboard.GET_KEY(data.UwU['press'][3])):
                try:
                    data.notes.remove(v)
                except:
                    pass
                rg = data.screen.get_height() - 65 - v['location']
                if abs(rg + data.config['latency']) <= 11:
                    data.score['last'] = 'perfect'
                    data.score['combo'] += 1
                    data.score['perfect'] += 1
                    EFFECT_SCORE.add(2000)
                elif abs(rg + data.config['latency']) <= 17:
                    if rg + data.config['latency'] > 0:
                        data.score['last'] = 'fast great'
                    else:
                        data.score['last'] = 'slow great'
                    data.score['combo'] += 1
                    data.score['great'] += 1
                    EFFECT_SCORE.add(1000)
                else:
                    if rg + data.config['latency'] > 0:
                        data.score['last'] = 'fast good'
                    else:
                        data.score['last'] = 'slow good'
                    data.score['combo'] = 0
                    data.score['good'] += 1
                    EFFECT_SCORE.add(500)
                data.score['last_c'] += 1
                if data.score['max-combo'] < data.score['combo']:
                    data.score['max-combo'] = data.score['combo']
def key_render():
    global _RESIZE_LINE
    in_key = list(filter(in_range,data.notes))
    #if keyboard.GET_KEY(pygame.K_UP):
    #    _RESIZE_LINE += 0.01
    #elif keyboard.GET_KEY(pygame.K_DOWN):
    #    _RESIZE_LINE -= 0.01
    if keyboard.GET_KEY(data.UwU['press'][0]):
        surface = pygame.Surface((_RESIZE_LINE * 50,data.screen.get_height()), pygame.SRCALPHA)
        surface.fill((255,255,255,65))
        data.screen.blit(surface, ((data.screen.get_width() / 2) - _RESIZE_LINE * 100, 0))
        #pygame.draw.rect(data.screen,(255,255,255),((data.screen.get_width() / 2) - _RESIZE_LINE * 100, 0,_RESIZE_LINE * 50,data.screen.get_height()))
        pygame.draw.line(data.screen,(250,88,88),(int((data.screen.get_width() / 2) - _RESIZE_LINE * 100),data.screen.get_height() - 65),(int((data.screen.get_width() / 2) - _RESIZE_LINE * 50),data.screen.get_height() - 65),int(_RESIZE_LINE * 2))
        threading.Thread(target=cking_key,args=(in_key,0)).start()
        text_0 = font_28.render("A",True,(250,88,88))
    else:
        text_0 = font_28.render("A",True,(255,255,255))
    if keyboard.GET_KEY(data.UwU['press'][1]):
        surface = pygame.Surface((_RESIZE_LINE * 50,data.screen.get_height()), pygame.SRCALPHA)
        surface.fill((255,255,255,65))
        data.screen.blit(surface, ((data.screen.get_width() / 2) - _RESIZE_LINE * 50, 0))
        pygame.draw.line(data.screen,(250,88,88),(int((data.screen.get_width() / 2) - _RESIZE_LINE * 50),data.screen.get_height() - 65),((data.screen.get_width() / 2),data.screen.get_height() - 65),int(_RESIZE_LINE * 2))
        threading.Thread(target=cking_key,args=(in_key,1)).start()
        text_1 = font_28.render("S",True,(250,88,88))
    else:
        text_1 = font_28.render("S",True,(255,255,255))
    if keyboard.GET_KEY(data.UwU['press'][2]):
        surface = pygame.Surface((_RESIZE_LINE * 50,data.screen.get_height()), pygame.SRCALPHA)
        surface.fill((255,255,255,65))
        data.screen.blit(surface, ((data.screen.get_width() / 2), 0))
        pygame.draw.line(data.screen,(250,88,88),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 50),data.screen.get_height() - 65),((data.screen.get_width() / 2),data.screen.get_height() - 65),int(_RESIZE_LINE * 2))
        threading.Thread(target=cking_key,args=(in_key,2)).start()
        text_2 = font_28.render("K",True,(250,88,88))
    else:
        text_2 = font_28.render("K",True,(255,255,255))
    if keyboard.GET_KEY(data.UwU['press'][3]):
        surface = pygame.Surface((_RESIZE_LINE * 50,data.screen.get_height()), pygame.SRCALPHA)
        surface.fill((255,255,255,65))
        data.screen.blit(surface, ((data.screen.get_width() / 2) + _RESIZE_LINE * 50, 0))
        pygame.draw.line(data.screen,(250,88,88),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 100),data.screen.get_height() - 65),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 50),data.screen.get_height() - 65),int(_RESIZE_LINE * 2))
        threading.Thread(target=cking_key,args=(in_key,3)).start()
        text_3 = font_28.render("L",True,(250,88,88))
    else:
        text_3 = font_28.render("L",True,(255,255,255))
    if keyboard.GET_KEY(data.UwU['press'][0]) or keyboard.GET_KEY(data.UwU['press'][1]) or keyboard.GET_KEY(data.UwU['press'][2]) or keyboard.GET_KEY(data.UwU['press'][3]):
        threading.Thread(target=cking_key_s,args=(in_key,)).start()
    text_rect_0 = text_0.get_rect()
    text_rect_0.center = (int((data.screen.get_width() / 2) - _RESIZE_LINE * 75),data.screen.get_height() - 45)
    data.screen.blit(text_0,text_rect_0)
    text_rect_1 = text_1.get_rect()
    text_rect_1.center = (int((data.screen.get_width() / 2) - _RESIZE_LINE * 25),data.screen.get_height() - 45)
    data.screen.blit(text_1,text_rect_1)
    text_rect_2 = text_2.get_rect()
    text_rect_2.center = (int((data.screen.get_width() / 2) + _RESIZE_LINE * 25),data.screen.get_height() - 45)
    data.screen.blit(text_2,text_rect_2)
    text_rect_3 = text_3.get_rect()
    text_rect_3.center = (int((data.screen.get_width() / 2) + _RESIZE_LINE * 75),data.screen.get_height() - 45)
    data.screen.blit(text_3,text_rect_3)
def display():
    blue_surface = pygame.Surface((_RESIZE_LINE * 100,data.screen.get_height() - 65), pygame.SRCALPHA)
    blue_surface.fill((129,159,247,195))
    red_surface = pygame.Surface((_RESIZE_LINE * 100,data.screen.get_height() - 65), pygame.SRCALPHA)
    red_surface.fill((247,129,129,195))
    data.screen.blit(blue_surface, ((data.screen.get_width() / 2) - _RESIZE_LINE * 100, 0))
    data.screen.blit(red_surface, ((data.screen.get_width() / 2), 0))
    ###############################################################################################
    pygame.draw.line(data.screen,(255,255,0),((data.screen.get_width() / 2),0),((data.screen.get_width() / 2),data.screen.get_height()),int(_RESIZE_LINE * 2))
    pygame.draw.line(data.screen,(0,64,255),(int((data.screen.get_width() / 2) - _RESIZE_LINE * 50),0),(int((data.screen.get_width() / 2) - _RESIZE_LINE * 50),data.screen.get_height()),int(_RESIZE_LINE * 2))
    pygame.draw.line(data.screen,(255,0,64),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 50),0),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 50),data.screen.get_height()),int(_RESIZE_LINE * 2))
    pygame.draw.line(data.screen,(255,255,255),(int((data.screen.get_width() / 2) - _RESIZE_LINE * 100),0),(int((data.screen.get_width() / 2) - _RESIZE_LINE * 100),data.screen.get_height()),int(_RESIZE_LINE * 2))
    pygame.draw.line(data.screen,(255,255,255),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 100),0),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 100),data.screen.get_height()),int(_RESIZE_LINE * 2))
    ####################################################################################################################################
    pygame.draw.line(data.screen,(120,120,120),((data.screen.get_width() / 2),data.screen.get_height() - 65),((data.screen.get_width() / 2),data.screen.get_height()),int(_RESIZE_LINE * 2))
    pygame.draw.line(data.screen,(120,120,120),(int((data.screen.get_width() / 2) - _RESIZE_LINE * 50),data.screen.get_height() - 65),(int((data.screen.get_width() / 2) - _RESIZE_LINE * 50),data.screen.get_height()),int(_RESIZE_LINE * 2))
    pygame.draw.line(data.screen,(120,120,120),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 50),data.screen.get_height() - 65),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 50),data.screen.get_height()),int(_RESIZE_LINE * 2))
    pygame.draw.line(data.screen,(255,255,255),(int((data.screen.get_width() / 2) - _RESIZE_LINE * 100),data.screen.get_height() - 65),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 100),data.screen.get_height() - 65),int(_RESIZE_LINE * 2))
def play_bar():
    do = (int(time.time()) - int(data.music['start'])) / int(data.music['playing']['info']['length']) * ((_class_init.BK.get_size()[0] + _class_init.BK.get_location()[0] - 10) - (_class_init.BK.get_location()[0] + 10)) + _class_init.BK.get_location()[0] + 10
    pygame.draw.line(data.screen,(120,120,120),(_class_init.BK.get_location()[0] + 10,_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 5),(_class_init.BK.get_size()[0] + _class_init.BK.get_location()[0] - 10,_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 5),7)
    pygame.draw.line(data.screen,(255,255,255),(_class_init.BK.get_location()[0] + 10,_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 5),(do,_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 5),7)
def FFT_bar():
    pygame.draw.line(data.screen,(255,255,128),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 100) + 30,data.screen.get_height() - 15),(data.screen.get_width() - 20,data.screen.get_height() - 15),12)
    do = data.FFT['reval'] / data.FFT['high'] * (data.screen.get_width() / 2 - (data.screen.get_width() - 20)) + (data.screen.get_width() - 20)
    if do <= (int((data.screen.get_width() / 2) + _RESIZE_LINE * 100) + 30):
        do = (int((data.screen.get_width() / 2) + _RESIZE_LINE * 100) + 30)
    pygame.draw.line(data.screen,(120,120,120),((int((data.screen.get_width() / 2) + _RESIZE_LINE * 100) + 30),data.screen.get_height() - 15),(do,data.screen.get_height() - 15),12)
def doing():
    global LAST_C
    if time.time() - int(data.music['start']) >= int(data.music['playing']['info']['length']):
        Class.music_start.stop()
        data.__SCREEN = 'end'
        return
    #background.draw(data.music_list[data.music_choice_s]['source']['background-image'],(data.screen.get_width() / 1.14,0),(-1,-1))
    #background.draw(data.music_list[data.music_choice_s]['source']['background-image'],(data.screen.get_width() - ((data.screen.get_width() / 2) + _RESIZE_LINE * 120),0),((data.screen.get_width() / 2) + _RESIZE_LINE * 120 - 10,40))
    #threading.Thread(target=background.draw,args=(data.music_list[data.music_choice_s]['source']['background-image'],(data.screen.get_width() - ((data.screen.get_width() / 2) + _RESIZE_LINE * 120),0),((data.screen.get_width() / 2) + _RESIZE_LINE * 120 - 10,40))).start()
    #threading.Thread(target=_class_init.BK.draw).start()
    surface = pygame.Surface((data.screen.get_width() - (data.screen.get_width() / 2) + _RESIZE_LINE * 100,_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 50), pygame.SRCALPHA)
    surface.fill((129,159,0,125))
    data.screen.blit(surface, ((data.screen.get_width() / 2) + _RESIZE_LINE * 100 + 1,0))
    display()
    render()
    #FFT_bar()
    key_render()
    _class_init.EFFECT_LAST.draw()
    EFFECT_SCORE.render()
    success_render()
    _class_init.BK.draw()
    play_bar()
    if data.score['combo'] >= 3:
        text = font_28.render("Combo! "+str(data.score['combo']), True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (data.screen.get_width() // 2, data.screen.get_height() // 2 - 65)
        data.screen.blit(text, text_rect)
    text = font_20.render("Accuracy : "+str(data.score['success'])+"%", True, (128,255,255))
    text_rect = text.get_rect()
    text_rect.center = ((data.screen.get_width() / 2) + _class_init.BK.get_size()[0],_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 70) #(((data.screen.get_width() / 2 - _RESIZE_LINE * 140) + 20) / 2,35)
    data.screen.blit(text, text_rect)
    #data.screen.blit(font_14.render("Play : "+str(data.music['playing']['name']), True, (255,255,255)),((data.screen.get_width() / 2) + _RESIZE_LINE * 120,_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 9))
    #data.screen.blit(font_14.render("L "+str(data.music['playing']['composer']), True, (255,255,255)),((data.screen.get_width() / 2) + _RESIZE_LINE * 120 + 35,_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1]+ 24))
    text = font_20.render(str(data.music['playing']['name']), True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.center = ((data.screen.get_width() / 2) + _class_init.BK.get_size()[0],_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 17)
    data.screen.blit(text,text_rect)
    text = font_20.render(str(data.music['playing']['composer']), True, (255,255,255))
    text_rect = text.get_rect()
    text_rect.center = ((data.screen.get_width() / 2) + _class_init.BK.get_size()[0],_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 34)
    data.screen.blit(text,text_rect)
    text = font_20.render("Max-Combo : "+str(data.score['max-combo']), True, (178,255,222))
    text_rect = text.get_rect()
    text_rect.center = ((data.screen.get_width() / 2) + _class_init.BK.get_size()[0],_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 90) #(((data.screen.get_width() / 2 - _RESIZE_LINE * 140) + 20) / 2,35)
    data.screen.blit(text, text_rect)
    text = font_20.render("Score : "+str(data.score['scores']), True, (208,255,182))
    text_rect = text.get_rect()
    text_rect.center = ((data.screen.get_width() / 2) + _class_init.BK.get_size()[0],_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 110) #(((data.screen.get_width() / 2 - _RESIZE_LINE * 140) + 20) / 2,35)
    data.screen.blit(text, text_rect)
    #data.screen.blit(font_28.render("Score   : "+str(data.score['scores']), True, (208,252,92)),(10,data.screen.get_height() - 165))
    text = font_20.render("Perfect : "+str(data.score['perfect']), True, (208,252,92))
    text_rect = text.get_rect()
    text_rect.center = ((data.screen.get_width() / 2) + _class_init.BK.get_size()[0],_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 130) #(((data.screen.get_width() / 2 - _RESIZE_LINE * 140) + 20) / 2,35)
    data.screen.blit(text, text_rect)
    text = font_20.render("Great : "+str(data.score['great']), True, (255,255,0))
    text_rect = text.get_rect()
    text_rect.center = ((data.screen.get_width() / 2) + _class_init.BK.get_size()[0],_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 150) #(((data.screen.get_width() / 2 - _RESIZE_LINE * 140) + 20) / 2,35)
    data.screen.blit(text, text_rect)
    text = font_20.render("Good : "+str(data.score['good']), True, (255,160,92))
    text_rect = text.get_rect()
    text_rect.center = ((data.screen.get_width() / 2) + _class_init.BK.get_size()[0],_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 170) #(((data.screen.get_width() / 2 - _RESIZE_LINE * 140) + 20) / 2,35)
    data.screen.blit(text, text_rect)
    text = font_20.render("Miss : "+str(data.score['miss']), True, (247,129,129))
    text_rect = text.get_rect()
    text_rect.center = ((data.screen.get_width() / 2) + _class_init.BK.get_size()[0],_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 190) #(((data.screen.get_width() / 2 - _RESIZE_LINE * 140) + 20) / 2,35)
    data.screen.blit(text, text_rect)
    pygame.draw.line(data.screen,(255,255,255),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 100),_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 50),(data.screen.get_width(),_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 50),int(_RESIZE_LINE * 2))
    #pygame.draw.line(data.screen,(255,255,255),(int((data.screen.get_width() / 2) + _RESIZE_LINE * 100),_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 190),(data.screen.get_width(),_class_init.BK.get_size()[1] + _class_init.BK.get_location()[1] + 190),int(_RESIZE_LINE * 2))
    #data.screen.blit(font_28.render("Perfect : "+str(data.score['perfect']), True, (208,252,92)),(10,data.screen.get_height() - 135))
    #data.screen.blit(font_28.render("Great   : "+str(data.score['great']), True, (255,255,0)),(10,data.screen.get_height() - 105))
    #data.screen.blit(font_28.render("Good    : "+str(data.score['good']), True, (255,160,92)),(10,data.screen.get_height() - 75))
    #data.screen.blit(font_28.render("Miss    : "+str(data.score['miss']), True, (255,0,64)),(10,data.screen.get_height() - 45))
    if data.score['last'] == 'perfect':
        if data.score['last_c'] != LAST_C:
            _class_init.EFFECT_LAST.add(data.screen.get_width() // 2, data.screen.get_height() // 2 - 100,'perfect',(208,252,92))
            LAST_C = data.score['last_c']
            data.score['last_cn'] = 'perfect'
        #text = font_48.render('perfect', True, (208,252,92))
    elif data.score['last'] == 'fast great' or data.score['last'] == 'slow great':
        if data.score['last_c'] != LAST_C:
            _class_init.EFFECT_LAST.add(data.screen.get_width() // 2, data.screen.get_height() // 2 - 100,data.score['last'],(255,255,0))
            LAST_C = data.score['last_c']
            data.score['last_cn'] = data.score['last']
        #text = font_48.render(data.score['last'], True, (255,255,0))
    elif data.score['last'] == 'fast good' or data.score['last'] == 'slow good':
        if data.score['last_c'] != LAST_C:
            _class_init.EFFECT_LAST.add(data.screen.get_width() // 2, data.screen.get_height() // 2 - 100,data.score['last'],(255,160,92))
            LAST_C = data.score['last_c']
            data.score['last_cn'] = data.score['last']
        #text = font_48.render(data.score['last'], True, (255,160,92))
    elif data.score['last']:
        if data.score['last_c'] != LAST_C:
            if data.score['last'] != data.score['last_cn']:
                _class_init.EFFECT_LAST.add(data.screen.get_width() // 2, data.screen.get_height() // 2 - 100,'miss',(255,0,64))
            LAST_C = data.score['last_c']
            data.score['last_cn'] = 'miss'
        #text = font_48.render('miss', True, (255,0,64))
    #else:
    #    return
    #text_rect = text.get_rect()
    #text_rect.center = (data.screen.get_width() // 2, data.screen.get_height() // 2 - 100)
    #data.screen.blit(text, text_rect)
    #data.screen.blit(font_20.render("HIGH : "+str(data.FFT['high']), True, (208,252,92)),((int((data.screen.get_width() / 2) + _RESIZE_LINE * 100) + 30),data.screen.get_height() - 100))
    #data.screen.blit(font_20.render("LOW  : "+str(data.FFT['low']), True, (208,252,92)),((int((data.screen.get_width() / 2) + _RESIZE_LINE * 100) + 30),data.screen.get_height() - 125))
    #data.screen.blit(font_20.render("TAS  : "+str(math.pow((data.FFT['low'] + data.FFT['high']) / 2,2)), True, (208,252,92)),((int((data.screen.get_width() / 2) + _RESIZE_LINE * 100) + 30),data.screen.get_height() - 75))
    #if data.FFT['value'] >= math.pow((data.FFT['low'] + data.FFT['high']) / 2,2):
    #    data.screen.blit(font_20.render("FFT  : "+str(data.FFT['value']), True, (255,0,64)),((int((data.screen.get_width() / 2) + _RESIZE_LINE * 100) + 30),data.screen.get_height() - 50))
    #else:
    #    data.screen.blit(font_20.render("FFT  : "+str(data.FFT['value']), True, (208,252,92)),((int((data.screen.get_width() / 2) + _RESIZE_LINE * 100) + 30),data.screen.get_height() - 50))