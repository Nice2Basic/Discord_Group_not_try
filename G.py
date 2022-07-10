from httpx import Client
from concurrent.futures import ThreadPoolExecutor
from random import randint, choice
from time import sleep




userID = [
    "",
    ""
]

tokens = ""

postHeaders = {
    "content-type"          :   "application/json",
    "origin"                :   "https://discord.com",
    "referer"               :   "https://discord.com/channels/@me",
    "sec-ch-ua"             :   'Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile"      :   "?0",
    "sec-ch-ua-platform"    :   "Windows",
    "sec-fetch-dest"        :   "empty",
    "sec-fetch-mode"        :   "cors",
    "sec-fetch-site"        :   "same-origin",
    "user-agent"            :   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.1010 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    "x-debug-options"       :   "bugReporterEnabled",
    "x-super-properties"    :   "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJwdGIiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC4xMDEwIiwib3NfdmVyc2lvbiI6IjEwLjAuMTgzNjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA1MzA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "te"                    :   "trailers"
}

delsHeaders = {
    "origin"                :   "https://discord.com",
    "referer"               :   "https://discord.com/channels/@me",
    "sec-ch-ua-mobile"      :   "?0",
    "sec-ch-ua-platform"    :   "Windows",
    "sec-fetch-dest"        :   "empty",
    "sec-fetch-mode"        :   "cors",
    "sec-fetch-site"        :   "same-origin",
    "user-agent"            :   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.1010 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    "x-debug-options"       :   "bugReporterEnabled",
    "x-super-properties"    :   "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJwdGIiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC4xMDEwIiwib3NfdmVyc2lvbiI6IjEwLjAuMTgzNjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA1MzA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "te"                    :   "trailers"
}

threading = ThreadPoolExecutor(max_workers=int(1000000000))

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

class randoms:
    def strings(length, strings="abcdefghijklmnopqrstuvwxyz0123456789"):
        return ''.join(strings[randint(0, len(strings) - 1)] for _ in range(0, length))

    def process_payments(strings="abcde0123456789"):
        return ''.join(''.join(strings[randint(0, len(strings) - 1)] for _ in range(0, _)) + "-"for _ in [8, 4, 4, 4, 18])[:-1]

def setRequests(headers, usedTOKEN):
    __defduid    = f'__dcfduid={randoms.strings(32)}; '
    __sdcfduid   = f'__sdcfduid={randoms.strings(96)}; '
    __stripe_mid = f'__stripe_mid={randoms.process_payments()}; '
    __cfruid     = f'__cfruid={randoms.strings(40)}-{randoms.strings(10)}'

    headers["authorization"] = usedTOKEN
    headers["cookie"] = __defduid + __sdcfduid + __stripe_mid + __cfruid

def create_groups(tokens):
    while True:
        setRequests(postHeaders, tokens)
        with Client() as httpxCLIENT:
            requestsResponse = httpxCLIENT.post(
                "https://discord.com/api/v9/users/@me/channels",
                headers=postHeaders,
                json={"recipients": userID}
            ).json()
            
            try:
                httpxCLIENT.post(
                    f"https://discord.com/api/v9/channels/{requestsResponse['id']}/messages",
                    headers=postHeaders,
                    json={"content": genAmongUs()}
                )
                
                sleep(5)
                setRequests(delsHeaders, tokens)
                httpxCLIENT.delete(
                    f"https://discord.com/api/v9/channels/{requestsResponse['id']}",
                    headers=delsHeaders
                )
            except:
                print(''.join([requestsResponse['message'][:-1], ': ', str(requestsResponse['retry_after'])]))
                sleep(requestsResponse['retry_after']//10)

for _ in range(30):
    threading.submit(create_groups, tokens)