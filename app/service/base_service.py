import pytz
import json
import aiofiles

from datetime import datetime


def get_moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).replace(tzinfo=None)
    return moscow_time


async def read_json_async(file_path):
    async with aiofiles.open(file_path, mode='r', encoding='utf-8') as f:
        contents = await f.read()
        return json.loads(contents)


async def write_json_async(file_path, data):
    async with aiofiles.open(file_path, mode='w', encoding='utf-8') as f:
        await f.write(json.dumps(data, ensure_ascii=False, indent=4))
