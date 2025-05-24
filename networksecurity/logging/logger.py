import logging
import os
from datetime import datetime

# //Log filename
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# //Log path
logs_dir=os.path.join(os.getcwd(),'Logs')
os.makedirs(logs_dir,exist_ok=True)


LOG_FILE_PATH=os.path.join(logs_dir,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d - %(levelname)s: %(message)s',
    level=logging.INFO
)
