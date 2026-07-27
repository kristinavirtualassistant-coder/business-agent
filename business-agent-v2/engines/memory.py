import json
from pathlib import Path

from config import MEMORY_DIR

from core.logger import Logger


class MemoryEngine:

    def __init__(self):

        self.file = Path(MEMORY_DIR) / "selectors.json"

    def load(self):

        Logger.info("Loading learned memory...")

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        Logger.success("Memory loaded")

        return data

    def save(self, data):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )

        Logger.success("Memory updated")
