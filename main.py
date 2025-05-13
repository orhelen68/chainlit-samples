from openai import AsyncOpenAI
import os
import chainlit as cl
import httpx

# client = AsyncOpenAI()
client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    http_client = httpx.AsyncClient(verify=False)
)

# Instrument the OpenAI client
cl.instrument_openai()

settings = {
    "model": "deepseek/deepseek-r1:free",
    "temperature": 0,
    # ... more settings
}

@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful and humourous bot and you always reply in both English and Traditional Chinese",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()