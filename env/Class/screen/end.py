import Class.event.keyboard as keyboard
import data
font_28 = data.font(28)
def render():
    text = font_28.render("Accuracy : "+str(data.score['success'])+"%", True, (128,255,255))
    text_rect_0 = text.get_rect()
    text_rect_0.center = (int(data.screen.get_width() / 2),int(data.screen.get_height() / 2) - 120)
    data.screen.blit(text,text_rect_0)

    text = font_28.render("Max-Combo : "+str(data.score['max-combo']), True, (178,255,222))
    text_rect_0 = text.get_rect()
    text_rect_0.center = (int(data.screen.get_width() / 2),int(data.screen.get_height() / 2) - 90)
    data.screen.blit(text,text_rect_0)

    text = font_28.render("Score : "+str(data.score['scores']), True, (208,255,182))
    text_rect_0 = text.get_rect()
    text_rect_0.center = (int(data.screen.get_width() / 2),int(data.screen.get_height() / 2) - 60)
    data.screen.blit(text,text_rect_0)

    text = font_28.render("Perfect : "+str(data.score['perfect']), True, (208,252,92))
    text_rect_0 = text.get_rect()
    text_rect_0.center = (int(data.screen.get_width() / 2),int(data.screen.get_height() / 2))
    data.screen.blit(text,text_rect_0)

    text = font_28.render("Great : "+str(data.score['great']), True, (255,255,0))
    text_rect_0 = text.get_rect()
    text_rect_0.center = (int(data.screen.get_width() / 2),int(data.screen.get_height() / 2) + 30)
    data.screen.blit(text,text_rect_0)

    text = font_28.render("Good : "+str(data.score['good']), True, (255,160,92))
    text_rect_0 = text.get_rect()
    text_rect_0.center = (int(data.screen.get_width() / 2),int(data.screen.get_height() / 2) + 60)
    data.screen.blit(text,text_rect_0)

    text = font_28.render("Miss : "+str(data.score['miss']), True, (247,129,129))
    text_rect_0 = text.get_rect()
    text_rect_0.center = (int(data.screen.get_width() / 2),int(data.screen.get_height() / 2) + 90)
    data.screen.blit(text,text_rect_0)
def doing():
    render()