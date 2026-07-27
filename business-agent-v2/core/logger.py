from datetime import datetime


class Logger:

    @staticmethod
    def _stamp():
        return datetime.now().strftime("%H:%M:%S")

    @classmethod
    def info(cls, message):
        print(f"[{cls._stamp()}] INFO  {message}")

    @classmethod
    def success(cls, message):
        print(f"[{cls._stamp()}] OK    {message}")

    @classmethod
    def warning(cls, message):
        print(f"[{cls._stamp()}] WARN  {message}")

    @classmethod
    def error(cls, message):
        print(f"[{cls._stamp()}] ERROR {message}")

    @classmethod
    def section(cls, title):
        print()
        print("=" * 70)
        print(title)
        print("=" * 70)
