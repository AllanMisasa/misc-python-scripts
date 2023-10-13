# pip install watchdog

import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

class watch_folder:

    def __init__(self, path_to_watch = '.', polling_interval=1.0):
        self.observer = Observer()
        self.path_to_watch = path_to_watch
        self.polling_interval = polling_interval

    def watch(self):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        event_handler = LoggingEventHandler()
        self.observer.schedule(event_handler, self.path_to_watch, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(self.polling_interval)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
 
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Event is created, you can process it now
            print("Watchdog received created event - % s." % event.src_path)
        elif event.event_type == 'modified':
            # Event is modified, you can process it now 
            print("Watchdog received modified event - % s." % event.src_path)

if __name__ == '__main__':
    watcher = watch_folder("/home/janus/Downloads")
    watcher.watch()