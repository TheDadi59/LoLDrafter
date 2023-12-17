import asyncio
from websockets import serve

from tensorflow.keras.models import load_model
import numpy as np
import loldrafter

rnn_model = load_model('models/rnn-model.keras')


def process_champions(champions):
    # TODO: implement the function to process data the query received from the C# app
    roles = ["TOP", "JUNGLE", "MIDDLE", "BOTTOM", "UTILITY", "TOP", "JUNGLE", "MIDDLE", "BOTTOM", "UTILITY"]
    encoded_champions = loldrafter.encode_champions(champions)
    encoded_roles = loldrafter.encode_roles(roles)
    query = np.concatenate(encoded_champions, encoded_roles).reshape((1, 1, -1))
    return query


async def ws_handler(websocket, path):
    # Handle incoming messages
    while True:
        champions = await websocket.recv()
        print(f"Received champions: {champions}")

        x = process_champions(champions)
        prediction = rnn_model.predict(x).round()
        winner = "blue" if prediction else "red"
        # Send response: which team was predicted as the winner
        await websocket.send(winner)


async def main():
    port = 8123
    async with serve(ws_handler, port=port):
        print(f"Server started on port {port}")


asyncio.run(main())
