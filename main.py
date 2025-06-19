from employee_agents.accountant import accountant
from agents import Runner
import asyncio



async def main():
    
    response = await Runner.run(accountant, input="Tell me the total fee structure of CA in Pakistan?")
   
    print(response)

asyncio.run(main())






