# CashBot App

CashBot is a Flask-based web application integrated with Google Dialogflow, designed to provide a conversational interface for currency conversion.

## Features

- **Conversational Interface:** CashBot utilizes Google Dialogflow to understand natural language inputs and provide meaningful responses to user queries.
- **Currency Conversion: ** Users can easily convert between different currencies by specifying the source amount and the desired target currency.
- **Real-Time Exchange Rates: ** CashBot fetches the latest exchange rates from a reliable API to ensure accurate currency conversions.
- **Multi-Currency Support:** CashBot supports a wide range of currencies, allowing users to convert between various global currencies.

## Installation

To run CashBot locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/neupanemadan/cashbot.git
   
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   
3. Set up Dialogflow:

- Create a new Dialogflow project in the Google Cloud Console.
- Enable the Dialogflow API and obtain the necessary credentials.
- Set the environment variable.

5. Run the application:

   ```bash
   flask run
   
5. Run the application:

   Access CashBot in your browser at **http://localhost:5000**
