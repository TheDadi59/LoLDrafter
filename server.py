import asyncio
from websockets import serve

from tensorflow.keras.models import load_model
import numpy as np


# Encode the input champion ids as one-hot for every champion
def encode_champion(champion_id):
  correspondances = [
    266, 103, 84, 166, 12, 32, 34, 1, 523, 22,
    136, 268, 432, 200, 53, 63, 201, 233, 51, 164,
    69, 31, 42, 122, 131, 119, 36, 245, 60, 28, 81,
    9, 114, 105, 3, 41, 86, 150, 79, 104, 887, 120,
    74, 910, 420, 39, 427, 40, 59, 24, 126, 202, 222,
    145, 429, 43, 30, 38, 55, 10, 141, 85, 121, 203,
    240, 96, 897, 7, 64, 89, 876, 127, 236, 117, 99,
    54, 90, 57, 11, 902, 21, 62, 82, 25, 950, 267,
    75, 111, 518, 76, 895, 56, 20, 2, 61, 516, 80,
    78, 555, 246, 133, 497, 33, 421, 526, 888, 58, 107,
    92, 68, 13, 360, 113, 235, 147, 875, 35, 98, 102,
    27, 14, 15, 72, 37, 16, 50, 517, 134, 223, 163,
    91, 44, 17, 412, 18, 48, 23, 4, 29, 77, 6, 110,
    67, 45, 161, 711, 254, 234, 112, 8, 106, 19, 498,
    101, 5, 157, 777, 83, 350, 154, 238, 221, 115, 26,
    142, 143
  ]
  encoding = np.zeros(nb_champions)
  index = correspondances.index(champion_id)
  encoding[index] = 1
  return encoding


def encode_champions(champions_ids):
  """
  Encodes the given list of champions ids into an input vector of size nb_champions * 10 (number of players in each LoL game)
  """
  encoding = np.array([])
  for id in champions_ids:
      encoding = np.concatenate((encoding, encode_champion(id)))
  return encoding


def encode_role(role):
    roles = {
        "TOP": 0,
        "JUNGLE": 1,
        "MIDDLE": 2,
        "BOTTOM": 3,
        "UTILITY": 4
    }
    role = role.strip()
    encoding = np.zeros(len(roles))
    encoding[roles[role]] = 1
    return encoding


def encode_roles(roles):
    encoding = np.array([])
    for role in roles:
        encoding = np.concatenate((encoding, encode_role(role)))
    return encoding


rnn_model = load_model('models/rnn-model.keras')


def process_champions(champions):
    # TODO: implement the function to process data the query received from the C# app
    roles = ["TOP", "JUNGLE", "MIDDLE", "BOTTOM", "UTILITY", "TOP", "JUNGLE", "MIDDLE", "BOTTOM", "UTILITY"]
    encoded_champions = encode_champions(champions)
    encoded_roles = encode_roles(roles)
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
