from flaskr.utils.converter import Converter

class Debug:
    def __init__(self, texto):
        f = open('debug.txt', 'a')
        f.write(Converter.data_atual_string() + ': ' + str(texto) +'\n')
        f.close()