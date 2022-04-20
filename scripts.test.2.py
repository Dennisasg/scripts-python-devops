#Dicionário: Estrutura de dados primitiva que adota o padrãp chave:valor
nome_dicionario = {'Ano': 2022, 'IP': '192.168.0.1'}
for i in nome_dicionario.items():
  print(i)
type(nome_dicionario)

import pandas as pd
planilha = pd.read_csv('/content/prova_iris.csv.csv')
type(planilha)
planilha.info()
print(planilha['petal_length'])

#pip install smtplib

import smtplib
sender = "Fabio Gomes <gomesrocha@gmail.com>"
receiver = "Fabio Rocha <fabio.rocha@faculdadeimpacta.com.br>"

mensagem_email = f"""\
  subject: Testando o servidor
  To: {receiver}
  From: {sender}

  Testando """
with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
  server.login("ca5868946bea94", "3abf7c31ea7d20")
  server.sendmail(sender, receiver, mensagem_email)


!pip install ping3
Collecting ping3
  Downloading ping3-4.0.2-py3-none-any.whl (13 kB)
Installing collected packages: ping3
Successfully installed ping3-4.0.2

from ping3 import ping, verbose_ping
dados = ping('meusite.edu.br')


sender = "Fabio Gomes <gomesrocha@gmail.com>"
receiver = "Fabio Rocha <fabio.rocha@faculdadeimpacta.com.br>"

message = f"""\
Subject: Ping
To: {receiver}
From: {sender}

Resultado do ping: {dados}"""

if dados == False:
  with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
      server.login("419c3116741b3d", "6e359f31654beb")
      server.sendmail(sender, receiver, message)


