import logging
import os
from time import sleep

import prometheus_client
import requests
from prometheus_client import start_http_server, Gauge

from settings import WALLETS
import json

BALANCE = balance = Gauge('balance', 'Available balance', ['node'])

def get_balance(node_addr,wallet,denom):
    r= requests.get(
            f'{node_addr}/cosmos/bank/v1beta1/balances/{wallet}')
    if r.status_code != 200:
        return None
    for b in r.json()['balances']:
        if b['denom']==denom:
            print(b)
            return float(b['amount'])
    return 0

if __name__ == '__main__':
    start_http_server(int(os.environ.get("PORT", 8099)), addr='0.0.0.0')
    logging.info("STARTED")

    while True:

        for w in WALLETS:
            r = requests.get(f"https://proxy.atomscan.com/directory/{w['chain']}/chain.json")
            rpcs = r.json()['apis']['rest']
            for r in rpcs:
                balance = get_balance(r['address'], w['wallet'], w['denom'])
                if balance is not None:
                    logging.info(f"chain: {w['chain']}, balance: {balance}")
                    BALANCE.labels(w['chain']).set(balance/10**w['decimals'])
                    break
        sleep(10)




