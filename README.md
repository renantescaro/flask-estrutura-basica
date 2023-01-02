# Estrutura básica Flask


## Configurações ⚙️
* arquivo .env

<br>

## No Windows 🪟
1 - Instalar todas as dependências
```bash
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

2 - Executar
```bash
venv\Scripts\activate.bat
python run.py
```

<br>

## No Linux 🐧
1 - Instalar todas as dependências
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2 - Executar
```bash
source venv/bin/activate
python run.py
```

<br>

## Executar modo dev 🧪
```bash
python -m flask --app main --debug run
```
