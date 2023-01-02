from main.utils.converter import Converter

class Debug:
    def __init__(self, texto:str) -> None:
        with open('debug.txt', 'a') as f:
            f.write(f'{Converter.data_atual_string()}: {texto}' + '\n')
