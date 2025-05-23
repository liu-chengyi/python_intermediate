# five security levels (low to high)
# Debug, Info, Warning, Error, Critical

import logging

# change default security level
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("Tommy's Logger")

# create a file handler

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("mylog.log") # the file would log to
handler.setLevel(logging.INFO) # only want info or above in my log file

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("This is a debug message!")
logger.info("This is important information!")