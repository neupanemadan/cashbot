from flask import Flask, request, jsonify, render_template
import requests
from config import setting

app = Flask(__name__)
API_KEY = setting.API_KEY


@app.route('/api', methods=['POST'])
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
        
        response = {
            'fulfillmentText':"{} {} is equal to {} {} as per {} .".format(amount, from_c, result, to_c, time)
        }
        
        return jsonify(response)
        
    except Exception as e:
        response = {
            'fulfillmentText':"Sorry , Could not convert!!"
        }
        
        return jsonify(response)
    
@app.route("/")
def index():
    print(API_KEY)
    return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)
        