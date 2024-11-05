import base64,json
def write(path,data):
    path = f"./app_data/music/smf/{path}"
    with open(path,'w') as file:
        file.write(base64.b64encode(json.dumps(data).encode('utf-8')).decode('utf-8'))
def read(path):
    path = f"./app_data/music/smf/{path}"
    with open(path,"r",encoding='utf-8') as json_file:
        data = json.loads(base64.b64decode(json_file.read()).decode('utf-8'))
    return data
def u_write(path,data):
    path = f"./app_data/{path}"
    with open(path,'w') as file:
        file.write(base64.b64encode(json.dumps(data).encode('utf-8')).decode('utf-8'))
def u_read(path):
    path = f"./app_data/{path}"
    with open(path,"r",encoding='utf-8') as json_file:
        data = json.loads(base64.b64decode(json_file.read()).decode('utf-8'))
    return data