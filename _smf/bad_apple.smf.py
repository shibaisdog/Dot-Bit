import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import env.encryption.mod as mod
mod.write("YmFkX2FwcGxlISE=.smf",{
    "@base":[],
    "@note":[
        {"w" : 1300,"s":10,"t":"b"},
        {"w" : 400,"s":10,"t":"b"},
        {"w" : 500,"s":10,"t":"b"},
        {"w" : 400,"s":10,"t":"b"},
    ]
})