from Class.effect._font_size import get_size_font
import data
class New:
    def __init__(self):
        self.instances = []
    def reset(self):
        self.instances = []
    def add(self,x,y,text,rgb):
        self.instances = []
        self.instances.append({
            "text" : text,
            "count" : 0,
            "scale" : 20,
            "location" : (x,y),
            "rgb" : rgb
        })
    def draw(self):
        for v in self.instances:
            if v['count'] <= 10 * (data.config['fps'] / 60):
                v['scale'] += 2 / (data.config['fps'] / 60)
            v['count'] += 1
            index = get_size_font(int(v['scale'])).render(v['text'],True,v['rgb'])
            index_rect = index.get_rect()
            index_rect.center = v['location']
            data.screen.blit(index,index_rect)