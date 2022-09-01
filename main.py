import asyncio
from asyncio import tasks
import sys

from scanner.readConfig import readConfig
from commands.runCommand import runCommand


async def main():
    tasks = []
    for fileName in ['inventory.ini', 'commands.ini']:
        tasks.append(asyncio.create_task(readConfig(fileName)))
    inventory, commands = await asyncio.gather(*tasks)
    await runCommand(inventory, commands)

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except Exception as e:
        sys.exit(f"Unable to execute the given commands due to {e}")
