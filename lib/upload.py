from instabot import Bot
import os 
import glob
import json


def upLoad(commitlog):
    if os.path.isfile("config/*cookie.json"):
        cookie_del = glob.glob("config/*cookie.json")
        os.remove(cookie_del[0])
        
    if os.path.isfile("data/userdate.json"):
        with open('data/userdate.json') as json_file:
            userDate = json.load(json_file)
    else:
        print("userdate.json 파일이 존재하지 않습니다.")
        print("파일생성후 다시 실행해주십시요")

    bot = Bot()

    bot.login(username = userDate["username"],
            password = userDate["password"])
    
    cp = commitlog + "#instagram_github_contribution"
    bot.upload_photo("data/code.jpg", caption = cp)