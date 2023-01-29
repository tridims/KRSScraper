from bs4 import BeautifulSoup
from lxml import etree
import requests
import pandas as pd

cookie = {
    "PHPSESSID": "bo1rjkc5dkrlnv757fvcegg827",
}

headers = {
    "Origin": "https://siam.ub.ac.id",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://siam.ub.ac.id/addcourse.php",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
}

url = "https://siam.ub.ac.id/addcourse.php"
payload = {
    "type": "0",
    "day": "1",
    "kmk_find": "",
    "search": "CARI JADWAL",
    "step": "1",
}

response = requests.post(url, headers=headers, cookies=cookie, data=payload)
if response.status_code != 200:
    print("Error: ", response.status_code)
    exit()

soup = BeautifulSoup(response.content, "lxml")
tables = soup.find_all("table")
data = tables[1]

df = pd.read_html(str(data))

# save to csv
df[3].to_csv("jadwal.csv", index=False)
