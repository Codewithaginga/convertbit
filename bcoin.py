# bitcoin program

import time


class Bitcoin:

    ti = time.asctime()

    bitcoin1 = '$2086'

    print(f'As {ti} bitcoin is currently trading at {bitcoin1} usd')

    @staticmethod
    def enter_coin():

        bit = 2086

        enter_bitcoin_amount = float(input('\33[1mEnter amount of bitcoin amount: ' '\n'))

        usd = bit * enter_bitcoin_amount

        print(f'That is worth {usd:,} usd')


b = Bitcoin()
b.enter_coin()







