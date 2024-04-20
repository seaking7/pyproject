import requests
import os

id = os.getenv("CLIENT_ID")
secret = os.getenv("CLIENT_SECRET")


def call_api(keyword, start=1, display=10):
    url = f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&start={start}&display={display}"
    res = requests.get(url, headers={"X-Naver-Client-Id": id,
                                     "X-Naver-Client-Secret": secret})
    print(res)
    r = res.json()
    return r



if __name__ == '__main__':
    # 1100
    r = call_api("교대역 병원", 10, 100)
    items_ = r['items']
    for item in items_:
        print(item)
