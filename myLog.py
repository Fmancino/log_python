import logging
import datetime
import os

def assurePathExists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


# create logger 
logger = logging.getLogger('fma_log')

logger.setLevel(logging.DEBUG)

 # create formatter 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 

oldUniqueLogFile = ""
#logger.addHandler(oldUniqueLogFile)

def addConsoleHandler():
    ch = logging.StreamHandler() 
    ch.setLevel(logging.DEBUG)
    # add formatter to ch 
    ch.setFormatter(formatter) 
    # add ch to logger 
    logger.addHandler(ch) 

def setUniqueLogFile(name):
    global oldUniqueLogFile
    nowStr = datetime.datetime.now().isoformat(sep='_', timespec='seconds')
    logDir = "log"
    logName = f"{nowStr}_{name}.log"
    if not os.path.exists(logDir):
        os.makedir(logDir)

    fh = logging.FileHandler(os.path.join(logDir,logName), mode='a', encoding=None, delay=False)
    fh.setFormatter(formatter)
    logger.removeHandler(oldUniqueLogFile)
    logger.addHandler(fh)
    oldUniqueLogFile = fh
