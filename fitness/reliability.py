import time

import requests


def check_server_recovery(drop_url, check_url, check_interval=0.1, timeout=60):
    try:
        print("Dropping application...")
        drop_response = requests.post(drop_url)

        start_time = time.time()

        while time.time() - start_time < timeout:
            try:
                check_response = requests.get(check_url)
                if check_response.status_code == 200:
                    recovery_time = time.time() - start_time
                    print(f"Server is up! Recovery time: {recovery_time:.2f} seconds")
                    return recovery_time * 1000
                else:
                    print(f"Server not ready. Status code: {check_response.status_code}")
            except requests.exceptions.RequestException:
                print("Server is still down...")

            time.sleep(check_interval)

        print("Server recovery timeout reached.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


DOMAIN = ""
DROP_CODE = ""

drop_url = f'https://{DOMAIN}/api/drop-application?drop_code={DROP_CODE}'
check_url = f'https://{DOMAIN}/api/messages/count'


def measure_average_get_request_time_in_ms(n):
    s = 0
    for i in range(n):
        s += check_server_recovery(drop_url, check_url)
        time.sleep(10)
    return s / n


print(measure_average_get_request_time_in_ms(5))
