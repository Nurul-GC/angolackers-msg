#  Copyright (c) 2019-2021 Nurul GC
#  Direitos Autorais (c) 2019-2021 Nurul GC
#
#   Jovem Programador
#  Estudante de Engenharia de Telecomunicaçoes
#  Tecnologia de Informação e de Medicina.
#  Foco Fé Força Paciência
#  Allah no Comando.
"""configuracoes do site"""

import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ANGOLACKERS_ACADEMY'
