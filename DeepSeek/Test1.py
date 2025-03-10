#API Key: sk-c28954ef0af24db99ad27ae6b5352dbd
#https://api.deepseek.com
#pip3 install openai

from openai import OpenAI

client = OpenAI(api_key="sk-c28954ef0af24db99ad27ae6b5352dbd", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)