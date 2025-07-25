
# 1.Listen for changes in the screenshot folder           DONE
# 2.Parse the image and use recognition
# 3.Place the image into the apropriate folder

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time, sys, os

DEFAULT_PATH = os.path.join(os.path.expanduser("~"), "Pictures", "Screenshots")

def get_watch_path():
    if len(sys.argv) == 2 and os.path.exists(sys.argv[1]):
        return sys.argv[1]
    return DEFAULT_PATH

class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, e):
        print("Pic Path: ", e.src_path)
        print(e)

def watch_repository(dir_path, event_handler):
    observer = Observer()
    observer.schedule(event_handler, dir_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(DEFAULT_PATH)
        print("PROGRAM STOPPED")
        observer.stop()
    observer.join()

def main():
    watch_repository(get_watch_path(), ScreenshotHandler())
    

if __name__ == "__main__":
    main()