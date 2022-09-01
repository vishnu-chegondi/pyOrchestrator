import asyncio
import asyncssh


async def runCommand(inventory, commands):
    for remote_host in inventory["hosts"]["hostList"].split(","):
        # Connect to remote host
        hostIp, username, port, password = (
            inventory[remote_host]["ip"],
            inventory[remote_host]["username"],
            int(inventory[remote_host]["port"]),
            inventory[remote_host]["password"],
        )
        async with asyncssh.connect(
            hostIp,
            username=username,
            known_hosts=None,
            password=password,
            port=port,
        ) as conn:
            print(f"-------Connected to {remote_host}--------", end="\n")
            for command in commands["commands"]["listCommands"].split(","):
                result = await conn.run(command, check=True)
                print(f"---> Output of {command} on {remote_host} is:\n {result.stdout}", end="")
