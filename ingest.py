"""Step 1: connect to Binance websocket and print live trades.

Run with:  python ingest.py
Stop with: Ctrl+C
"""

import asyncio
import json

import websockets

# Binance public websocket endpoint for BTC/USDT trades.
# No API key needed - this is public market data.
BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"


async def main():
    # TODO 1: open a websocket connection to BINANCE_WS_URL.
    async with websockets.connect(BINANCE_WS_URL) as ws:
    # TODO 2: inside the "async with" block, loop over incoming messages with "async for message in ws:"
    # TODO 3: inside the loop, parse the JSON string into a dict.
    # TODO 4: print the fields you care about: trade ID, price, quantity.
        async for message in ws:
            trade = json.loads(message)
            price = float(trade["p"])
            print(f"trade_id={trade['t']} price={price:.2f} quantity={trade['q']}")




if __name__ == "__main__":
    # asyncio.run() starts the async event loop and runs main()
    # until it finishes (or you press Ctrl+C).
    asyncio.run(main())
