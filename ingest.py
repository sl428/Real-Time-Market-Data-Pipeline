"""Step 1: connect to Binance websocket and print live trades.

Run with:  python ingest.py
Stop with: Ctrl+C
"""

import asyncio
import json

import websockets

import csv
from pathlib import Path

# Binance public websocket endpoint for BTC/USDT trades.
# No API key needed - this is public market data.
BINANCE_WS_URL = "wss://stream.binance.com:9443/ws/btcusdt@trade"
DATA_FILE = Path("data/trades.csv")

async def main():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    is_new_file = not DATA_FILE.exists()
    with open(DATA_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if is_new_file:
            writer.writerow(["trade_id", "price", "qty", "trade_time", "event_time", "is_buyer_maker"])
        async with websockets.connect(BINANCE_WS_URL) as ws:
            count = 0
            async for message in ws:
                trade = json.loads(message)
                writer.writerow([trade["t"], trade["p"], trade["q"], trade["T"], trade['E'], trade['m']]) 
                count += 1
                if count % 1000 == 0:
                    print(f"received {count} trades")





if __name__ == "__main__":
    # asyncio.run() starts the async event loop and runs main()
    # until it finishes (or you press Ctrl+C).
    asyncio.run(main())
