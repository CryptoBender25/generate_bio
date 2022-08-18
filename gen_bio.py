import requests
from fake_useragent import UserAgent
headers = {
    'authority': 'biogen.kacia.com',
    'accept': '*/*',
    'accept-language': 'ru,ru-RU;q=0.9,en;q=0.8',
    # 'content-length': '0',
    'origin': 'https://biogen.kacia.com',
    'referer': 'https://biogen.kacia.com/',
    'sec-ch-ua': '""',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': UserAgent().chrome,
    'x-requested-with': 'XMLHttpRequest',
}

count = int(input("Сколько био генерить(1 запрос - 2 био) "))
q = []
with open("bio.txt", "a") as f:
    for i in range(count):
        try:
            text =requests.post('https://biogen.kacia.com/bio.php', headers=headers).text
            if not text in q:
                q.append(text)
                f.write(text + "\n")
                print(f"Био {i+1}")
             
        except Exception as Err:
            print(Err)