# MacPriceBar

**MacPriceBar** is a lightweight macOS toolbar utility that displays real-time cryptocurrency prices directly in your menu bar. With a focus on simplicity and efficiency, MacPriceBar allows you to keep track of your favorite cryptocurrencies without the need for additional apps or browser tabs.

## Features

- **Real-time price updates** for Bitcoin (BTC), Ethereum (ETH), and Binance Coin (BNB).
- **Minimalistic design** with prices displayed directly in the macOS menu bar.
- **Automatic refresh** every 15 seconds to keep prices up-to-date.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/MacPriceBar.git
cd MacPriceBar
```

### 2. Install Dependencies
Ensure you have rumps and requests installed:

```bash
pip install rumps requests
```

###  3. Run the App
```bash
python macpricebar.py
```

The cryptocurrency prices will now appear in your macOS toolbar.

## Usage
After running the app, you'll see the current prices for Bitcoin (₿), Ethereum (Ξ), and Binance Coin (BNB) in your macOS menu bar. The prices automatically refresh every 15 seconds.

## Code Overview
The project is centered around the CryptoTickerApp class:

Initialization: The app initializes with a default "Loading..." title and starts a timer to update the prices every 15 seconds.
Price Updates: The update_prices method fetches the latest prices from the Binance API and updates the menu bar title with the current prices.
API Requests: The get_prices method sends requests to the Binance API to retrieve the latest prices for BTC, ETH, and BNB, rounding them for display.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request with any enhancements, bug fixes, or suggestions.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
