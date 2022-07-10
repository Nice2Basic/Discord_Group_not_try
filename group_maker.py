import requests
import discum
import json
import time
import random
with open("config.json") as conf:
  config = json.load(conf)
  token = config["token"]
  image_path = config["icon path"]
  names = ["NICEDAYZ","NICEDAYZSPAM", "HONONICEDAYZ GOT FUCK"]

headers = {
  "Authorization": token,
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"
}

while True:
    try:     
        r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json={"recipients": []})
        json_resp = json.loads(r.content)
        group_id = json_resp['id']
        bot = discum.Client(token=token, log={"console": False, "file": False})
        bot.setDmGroupIcon(group_id, image_path)
        time.sleep(0.5)
        response = requests.patch(f'https://discord.com/api/v9/channels/{group_id}', headers=headers, json={'name': random.choice(names)})
        print(response.status_code)

        with open("group_id.txt", "a") as group_id:
          group_id.write(json_resp['id'] + '\n')

    except: print(json_resp['retry_after']), time.sleep(json_resp['retry_after'])
