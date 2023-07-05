from datetime import datetime as dt


class Converter:
    @staticmethod
    def current_date_time() -> str:
        now = dt.now()
        return now.strftime("%d/%m/%Y %H:%M:%S")
