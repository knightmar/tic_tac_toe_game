import threading

import tic_tac_toe
import utils_window


def launchApp():
    tic_tac_toe.launch()


def launchDebug():
    utils_window.launch()


if __name__ == "__main__":
    appThread = threading.Thread(target=launchApp)
    appThread.start()

    debugThread = threading.Thread(target=launchDebug)
    debugThread.start()
