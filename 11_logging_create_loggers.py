# five security levels (low to high)
# Debug, Info, Warning, Error, Critical

import logging
# example 1: using default logger

# python has default security level of "WARNING"
# so by default can only see above Warning

# change default security level
logging.basicConfig(level=logging.DEBUG)
logging.info("You have got 20 mails in your inbox")
logging.critical("All component failed")

# example 2: create own logger

logger = logging.getLogger("Tommy's Logger")
logger.info("The best logger was just created!")
logger.critical("Your email was deleted")
logger.log(logging.ERROR, "An error occured")