import myLog
import time
from myLog import logger

myLog.setUniqueLogFile("helloProg")
logger.info("program starting")
print("hello")
name = input("what is your name?\n")
logger.debug(f"Name read: {name}")
print(f"Hello {name}, my name is bot")
logger.info("program done")