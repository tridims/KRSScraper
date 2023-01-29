import os
from dotenv import load_dotenv
load_dotenv()

COOKIES = {
    "PHPSESSID": os.getenv("PHPSESSID"),
}

HEADERS = {
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

URL = "https://siam.ub.ac.id/addcourse.php"


class Configuration:
    def __init__(self):
        self.headers = HEADERS
        self.url = URL
        self.cookies = COOKIES
        assert self.cookies["PHPSESSID"] is not None, "PHPSESSID is not set"


class Payload:
    def __init__(self, type, day, kmk_find, search, step):
        self.type = type
        self.day = day
        self.kmk_find = kmk_find
        self.search = search
        self.step = step

    def get_payload(self):
        return {
            "type": self.type,
            "day": self.day,
            "kmk_find": self.kmk_find,
            "search": self.search,
            "step": self.step,
        }


DEFAULT_PAYLOADS = [
    Payload("0", "1", "", "CARI JADWAL", "1"),
    Payload("0", "2", "", "CARI JADWAL", "1"),
    Payload("0", "3", "", "CARI JADWAL", "1"),
    Payload("0", "4", "", "CARI JADWAL", "1"),
    Payload("0", "5", "", "CARI JADWAL", "1"),
    Payload("0", "6", "", "CARI JADWAL", "1"),
    # Payload("0", "7", "", "CARI JADWAL", "1"),
]

DEFAULT_CONFIGURATION = Configuration()
