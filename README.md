# Cosmos balance tracker
Simple balance tracker with prometheus integration

### Getting starteg
Edit chains info in settings.py file:
```
WALLETS = [
    {
        "chain": "osmosis", #from chain-registry ID https://github.com/cosmos/chain-registry
        "wallet": "osmo1m7xlymnpxl2d4llu67v08e8xs67dj2fz0wqmqw", # your wallet
        "denom": "uosmo",
        "decimals": 6 # 10^6 by default
    },
]
```

Run without using Docker:
```
pip install -r requirements
python main.py
```

