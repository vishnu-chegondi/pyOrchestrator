import aiofiles
import configparser


async def readConfig(configFile):
    async with aiofiles.open(configFile, "r+") as invFO:
        contents = await invFO.readlines()
    config = configparser.ConfigParser()
    config.read_string("\n".join(contents))
    return config
