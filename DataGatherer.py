from binance import AsyncClient, BinanceSocketManager
import asyncio
import pandas as pd
import csv

API_KEY = "qb4uHStm5PhDvhSMzOfntlk4MZKFaxYjqYJTb3kIgIxqgbM4ez1aGHhnsj1sRXFk"
SECRET_KEY = "gE19URvgXIz39QfCWAgF0XHEv7RjQpeJG72dr4whEMMtOVdlNWCW0KKdAkGMzOEl"

SYMBOL = "BTCUSDT"

FILE_NAME = "BTC_DATA.csv"

async def main():

    

    client = await AsyncClient.create()#(API_KEY,SECRET_KEY)
    bm = BinanceSocketManager(client)
    # start any sockets here, i.e a trade socket
    ts = bm.trade_socket(SYMBOL)

#       file = open(FILE_NAME,"a")
    # then start receiving messages
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            t = float(res['p'])
            file = open(FILE_NAME,"a")
            file.write(str(t) + "\n")
            file.close()
            print(str(t))

    await client.close_connection()

def clearFile():
    with open(FILE_NAME, 'r+') as f:
        f.truncate()
if __name__ == "__main__":

    clearFile()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())