import requests
import json


def ticker_tape_images():
    url = "https://api.tickertape.in/screener/query"

    payload = json.dumps({
    "match": {},
    "sortBy": "mrktCapf",
    "sortOrder": -1,
    "project": [
        "subindustry",
        "mrktCapf",
        "roce",
        "roe",
        "pftMrg"
    ],
    "offset": 0,
    "count": 10000,
    "sids": []
    })
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'accept-version': '8.14.0',
    'Content-Type': 'application/json'
    }
    failed_stocks = []
    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    stock_list = data['data']['results']
    
    for stock in stock_list:
        sid = (stock['sid'])
        symbol = stock['stock']['info']['ticker']

        image_url = f"https://assets.tickertape.in/stock-logos/{sid}.png"

        image_response = requests.get(image_url, stream=True)
        if image_response.status_code == 200:
            with open(f"images/png/tickertape/{symbol}.png", 'wb') as out_file:
                out_file.write(image_response.content)
            print(f"Image saved for {sid}")
        else:
            failed_stocks.append(symbol)
            with open("failed_stocks.txt", "a") as f:
                f.write(f"{symbol}\n")
            print(f"Failed to retrieve image for {symbol}")


# ticker_tape_images()


def dhan_images():
    with open("failed_stocks.txt", "r") as f:
        failed_stocks = f.readlines()
    failed_stocks = [x.strip() for x in failed_stocks]
    for stock in failed_stocks:
        dhan_image_url = f"https://images.dhan.co/symbol/{stock}.png"
        image_response = requests.get(dhan_image_url, stream=True)
        if image_response.status_code == 200:
            with open(f"images/equity/dhan/png/{stock}.png", 'wb') as out_file:
                out_file.write(image_response.content)
            print(f"Image saved for {stock}")
        else:
            print(f"Failed to retrieve image for {stock}")
            with open("dhan_failed_stocks.txt", "a") as f: 
                f.write(f"{stock}\n")
            print(f"Failed to retrieve image for {stock}")

dhan_images()