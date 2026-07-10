import logging
import uuid
from datetime import datetime

logfilename = "learn_log.log"
logging.basicConfig(
    filename=logfilename,
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

now = datetime.now()


try:

    logging.info(
        f"[{now}] ==Start=="
    )

    loginfo_car = {
        "id": 1001,
        "modal": "Chiron",
        "company": "Buggati",
        "price":0, 
        "year":''
    }

    logging.info(
        f"[{now}] read car"
    )
    logging.info(loginfo_car)
    
    if not loginfo_car["year"]:
        logging.warning(
            f"[{now}] Missing year"
        )

    result = 10 / loginfo_car['price']

    logging.info(
        f"[{now}] == END=="
    )

except ZeroDivisionError as e:

    # Error log
    logging.error(
        f"[{now}] API calculation failed: {e}"
    )

    logging.exception(
        f"[{now}] Full exception details"
    )

print("Program completed")
