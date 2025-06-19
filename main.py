from conf import Model
from agents import Agent, Runner
import asyncio

accountant = Agent(
    name="Ahmed raza dahrolia",
    instructions="You are a helpful assistant that can help with accounting tasks. Your name is  ahmed raza dahrolia and you are a employee of the user and you are an qualified CA.",
    model=Model,
)

async def main():
    response = await Runner.run(accountant, "Tell me the total fee structure of CA in Pakistan?")
    print(response)

asyncio.run(main())






