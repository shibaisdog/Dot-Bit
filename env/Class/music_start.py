import pygame,time,data,_class_init
import Class.audio as audio
import threading,Class.note.smf
SMF = Class.note.smf.SMF()
def reset():
    data.notes = []
    data.score = {
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
def start(req):
    reset()
    data.music['start'] = time.time()
    data.music['playing'] = req
    data.__SCREEN = 'play'
    if req['source']['smf'] == "None":
        audio.play(req['source']['mp3'])
    else:
        audio.non_play(req['source']['mp3'])
        SMF.set(req['source']['smf'])
        SMF.run()
        #SMF._doing_()
def stop():
    SMF.reset()
    data.music['start'] = 0
    data.music['playing'] = {}
    pygame.mixer.music.stop()
    data.__SCREEN = 'choice'
    audio.non_play(data.music_list[data.music_choice_s]['source']['mp3'],data.music_list[data.music_choice_s]['info']['seek'])
    _class_init.BK.set(data.music_list[data.music_choice_s]['source']['background-image'],((data.screen.get_width() / 2) - 160,0),(10,10))