# import base64
# from openai import OpenAI


goo_api=""


# import anthropic
# import base64
# import httpx

# Function to encode the image
# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
image_path = "Sudoku.png"

# Getting the Base64 string
# base64_image = encode_image(image_path)

from google import genai
from google.genai import types

# import requests
import PIL.Image

# image_path = "https://goo.gle/instrument-img"
# image = requests.get(image_path)
image = PIL.Image.open('Sudoku.png')

client = genai.Client(api_key=goo_api)
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["This image is an unsolved sudoku grid. Give me just an array in format [[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]] of the digidts in this sudoku grid, when threre is no digit place 0. Please respond just with [][], no additional words.",
              image])

print(response.text)


# # image1_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
# image1_media_type = "image/jpeg"
# # image1_data = base64.standard_b64encode(httpx.get(image1_url).content).decode("utf-8")


# client = anthropic.Anthropic(
#     # defaults to os.environ.get("ANTHROPIC_API_KEY")
#     api_key=api,
# )

# message = client.messages.create(
#     model="claude-3-5-sonnet-20241022",
#     max_tokens=1024,
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "image",
#                     "source": {
#                         "type": "base64",
#                         "media_type": image1_media_type,
#                         "data": base64_image,
#                     },
#                 },
#                 {
#                     "type": "text",
#                     "text": "This image is an unsolved sudoku grid. Give me just an array in format [[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]] of the digidts in this sudoku grid, when threre is no digit place 0. Please respond just with [][], no additional words."
#                 }
#             ],
#         }
#     ],
# )
# print(message.content)



# Function to encode the image
# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode("utf-8")


# # Path to your image
# image_path = "Sudoku.png"

# # Getting the Base64 string
# base64_image = encode_image(image_path)

# response = client.chat.completions.create(
#     model="gpt-4o-2024-08-06",
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "This image is an unsolved sudoku grid. Give me just an array in format [[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]] of the digidts in this sudoku grid, when threre is no digit place 0. Please respond just with [][], no additional words.",
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {"url": f"data:image/png;base64,{base64_image}"},
#                 },
#             ],
#         }
#     ],
# )

# print(response.choices[0])