import requests,json

token = ""


headers = {
  "Authorization": token,
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 OPR/81.0.4196.31"
}

request = requests.get("https://canary.discord.com/api/v8/users/@me/guilds", headers=headers).json()
for guild in request:
        print(f"{guild['id']}")