import os
from typing import Any
from dotenv import load_dotenv

class Config:
    @staticmethod
    def arquivo_vazio():
        return os.stat('.env').st_size == 0

    @staticmethod
    def limpar():
        open('.env', 'w').close()

    @staticmethod
    def set(hash:str, valor:Any):
        if Config.get(hash) is None:
            with open('.env', 'a') as f:
                f.write(f'{hash.upper()}={valor}\n')

    @staticmethod
    def get(hash: str) -> str:
        load_dotenv()
        return os.getenv(hash.upper(), '')
