import os


def run(data: float, divisor: float) -> float:
    token = os.environ.get("API_TOKEN")
    if not token:
        raise EnvironmentError("API_TOKEN environment variable is not set")
def run(data, divisor):
    if divisor == 0:
        raise ValueError("divisor must not be zero")
    value = data / divisor
    return value
    return value
