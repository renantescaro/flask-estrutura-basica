from main.utils.converter import Converter


class Debug:
    def __init__(self, text: str) -> None:
        with open("debug.txt", "a") as f:
            f.write(f"{Converter.current_date_time()}: {text}" + "\n")
