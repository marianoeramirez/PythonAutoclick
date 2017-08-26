import pyautogui

from utils.autoclick import AutoClick
from utils import pyxhook

log_file = 'file.log'


class KeyPress():
    threadClick = None

    running = False

    def onKeyPress(self, event):
        fob = open(log_file, 'a')
        fob.write(event.Key)
        fob.write('\n')

        if event.Key == "F11":
            if self.running:
                self.running = False
                self.threadClick.cancel()
            else:
                self.running = True
                self.threadClick = AutoClick()
                self.threadClick.set_position(*pyautogui.position())
                self.threadClick.start()

        if event.Key == "bar":
            if self.running:
                self.running = False
                self.threadClick.cancel()
            fob.close()
            new_hook.cancel()

key = KeyPress()
# instantiate HookManager class
new_hook = pyxhook.HookManager()
# listen to all keystrokes
new_hook.KeyDown = key.onKeyPress
# start the session
new_hook.start()
