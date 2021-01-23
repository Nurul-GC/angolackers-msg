#  Copyright (c) 2019-2021 Nurul GC
#  Direitos Autorais (c) 2019-2021 Nurul GC
#
#   Jovem Programador
#  Estudante de Engenharia de Telecomunicaçoes
#  Tecnologia de Informação e de Medicina.
#  Foco Fé Força Paciência
#  Allah no Comando.
"""documentacao do jogo adivinha a palavra"""

from flask import Flask
from app.config import Config
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
# app.config['SECRET_KEY'] = '9991'
# Bootstrap(app=app)

from app import routes
