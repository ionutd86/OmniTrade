# OmniTrade

Advanced Trading Bot for Automated Crypto Trading

## Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create configuration**
   Copy `config.json.example` to `config.json` and fill in your Binance API credentials:
   ```json
   {
       "API_KEY": "your_api_key",
       "API_SECRET": "your_api_secret",
       "USE_TESTNET": true
   }
   ```
   Alternatively, set the `CONFIG_PATH` environment variable to point to a custom config file.

3. **Run the connection test**
   ```bash
   python test_connection.py
   ```

The script will load your configuration, initialize the Binance client and print basic account information.
