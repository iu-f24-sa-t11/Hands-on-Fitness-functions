import time

import requests

URL = 'https://adme-chat.duckdns.org/api/messages/count'


def measure_get_request_time_in_ms(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    if response.status_code != 200:
        raise Exception("Error with status code", response.status_code)

    return (end_time - start_time) * 1000


def measure_average_get_request_time_in_ms(n, url):
    return sum([measure_get_request_time_in_ms(url) for i in range(n)]) / n


print(measure_average_get_request_time_in_ms(100, URL))
