import data
font_20 = data.font(20)
font_50 = data.font(50)
def render():
    up = []
    this = None
    do = []
    for i,v in enumerate(data.music_list):
        if data.music_choice_s == i:
            this = v
        elif not this:
            up.append(v)
        else:
            do.append(v)
    text = font_50.render(this['name'],True,(0,64,255))
    text_rect = text.get_rect()
    text_rect.center = ((data.screen.get_width() / 2),(data.screen.get_height() / 2))
    data.screen.blit(text,text_rect)
    if len(up) >= 1:
        up.reverse()
        for i,v in enumerate(up):
            text = font_20.render(v['name'],True,(255,255,255))
            text_rect = text.get_rect()
            text_rect.center = ((data.screen.get_width() / 2),(data.screen.get_height() / 2) - (i * 20) - 50)
            data.screen.blit(text,text_rect)
    if len(do) >= 1:
        for i,v in enumerate(do):
            text = font_20.render(v['name'],True,(255,255,255))
            text_rect = text.get_rect()
            text_rect.center = ((data.screen.get_width() / 2),(data.screen.get_height() / 2) + (i * 20) + 50)
            data.screen.blit(text,text_rect)