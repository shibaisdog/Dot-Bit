import random,time
import data
def add_dot(_index = False,_speed = 10):
    if data.__SCREEN != 'play':
        return
    index = random.randint(0,3)
    if len(data.notes) >= 1:
        if data.notes[len(data.notes)-1]['index'] == index:
            if index == 0:
                index = 3
            elif index == 3:
                index = 0
            else:
                if random.randint(0,51) >= 50:
                    index += 1
                else:
                    index -= 1
        if _index == False:
            if data.notes[len(data.notes)-1]['type'] == "basic":
                if (time.time() - data.notes[len(data.notes)-1]['craft']) * 1000 <= 150:
                    return
            else:
                if (time.time() - data.notes[len(data.notes)-1]['craft']) * 1000 <= 250:
                    return
    ran = random.randint(0,1000)
    if ran >= 900:
        add_long_dot(_index)
    else:
        data.notes.append({"location":0,"index":index,"speed":_speed,"craft":time.time(),"type":"basic"})
def add_long_dot(_index = False,_speed = 10):
    if data.__SCREEN != 'play':
        return
    index = random.randint(0,1)
    if len(data.notes) >= 1:
        if data.notes[len(data.notes)-1]['type'] == "long":
            if data.notes[len(data.notes)-1]['index'] == 1:
                index = 0
            else:
                index = 1
    data.notes.append({"location":0,"index":index,"speed":_speed,"craft":time.time(),"type":"long"})