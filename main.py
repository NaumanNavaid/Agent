from employee_agents.accountant import accountant
from agents import Runner , enable_verbose_stdout_logging
import asyncio

enable_verbose_stdout_logging()

async def main():
    
    response = await Runner.run(accountant, input="Tell me the total fee structure of CA in Pakistan?")
   
    print(response)

asyncio.run(main())






