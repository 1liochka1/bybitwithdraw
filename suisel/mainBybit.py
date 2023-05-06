import random

import ccxt
from loguru import logger



bybit = ccxt.bybit({
        "apiKey": '',
        "secret": '',
        'rateLimit':200,
        'options':{
            'defaultType': 'spot',

        }})

def main():
        with open(f"wallets.txt", "r") as f:
            wallets = [row.strip() for row in f]

        for wallet in wallets:
            try:
                amount = random.randint(1,5)   #от скольки до скольки максимум бнб выводить
                withdraw = bybit.withdraw('bnb',amount,wallet, params={"network": 'BSC'})
                logger.info(f'{withdraw}')
            except Exception as e:
                logger.error(f'{e}')


if __name__ == "__main__":
    main()

