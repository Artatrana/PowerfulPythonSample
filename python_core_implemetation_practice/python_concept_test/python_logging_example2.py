# A fake API call is made.
# Different log levels show different system events.

import  logging
import random

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler() ] # ensures immediate flush
)

def fake_api_call():
    logging.info("Starting API call...")

    latency = random.randint(50, 3000) # ms
    logging.debug(f"API latency (ms): {latency}")

    if latency > 2000:
        logging.warning("API response is VERY slow")

    # Simulated failures
    if random.random() < 0.1:
        logging.error("API returned 500 Internal Server Error")
        return None

    if random.random() < 0.05:
        logging.critical("API server unreachable!")
        return None

    logging.info("API Call is successful")
    return {"data": "OK"}

# Driver code
print("---- Running API Simulation ----")

for _ in range(5):
    response = fake_api_call()
    print("Response:", response)

