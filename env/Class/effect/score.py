import data
class New:
    def __init__(self):
        self.instances = []
    def add(self,score):
        self.instances.append({
            "i" : 0,
            "score" : score
        })
    def render(self):
        for v in self.instances:
            if v['i'] + int(v['score'] / 20) >= v['score']:
                self.instances.remove(v)
            data.score['scores'] += int(v['score'] / 20)
            v['i'] += int(v['score'] / 20)