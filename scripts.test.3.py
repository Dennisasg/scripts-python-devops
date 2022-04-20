#Instalando o ping3
!pip install ping3
Collecting ping3
  Downloading ping3-4.0.2-py3-none-any.whl (13 kB)
Installing collected packages: ping3
Successfully installed ping3-4.0.2

import smtplib
sender = "Fabio Gomes <gomesrocha@gmail.com>"
receiver = "Fabio Rocha <fabio.rocha@faculdadeimpacta.com.br>"

mensagem_email = f"""\
  subject: Testando o servidor
  To: {receiver}
  From: {sender}

  Testando """
with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
  server.login("3b33e14e9238a6", "f7af905c190285")
  server.sendmail(sender, receiver, mensagem_email)

  import smtplib
def enviar_email(sender, receiver, msg_email, subject_info):
  message = f"""\
  Subject: {subject_info}
  To: {receiver}
  From: {sender}
  {msg_email}."""
  with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
      server.login("3b33e14e9238a6", "f7af905c190285")
      server.sendmail(sender, receiver, message)

 mensagem = "Envio de email do joselito"
remetente = "Private Person <from@example.com>"
receptor = "A Test User <to@example.com>"
titulo_email = "Email de teste"
enviar_email(remetente, receptor, mensagem, titulo_email)

from ping3 import ping, verbose_ping
import time
import pandas as pd
resultado_ping = []
for n in range(20):
  resultado = ping('google.com.br')
  resultado_ping.append(resultado)
  time.sleep(1)
df_ping = pd.DataFrame(resultado_ping)
print(df_ping.shape)
print(df_ping.info())
df_ping.plot()

(20, 1)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20 entries, 0 to 19
Data columns (total 1 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   0       20 non-null     float64
dtypes: float64(1)
memory usage: 288.0 bytes
None
<matplotlib.axes._subplots.AxesSubplot at 0x7f6cd3fcdf50>


from datetime import datetime
def analise_ip_dominio(ip_domain, tempo=2, qtd=1):
  for i in range(qtd):
    resultado = ping(ip_domain)
    if resultado == False:
      mensagem = "Ocorreu um erro as " + str(datetime.today()) + " no IP/dominio " + ip_domain
      enviar_email("<fabio.rocha@faculdadeimpacta.com.br>", "<fabio.rocha@faculdadeimpacta.com.br>", mensagem, "Erro durante a execução")
    else:
      time.sleep(tempo)


dominio = 'google.com'
analise_ip_dominio(dominio, 1, 10)

def analise_ip_dominio_salvar(ip_domain, nome_arquivo, tempo=2, qtd=1, ):
  resultado_ping = []
  for n in range(qtd):
    resultado = ping(ip_domain)
    resultado_ping.append(resultado)
    time.sleep(tempo)
  df_ping = pd.DataFrame(resultado_ping)
  df_ping.to_csv(nome_arquivo)  


 # Rodando um ping, durante 1h a cada 120 segundos
#analise_ip_dominio_salvar('google.com', 'meu_ping.csv',120, 30)
analise_ip_dominio_salvar('google.com', 'meu_ping.csv',2, 10)

def analise_ip_dominio_retornar(ip_domain, nome_arquivo, tempo=2, qtd=1, ):
  resultado_ping = []
  for n in range(qtd):
    resultado = ping(ip_domain)
    resultado_ping.append(resultado)
    time.sleep(tempo)
  df_ping = pd.DataFrame(resultado_ping)
  return df_ping

analise_ip_dominio_retornar('google.com', 'meu_ping.csv',1, 4).plot.bar()


#Análise de informações com o Pandas
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

cotacao = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/44')
cotacao_tratada = json.loads(cotacao.content)
df_cotacao = pd.DataFrame(cotacao_tratada)
df_cotacao.shape


#Converter dados no pandas
df_cotacao['low'] = df_cotacao['low'].apply(pd.to_numeric)
df_cotacao['low'].plot()
df_cotacao['high'] = df_cotacao['high'].apply(pd.to_numeric)
df_cotacao['high'].plot()
df_cotacao['bid'] = df_cotacao['bid'].apply(pd.to_numeric)
df_cotacao['bid'].plot()
df_cotacao['ask'] = df_cotacao['ask'].apply(pd.to_numeric)
df_cotacao['ask'].plot()
plt.legend(['Mínimo', 'Máximo', 'Compra', 'Venda'], title='Dolar')


import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_excel('idhm.xlsx', 'Dados')
# Quantidade de linhas e colunas de um arquivo
print(dados.shape)
print(dados.columns)
print(dados.head())

print(dados['NOME_AGREGA'])
print(dados.loc[:, 'NOME_AGREGA'])
print(dados.iloc[:, [1, 3]])

print("Gráfico 1")
plt.plot(dados['NOME_AGREGA'], dados['ESPVIDA'])
plt.show()


import seaborn as sns

# use the function regplot to make a scatterplot
sns.regplot(x=dados['ANO'], y=dados['ESPVIDA'])


sns.boxplot(x=dados['ANO'], y=dados['ESPVIDA'])


sns.boxplot(x=dados['NOME_AGREGA'], y=dados['ESPVIDA'])

sudeste = ['SP', 'RJ', 'ES', 'MG']
lista_sudeste = dados[dados.NOME_AGREGA.isin(sudeste)]
sns.boxplot(x=lista_sudeste['NOME_AGREGA'], y=lista_sudeste['ESPVIDA'])

sul = ['RS', 'SC', 'PR']
lista_sul = dados[dados.NOME_AGREGA.isin(sul)]
sns.boxplot(x=lista_sul['NOME_AGREGA'], y=lista_sul['ESPVIDA'])


nordeste = ['MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA']
lista_nordeste = dados[dados.NOME_AGREGA.isin(nordeste)]
sns.boxplot(x=lista_nordeste['NOME_AGREGA'], y=lista_nordeste['ESPVIDA'])

media_vida_nordeste = lista_nordeste.groupby(['NOME_AGREGA'])['ESPVIDA'].mean()
plt.plot(media_vida_nordeste, color='skyblue', alpha=0.3)
plt.savefig("grafico.png", dpi=100)


ping_dados = pd.read_csv('meu_ping.csv')
plt.plot(ping_dados, color='red')
plt.savefig('ping.png', dpi=300)


import socket as sc
testconnect = sc.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  testconnect.connect(('google.com', 80))
  testconnect.close()
except:
  print("Erro")
  testconnect.close()

#Programação orientado a objeto
class testeConectividade:
    
  #Inicializador da classe, responsável pelas variáveis locais da classe
  def __init__(self, servidor):
    self.servidor = servidor
  #Método = função, porém pertencente a uma classe
  def testar_com_socket(self, porta=0):
    testconnect = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
    try:
      testconnect.connect((self.servidor, porta))
      testconnect.close()
    except:
      mensagem = "Ocorreu um erro as " + str(datetime.today()) + " no IP/dominio " + self.servidor
      enviar_email("<fabio.rocha@faculdadeimpacta.com.br>", "<fabio.rocha@faculdadeimpacta.com.br>", mensagem, "Erro durante a execução")
      testconnect.close()
  
  def testar_com_ping(self, tempo=2, qtd=1):
    for i in range(qtd):
      resultado = ping(self.servidor)
      if resultado == False:
        mensagem = "Ocorreu um erro as " + str(datetime.today()) + " no IP/dominio " + self.servidor
        enviar_email("<fabio.rocha@faculdadeimpacta.com.br>", "<fabio.rocha@faculdadeimpacta.com.br>", mensagem, "Erro durante a execução")
      else:
        time.sleep(tempo)

    dominios = ['google.com', 'google.com.br', 'meusite.com.br']
for i in dominios:
  resultado = testeConectividade(i)
  resultado.testar_com_socket(80)
  resultado.testar_com_ping(1, 5)

from abc import ABCMeta, abstractmethod
class teste(metaclass = ABCMeta):
  @abstractmethod
  def som(self):
    pass

class rock(teste):
 def som(self):
  print("Rock")

novo = rock()
novo.som()

def fabio():
  var1 = 10
  var2 = ['casa', 'feriado']
  return var1, var2

for i in fabio():
  print(i)

