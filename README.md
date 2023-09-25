# Coinbase Market Data Tool

The Coinbase Market Data Tool is a Python program that provides real-time market insights for cryptocurrency exchange markets on the Coinbase platform. This tool allows users to specify a product (e.g., Bitcoin for US dollars or Ethereum for Euros) and receive updated metrics about trades every five seconds.

## Features

The Coinbase Market Data Tool provides the following insights in its output:

1. Current Bid and Ask Information: It displays the current highest bid and lowest ask prices, along with the corresponding quantities.
2. Biggest Bid-Ask Difference: It reports the biggest observed difference between the highest bid and lowest ask since the program was started.
3. Average Mid-Price: The mid-price is calculated as the average price between the highest bid and lowest ask. The tool provides the average mid-price for the last 1, 5, and 15 minutes.
4. Forecasted Mid-Price: It forecasts the mid-price for the specified product in the next 60 seconds.

## Requirements

* Python 3.x
* Python libraries specified in requirements.txt

## Getting Started

1. Clone or download this repository to your local machine.
2. Install the required Python libraries if they are not already installed:

```bash
pip install -r requirements.txt
```

3. Run the program by executing the main Python script:

```bash
python3 main.py
```

4. Follow the on-screen prompts to provide the product ID (e.g., "BTC-USD") you want to monitor.
5. Enjoy real-time market insights and metrics for the specified product. You go back to the product ID selection option by clicking CTRL+C. If you want to close to program clicl CTRL+Z.

## Notes
The program uses Coinbase's API to fetch real-time market data. Ensure that you have a stable internet connection for accurate data retrieval. Note that API urls may change in future.


