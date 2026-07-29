import json
from pathlib import Path

from config import MEMORY_DIR
from core.logger import Logger


class MemoryEngine:

    def __init__(self):
        self.memory_file = Path(MEMORY_DIR) / "selectors.json"
        self.permissions_file = Path(MEMORY_DIR) / "permissions.json"

    def load(self):

        Logger.info("Loading learned memory...")

        with open(self.memory_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        Logger.success("Memory loaded")

        return data

    def save(self, data):

        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        Logger.success("Memory updated")

    def load_permissions(self):

        with open(self.permissions_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_permissions(self, data):

        with open(self.permissions_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        Logger.success("Permissions saved")
