"""use cache result in python
"""
from dataclasses import dataclass
from typing import List
from time import time, sleep
from functools import lru_cache


@dataclass
class Response:
    """api response simulator
    """
    status_code: int
    execution_time: int
    content: str


@lru_cache(maxsize=4)
def fake_api_caller(api_url: str) -> Response:
    """call the fake api

    Args:
        api_url (str): url of api

    Returns:
        Response: response of api. (status, tie, content)
    """
    url_length: int = len(api_url)
    sleep(url_length / 1000)
    return Response(
        status_code=200,
        execution_time=url_length,
        content=api_url*url_length
    )


urls: List[str] = [
    "https://github.com/dori-dev"
    "https://www.youtube.com/channel/UC8PIMbjxztHeiBWZRpblp2A"
    "https://www.google.com/search?q=dori+dev"
    "https://virgool.io/@dori-dev"
    "https://www.aparat.com/dori.dev"
]

RUN_COUNT = 100

start: float = time()
for i in range(RUN_COUNT):
    for url in urls:
        result: Response = fake_api_caller(url)
    for url in urls[::-1]:
        result: Response = fake_api_caller(url)
end: float = time()

time_average = (end - start) / RUN_COUNT
print(f"run time average: {time_average}")
print(fake_api_caller.cache_info())
fake_api_caller.cache_clear()
