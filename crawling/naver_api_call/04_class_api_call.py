import requests
import os

id = os.getenv("CLIENT_ID")
secret = os.getenv("CLIENT_SECRET")

class NaverSearchApi():

    api_url = "https://openapi.naver.com/v1/search/blog.json"

    def call_api(self, keyword, start=1, display=10):
        url = f"{self.api_url}?query={keyword}&start={start}&display={display}"
        res = requests.get(url, headers={"X-Naver-Client-Id": id,
                                         "X-Naver-Client-Secret": secret})
        print(res)
        r = res.json()
        return r

    def get_paging_call(self, keyword, quantity):
        if quantity > 1100:
            # quantity = 1100
            exit("Error 최대 요청할 수 있는 건수는 1100건 입니다.")

        repeat = quantity // 100 # 1000총 10번
        display = 100
        if quantity < 100:
            display = quantity
            repeat = 1

        result = []
        for i in range(repeat):
            start = i * 100 + 1
            # 101
            if start > 1000:
                start = 1000
            print(f"{i + 1}번 반복 합니다. start:{start}")
            r = self.call_api(keyword, start=start, display=display)
            for i, item in enumerate(r['items']):
                print(i, item)
            result += r['items']
        return result

    def blog(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/blog.json"
        return self.get_paging_call(keyword, quantity)

    def news(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/news.json"
        return self.get_paging_call(keyword, quantity)

    def webkr(self, keyword, quantity=100):
        self.api_url = "https://openapi.naver.com/v1/search/webkr.json"
        return self.get_paging_call(keyword, quantity)

if __name__ == '__main__':
    naver_search_api = NaverSearchApi()
    r = naver_search_api.webkr("신림역 족발집", 20)
    # print(r)
    print(len(r))

    naver_search_api.news("이스라엘 전쟁", 200)

    naver_search_api.blog("청라", 20)


