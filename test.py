# # from openai import OpenAI
# # import os
# # from dotenv import load_dotenv

# # load_dotenv()


# # client = OpenAI(
# #     api_key= os.getenv('OPENROUTER_API_KEY'),
# #     base_url="https://openrouter.ai/api/v1",
# # )

# # response = client.chat.completions.create(
# #     model="openrouter/free",
# #     messages=[
# #         {"role": "user", "content": "My name is Sahil!"}
# #     ]
# # )


# # print(response.choices[0].message.content)

# # from mistralai.client import Mistral
# # from dotenv import load_dotenv
# # import os

# # load_dotenv()

# # client = Mistral(
# #     api_key=os.getenv("MISTRAL_API_KEY")
# # )

# # models = client.models.list()

# # for model in models.data:
# #     print(model.id)



# from mistralai.client import Mistral
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = Mistral(
#     api_key=os.getenv("MISTRAL_API_KEY")
# )

# response = client.chat.complete(
#     model="mistral-small-latest",
#     messages=[
#         {
#             "role": "user",
#             "content": "Hello!" 
#         }
#     ]
# )


# print(response.choices[0].message.content)


from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1"
)

# models = client.models.list()

# for model in models.data:
#     print(model.id)


# response = client.chat.completions.create(
#     model="meta/llama-3.2-90b-vision-instruct",
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "Describe this image."
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": "https://media.licdn.com/dms/image/v2/D5622AQED9nXwFVhXZQ/feedshare-shrink_800/feedshare-shrink_800/0/1696417959065?e=2147483647&v=beta&t=lo3PrayqMheU89RXqjKIt22s1almDHGNTSGjSt8eVXIhttps://media.licdn.com/dms/image/v2/D5622AQED9nXwFVhXZQ/feedshare-shrink_800/feedshare-shrink_800/0/1696417959065?e=2147483647&v=beta&t=lo3PrayqMheU89RXqjKIt22s1almDHGNTSGjSt8eVXI"
#                 }
#                 }
#             ]
#         }
#     ]
# )

# print(response)


response = client.chat.completions.create(
    model="meta/llama-3.1-70b-instruct",
    messages=[
        {
            "role": "user",
            "content": "What is langchain"
        }
    ]
)

print(response.choices[0].message.content)