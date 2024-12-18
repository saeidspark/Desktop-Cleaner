from source.directories import Directories
from source.mover import MoverHandler
from source.startup import Startup
from watchdog.observers import Observer
import logging
from time import sleep
import os

# ! NO NEED TO CHANGE BELOW CODE
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    directories = Directories()
    startup = Startup()
    startup.add_to_startup()
    
    event_handler = MoverHandler()
    event_handler.start()
    
    path = event_handler.source_dir
    
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()