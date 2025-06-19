from decouple import config
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel, Agent, Runner
import asyncio

my_key = config("GEMINI_API_KEY")

client = AsyncOpenAI(api_key=my_key,
                     base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

Model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

accountant = Agent(
    name="Ahmed Raza Dahrolia",
    instructions="""
    You are a helpful Pakistani Chartered Accountant. Your name is Ahmed Raza Dahrolia.
    You work for the user, and you're an expert at explaining accounting concepts clearly.
    Be polite, friendly, and use Urdu-English mix if it helps clarify things.
    """,
    model=Model,
)

async def main():
    user_input = input("Ask your accountant anything: ")  # 🔥 dynamic input here
    result = await Runner.run(accountant, user_input)
    print("\n--- Response from Ahmed Raza Dahrolia ---\n")
    print(result.final_output)

asyncio.run(main())
