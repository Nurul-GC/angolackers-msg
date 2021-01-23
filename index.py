"""
script principal do projecto
para executa-lo basta navegar ate a localização atual do script
e digitar no terminal:
*** linux ***
    ~$: python3 ./index.py
*** windows ***
    C/localizacao/do/script/:py index.py
"""
from app import app

if __name__ == '__main__':
    # ATT: o (debug=True) é apenas para durante o processo de desenvolvimento do programa..
    app.run(host='localhost', debug=True)
