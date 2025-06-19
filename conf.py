from decouple import config
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel, Agent, Runner


my_key = config("GEMINI_API_KEY")

client = AsyncOpenAI(api_key=my_key ,
 base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

Model= OpenAIChatCompletionsModel(  model="gemini-2.0-flash", openai_client=client)
