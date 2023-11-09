import websockets
import asyncio
import http.server

#socketsbay.com 

from http.server import SimpleHTTPRequestHandler

httpd = http.server.HTTPServer(("", 8000), SimpleHTTPRequestHandler)

async def main():
    
    ws = await websockets.connect("wss://socketsbay.com/wss/v2/1/demo/")

    # Nachricht an den Server senden
    await ws.send("Hallo ich bin Amin")

    data = await ws.recv()

    print(data)

asyncio.run(main())
