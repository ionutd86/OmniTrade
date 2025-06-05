# -*- coding: utf-8 -*-
"""Simple script to test Binance API connectivity."""

import json
import os
from binance.client import Client

# Determină calea către fișierul de configurare
# Dacă variabila de mediu ``CONFIG_PATH`` este setată, se va folosi acea valoare.
# În caz contrar, scriptul va căuta ``config.json`` în același director cu acest fișier.
config_path = os.environ.get(
    "CONFIG_PATH",
    os.path.join(os.path.dirname(__file__), "config.json"),
)

# Deschide fișierul de configurare
with open(config_path) as config_file:
    config = json.load(config_file)

# Afișează conținutul pentru verificare
print("Config loaded successfully:", config)

# Inițializează clientul Binance
client = Client(
    api_key=config["API_KEY"],
    api_secret=config["API_SECRET"],
    testnet=config.get("USE_TESTNET", False),
)

# Verifică soldul contului
try:
    account_info = client.get_account()
    print("Account Info:", account_info)
except Exception as e:
    print("Error connecting to Binance:", str(e))
