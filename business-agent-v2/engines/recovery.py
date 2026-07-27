from core.logger import Logger


class RecoveryEngine:

    def retry(self, action, attempts=3):

        for attempt in range(1, attempts + 1):

            try:

                return action()

            except Exception as e:

                Logger.warning(
                    f"Attempt {attempt} failed: {e}"
                )

        Logger.error("Recovery failed")

        return False
