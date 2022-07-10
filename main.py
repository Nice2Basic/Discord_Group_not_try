import requests,threading



guildsid = input("guildsid = ")
headers = {
    "accept": "*/*",
    "accept-language": "th,th-TH;q=0.9,en;q=0.8",
    "authorization": "",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "en-US",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InRoLVRIIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMC4wLjQ4OTYuMTI3IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDAuMC40ODk2LjEyNyIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoid3d3Lmdvb2dsZS5jb20iLCJzZWFyY2hfZW5naW5lIjoiZ29vZ2xlIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEyNjYxMSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
    "cookie": "__dcfduid=8b673610912411eca2fbcb34aa860177; __sdcfduid=8b673611912411eca2fbcb34aa860177799b0f1be0155bb46b36bb413593f5131f2cce7afccc94e0acc6ce45abf84928; _gcl_au=1.1.1111372619.1645234671; _ga=GA1.2.766095591.1645234671; _fbp=fb.1.1645234672384.160644962; __stripe_mid=5f637e6e-a986-49c6-9d64-09cd4af3716b16d8a7; __cfruid=5d01d817f38717a2756972b54f11a63f1e066c9e-1651505801; locale=en-US; _gid=GA1.2.1738241017.1651638815; OptanonConsent=isIABGlobal=false&datestamp=Wed+May+04+2022+11%3A33%3A35+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false; __cf_bm=CF3kWDKr_pjqwpxH_jruINdKpgwZFXxeBtw8Ozghd4E-1651661585-0-AXL6oD2t2wfHQqTCw/zNo5TTIWNXNQGll4W0QFBr1Cja13uMiPuhqYc6XJ4rKzn54LxWek3MDIwu19AppsHNQmJnK3D5qANoxf2BkHqHUHFGj/kp8jjJZOWJDuTrAlklcQ==",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }



def r():
    res = requests.post(f"https://discord.com/api/v9/guilds/{guildsid}/scheduled-events",headers=headers,json={"name":"SSSSS","description":"SSSSS","privacy_level":2,"scheduled_start_time":"2022-05-04T12:00:00.373Z","scheduled_end_time":"2022-05-04T14:00:00.373Z","entity_type":3,"channel_id":None,"entity_metadata":{"location":"Nicedayzzz"},"broadcast_to_directory_channels":"false"})
    print(res.text)




th = 100
for i in range(th):
    t = threading.Thread(target=r)
    t.start()    