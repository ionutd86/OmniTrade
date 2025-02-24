import json
from binance.client import Client

# Calea completă către fișierul config.json
config_path = r"E:\OmniTrade_backup\TaskZen\src\config.json"

# Deschide fișierul de configurare
with open(config_path) as config_file:
    config = json.load(config_file)

# Afișează conținutul pentru verificare
print("Config loaded successfully:", config)

# Inițializează clientul Binance
client = Client(api_key=config['API_KEY'], api_secret=config['API_SECRET'], testnet=config['USE_TESTNET'])

# Verifică soldul contului
try:
    account_info = client.get_account()
    print("Account Info:", account_info)
except Exception as e:
    print("Error connecting to Binance:", str(e))
