Monitoramento Contínuo dos Batimentos Cardíacos (IoT)

Descrição do Projeto

Este projeto tem como objetivo o desenvolvimento de um protótipo de sistema portátil para o monitoramento contínuo dos batimentos cardíacos, utilizando sensores flexíveis conectados via Internet das Coisas (IoT). A solução foi idealizada para ser acessível, permitindo que pacientes, especialmente idosos e aqueles com doenças cardíacas, sejam monitorados sem a necessidade de internação constante. O sistema também integra uma rede de atendimento emergencial para envio de dados em tempo real a profissionais de saúde.

O projeto segue a metodologia de Design Thinking, focando nas necessidades dos usuários e na criação de soluções inovadoras e funcionais.

Tecnologias Utilizadas

Backend: Django REST Framework

Banco de Dados: MySQL (Workbench)

Frontend: HTML

Instalar o Python
Acesse o site oficial do Python: https://www.python.org/downloads/

Baixe a versão mais recente compatível com o seu sistema operacional.

Durante a instalação, marque a opção "Add Python to PATH".

Verifique a instalação executando o seguinte comando no terminal ou prompt de comando:

python --version

Acesse o site do MySQL Workbench: https://dev.mysql.com/downloads/windows/installer/8.0.html

Baixe a primeira versão que aparece.

Após a instalação, abra o MySQL Workbench e crie um banco de dados para o projeto:
CREATE DATABASE monitoramento;

Após isso, clone o repositório com:
git clone https://github.com/mateus-schiavi/PI-III.git
e execute o seguinte comando:
cd backend

No arquivo settings.py, adicione o seguinte trecho de código:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'monitoramento',
        'USER': 'root',
        'PASSWORD': '', --> aqui vai a senha que você configurou para acessar o workbench
        'HOST': 'localhost',
        'PORT': '3306',
    }
},

em seguida, execute este comando no terminal:
python manage.py migrate
e em seguida execute:
python manage.py runserver

