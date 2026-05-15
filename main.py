import ok
import ok.capture

import src.globals
import src.tasks.FishingTask
import src.tasks.SRTriggerTask

from src.config import config

if __name__ == '__main__':
    config = config
    ok = ok.OK(config)
    ok.start()
