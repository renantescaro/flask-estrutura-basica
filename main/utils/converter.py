from datetime import datetime as dt

class Converter:
    @staticmethod
    def data_atual_string() -> str:
        data_hoje = dt.now()
        return str(data_hoje.strftime('%d/%m/%Y %H:%M:%S'))
