import requests
from bs4 import BeautifulSoup

def scraiping():

    print("実行")
    url = "https://www.yahoo.co.jp"

    response = requests.get(url)
    print(response)

    soup = BeautifulSoup(response.text, "html.parser")
    followers = soup.find_all("title")
    
    print(followers.count)

    if followers.count == 0:
        print("フォロワーが見つかっていない")
    else:
        for follower in followers:
            print(follower)

scraiping()



def scraipingZOZO():

    print("実行")
    url = "https://zozo.jp/category/jacket-outerwear/tailored-jacket/"

    response = requests.get(url)
    print(response)

    soup = BeautifulSoup(response.text, "html.parser")
    jackets = soup.find_all("div", class_="catalog-content")
    
    print(jackets.count)

    if jackets.count == 0:
        print("フォロワーが見つかっていない")
    else:
        for jacket in jackets:
            title = jacket.find("div", class_="catalog-h")
            price = jacket.find("div", class_="catalog-price-amount")

            print("商品の名前: "+str(title)+"  "+"価格: "+str(price))

scraipingZOZO()