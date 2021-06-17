from instabot import Bot
import os 
import glob
import json


cookie_del = glob.glob("config/*cookie.json")
os.remove(cookie_del[0])

with open('userDate.json') as json_file:
    userDate = json.load(json_file)

bot = Bot()

bot.login(username = userDate["username"],
          password = userDate["password"])

def upLoad(commitlog):
    cp = commitlog + "#instagram_github_contribution"
    bot.upload_photo("code.jpg", caption = cp)