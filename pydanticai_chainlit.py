import os
import httpx
import chainlit as cl
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider


os.environ["OPENROUTER_API_KEY"] = OPENROUTER_API_KEY

# ✅ Set up the OpenAI provider with the OpenRouter API key

model = OpenAIModel(
    'deepseek/deepseek-prover-v2:free',
    provider=OpenAIProvider(
        base_url='https://openrouter.ai/api/v1',
        api_key=os.getenv("OPENROUTER_API_KEY")
    )
)

bilingual_agent = Agent(
    model = model,
    system_prompt='You are a helpful and humourous assistant who always replies in English paragraphs of about 50-100 words, you are always funny, always ready with a joke or a fun fact in your response. You are also always polite and when the user responds to your reply with a short phrase like great, good job etc, you reply with thank you.'
)

# ✅ Define the Chainlit app
@cl.on_message
async def handle_message(message):
    response = bilingual_agent.run_sync(message.content)
    await cl.Message(content=response.output).send()
 
#bilingual_agent2 = Agent(
#    model = model,
#    system_prompt='You are a helpful and humourous assistant who always replies in both English and Japanese.'
#)   
    
result_sync = bilingual_agent.run_sync('Give me a slogan for a new product that is a combination of a toothpaste and mouthwash.')
#print(result_sync.output)

#print ('-----------------------------------')

#result_sync2 = bilingual_agent2.run_sync('Give me a slogan for a new product that is a combination of a toothpaste and mouthwash.')
#print(result_sync2.output)