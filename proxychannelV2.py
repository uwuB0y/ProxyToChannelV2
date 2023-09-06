import telebot
import requests
import time
import threading
import os

token = "ur token" #توكنك
chat_id = "@defproxy" #حط يوزر قناتك
filename = "proxy.txt" #لاتغيره
url_1 = "https://gimmeproxy.com/api/getProxy"
url_2 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"

bot = telebot.TeleBot(token)

def proxyGay():
    while True:
        try:
            rq = requests.get(url_1)
            protocol = rq.json()["protocol"]
            ipport = rq.json()["ipPort"]
            country = rq.json()["country"]
            messageProxy = f"*- New Proxy*\n*Ip-Port:* `{ipport}`.\n*Type:* {protocol}.\n*Country:* {country}.\n----- ------- ------- ----\n-=> [404](t.me/teamon404)"
            bot.send_message(chat_id, messageProxy, parse_mode="markdown", disable_web_page_preview=True)
            print("done send proxy")
        except Exception as e:
            print(f"an error when send proxy:\n{e}")
        time.sleep(60)

def send404():
    while True:
        cap = "New proxy File"
        if os.path.exists(filename):
            try:
                os.remove(filename)
                print("done remove the old file")
            except Exception as e:
                print(f"an error in remove old file:\n{e}")
        try:
            data = requests.get(url_2).content
            with open(filename, 'wb') as f:
                f.write(data)
            print("done download file")
        except Exception as e:
            print(f"an error in downloading file:\n{e}")
        try:
            with open('proxy.txt', 'rb') as txt:
                bot.send_document(chat_id, txt, caption=cap)
                print("done send proxy file")
        except Exception as e:
            print("an error when send the file:")
        os.system("clear")
        print("done send file")
        time.sleep(3600)

oneminute = threading.Thread(target=proxyGay)
onehour = threading.Thread(target=send404)
#مسموح تنشر وتغير الحقوق مادام تذكر مصدري
oneminute.start()
onehour.start()