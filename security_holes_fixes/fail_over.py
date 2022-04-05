import requests
import time

if __name__ == '__main__':
    while True:
        url="http://localhost/rest/captcha/"
        resp = requests.get(url=url)
        print(f"GET {url} Response: {resp.status_code} {resp.json()}")
        time.sleep(1)