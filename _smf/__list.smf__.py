import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import env.encryption.mod as mod
mod.u_write("music/list.smf",[
    {
        "name" : "Bad apple!!",
        "composer" : "Zun",
        "source" : {
            "mp3" : "YmFkX2FwcGxlISE=.mp3",
            "smf" : "None",
            "background-image" : "YmFkX2FwcGxlISE=.jpg"
        },
        "info" : {
            "seek" : 28,
            "length" : 115
        }
    },
    {
        "name" : "Fun Blue!",
        "composer" : "Fujiwara Steel",
        "source" : {
            "mp3" : "a.mp3",
            "smf" : "None",
            "background-image" : "a_hq720.jpg"
        },
        "info" : {
            "seek" : 60,
            "length" : 166
        }
    },
    {
        "name" : "Konton Boogie",
        "composer" : "jon-YAKITORY",
        "source" : {
            "mp3" : "b.mp3",
            "smf" : "None",
            "background-image" : "b_hq720.jpg"
        },
        "info" : {
            "seek" : 51.4,
            "length" : 157
        }
    },
    {
        "name" : "Mesmerizer",
        "composer" : "32ki",
        "source" : {
            "mp3" : "c.mp3",
            "smf" : "None",
            "background-image" : "c_hq720.jpg"
        },
        "info" : {
            "seek" : 44.8,
            "length" : 158
        }
    },
    {
        "name" : "Alice in Freezer",
        "composer" : "Orangestar",
        "source" : {
            "mp3" : "d.mp3",
            "smf" : "None",
            "background-image" : "d_hq720.jpg"
        },
        "info" : {
            "seek" : 23,
            "length" : 350
        }
    }
])