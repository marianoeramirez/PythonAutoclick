import threading

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s %(threadName)s] %(message)s',
                    datefmt='%H:%M:%S')

class AutoClick(threading.Thread):
    def __init__(self, x=None, y=None):
        threading.Thread.__init__(self)
        self.finished = threading.Event()
        self.x = x
        self.y = y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def run(self):
        i = 0
        while not self.finished.isSet():
            logger.info(i)
            pyautogui.moveTo(self.x, self.y, duration=0.25)
            pyautogui.click(self.x, self.y)
            time.sleep(.5)
            i += 1

    def cancel(self):
        logger.info("cancel")
        self.finished.set()