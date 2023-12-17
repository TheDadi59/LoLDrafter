import asyncio
from websockets import serve

from tensorflow.keras.models import load_model

rnn_model = load_model('models/rnn-model.keras')


def process_champions(champions):
    # TODO: implement the function to process data the query received from the C# app
    return 0


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
