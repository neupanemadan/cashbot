from flask import Flask, request
import requests

app = Flask(__name__)
API_KEY = '6V6HGEJIKYG0NW4H.'


@app.route('/', methods=['POST'])
def home():
    try:
        data = request.get_json()
        amount = data['queryResult']['parameters']['unit-currency']['amount']
        amount = int(amount)
        from_c = data['queryResult']['parameters']['unit-currency']['currency']
        to_c = data['queryResult']['parameters']['currency-name']
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(
            from_c, to_c, API_KEY)
        response = requests.get(url=url).json()
        rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
        rate = float(rate)
        result = rate * amount
        time = response['Realtime Currency Exchange Rate']['6. Last Refreshed']
        
        return f"{amount} {from_c} is equal to {result} {to_c} as per {time}"
    except Exception as e:
        return 'Sorry, Could not convert'


if __name__ == "__main__":
	app.run(debug=True)
