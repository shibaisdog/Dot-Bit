import time,Class.note.note,encryption.mod,threading,data
class SMF:
    def __init__(self):
        self.file = None
        self.data = None
        self.doing = False
    def reset(self):
        self.file = None
        self.data = None
        self.doing = False
    def set(self,file):
        self.file = file
        self.data = encryption.mod.read(file)
        self.doing = True
    def _base_(self):
        i = 0
        for v in self.data['@base']:
            if self.doing == False:
                break
            if i == 0:
                time.sleep(((v['w']) - (data.screen.get_height() - 65) / ((v['s']) / (data.config['fps'] / 60)) * 10) / 1000)
                print(f"note (base line) <wait : {((v['w']) - (data.screen.get_height() - 65) / ((v['s']) / (data.config['fps'] / 60))) / 1000}ms | speed : {v['s']} | type : {v['t']} | len : {len(self.data['@base']) - 1} / {i}>")
            else:
                time.sleep(v['w'] / 1000)
                print(f"note (base line) <wait : {v['w']}ms | speed : {v['s']} | type : {v['t']} | len : {len(self.data['@base']) - 1} / {i}>")
            if v['t'] == "b":
                Class.note.note.add_dot(True,v['s'])
            elif v['t'] == "l":
                Class.note.note.add_long_dot(True,v['s'])
            i += 1
    def _doing_(self):
        i = 0
        for v in self.data['@note']:
            if self.doing == False:
                break
            time.sleep(v['w'] / 1000)
            print(f"note <wait : {v['w']}ms | speed : {v['s']} | type : {v['t']} | len : {len(self.data['@note']) - 1} / {i}>")
            if v['t'] == "b":
                Class.note.note.add_dot(True,v['s'])
            elif v['t'] == "l":
                Class.note.note.add_long_dot(True,v['s'])
            i += 1
    def run(self):
        threading.Thread(target=self._base_).start()
        threading.Thread(target=self._doing_).start()