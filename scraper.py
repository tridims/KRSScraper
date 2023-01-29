from bs4 import BeautifulSoup
import requests
import pandas as pd
from config import Payload, Configuration


class KRSScraper:
    def __init__(self, configuration: Configuration, list_payload):
        self.cookies = configuration.cookies
        self.headers = configuration.headers
        self.url = configuration.url
        self.list_payload = list_payload

    def _send_request(self, payload: Payload):
        response = requests.post(
            self.url, headers=self.headers, cookies=self.cookies, data=payload.get_payload())
        assert response.status_code == 200, "Error fetching data from siam. Status Code: " + \
            str(response.status_code)
        return response

    def _parse_response_to_daftaframe(self, response):
        try:
            soup = BeautifulSoup(response.content, "lxml")
            tables = soup.find_all("table")
            data = tables[1]
            df = pd.read_html(str(data))
        except:
            print("Error parsing response, possible cause: invalid PHPSESSID")
            exit()
        return df[3]

    def scrape(self):
        list_df_result = []
        for payload in self.list_payload:
            response = self._send_request(payload)
            df = self._parse_response_to_daftaframe(response)
            list_df_result.append(df)

        self.result = pd.concat(list_df_result)
        return self.result

    def save(self, filename):
        assert self.result is not None, "Result is not set, run scrape first!"
        self.result.to_csv(filename, index=False)
