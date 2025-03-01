import os
import time
import logging
import shutil

import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileCreatedEvent

# Configure logging
logging.basicConfig(level=logging.INFO)
Log = logging.getLogger(__name__)


class PathUtils:
    @staticmethod
    def get_complete_path(path_in_dir: str) -> str:
        return os.path.join(
            os.path.dirname(os.path.realpath(__file__)), path_in_dir
        )

    @staticmethod
    def return_extension(path: str) -> str:
        return (os.path.basename(path)).split(".")[-1]


PATH_INPUT: str = PathUtils.get_complete_path(os.getenv("FILE_INPUT", None))
PATH_OUTPUT: str = PathUtils.get_complete_path(os.getenv("FILE_OUTPUT", None))


class Handler(FileSystemEventHandler):
    # Class with all the methods that will handle the events when a file is
    # created, deleted, modified, moved, etc.

    @staticmethod
    def on_created(event: FileCreatedEvent) -> None:
        # The process triggers if the file a CSV
        if not event.is_directory:
            if PathUtils.return_extension(event.src_path).upper() == "CSV":
                Log.info(f"CSV detected: {event.src_path}")

                # Handles if there are any error with the transformations
                try:
                    # Make the cleaning of the file
                    df = pd.read_csv(event.src_path)
                    df = df.dropna()
                    df = df.drop_duplicates()

                    # Save the results as output
                    df.to_csv(event.src_path, index=False)
                    shutil.move(
                        event.src_path,
                        os.path.join(
                            PATH_OUTPUT, os.path.basename(event.src_path)
                        ),
                    )

                except ValueError as val_err:
                    Log.error("There has been an error when the CSV cleaning")
                    Log.debug(val_err.args)
                except shutil.Error as shutil_err:
                    Log.error("Error when the movement of files has been done")
                    Log.debug(shutil_err.args)


class WatchDog:
    def __init__(self):
        self.observer = Observer()

    def start(self) -> None:
        self.observer.schedule(Handler(), PATH_INPUT)
        self.__start_loop()

    def __start_loop(self) -> None:
        # The watchdogs only stops when is sent a ctrl+c
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


if __name__ == "__main__":
    WatchDog().start()
