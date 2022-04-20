# List Comprehensions

roupas = ['Camiseta', 'Camisa', 'Camisa Polo']
tamanhos = ['PP', 'P', 'M', 'G', 'GG', 'XGG', 'Cara você é gordo']
pecas_roupa = [(tipo, size) for tipo in roupas for size in tamanhos]
print(pecas_roupa)


import pickle
#salva os dados,  em um arquivo binário com o pickle - Formato do Python
pickle.dump(pecas_roupa, open('pecas_vendas.pk', "wb"))

# Abre o arquito pickle e salva em uma lista
minha_lista_de_roupas = pickle.load(open('pecas_vendas.pk', "rb"))
print(minha_lista_de_roupas)

type(minha_lista_de_roupas)
len(minha_lista_de_roupas)
minha_lista_de_roupas.append(('Bermuda', 'G'))

print(minha_lista_de_roupas)

# Remove o item pelo id - Posição na lista
minha_lista_de_roupas.pop(len(minha_lista_de_roupas)-1)

# Remove o item específico
minha_lista_de_roupas.remove(('Bermuda', 'G'))

print(minha_lista_de_roupas)

import pandas as pd
dados = pd.read_excel('aula_python.xlsx')
dados_pk = pd.read_pickle('pecas_vendas.pk')
print(dados)


print(dados_pk)

import matplotlib.pyplot as plt
dados.iloc[:,1].plot()
dados.iloc[:,2].plot()
dados.iloc[:,3].plot()
plt.legend(['Planejado', 'Realizado', 'Velocidade Média'], title='Sprint')



#Instalação do NMPA-Linux 

!pip install python3-nmap
Collecting python3-nmap
  Downloading python3_nmap-1.5.1-py3-none-any.whl (25 kB)
Collecting simplejson
  Downloading simplejson-3.17.6-cp37-cp37m-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (130 kB)
     |████████████████████████████████| 130 kB 11.5 MB/s 
Installing collected packages: simplejson, python3-nmap
Successfully installed python3-nmap-1.5.1 simplejson-3.17.6


!sudo apt install nmap
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  liblinear3 liblua5.3-0 libpcap0.8
Suggested packages:
  liblinear-tools liblinear-dev ndiff
The following NEW packages will be installed:
  liblinear3 liblua5.3-0 libpcap0.8 nmap
0 upgraded, 4 newly installed, 0 to remove and 39 not upgraded.
Need to get 5,446 kB of archives.
After this operation, 24.9 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 libpcap0.8 amd64 1.8.1-6ubuntu1.18.04.2 [118 kB]
Get:2 http://archive.ubuntu.com/ubuntu bionic/main amd64 liblinear3 amd64 2.1.0+dfsg-2 [39.3 kB]
Get:3 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 liblua5.3-0 amd64 5.3.3-1ubuntu0.18.04.1 [115 kB]
Get:4 http://archive.ubuntu.com/ubuntu bionic/main amd64 nmap amd64 7.60-1ubuntu5 [5,174 kB]
Fetched 5,446 kB in 2s (3,041 kB/s)
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76, <> line 4.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (This frontend requires a controlling tty.)
debconf: falling back to frontend: Teletype
dpkg-preconfigure: unable to re-open stdin: 
Selecting previously unselected package libpcap0.8:amd64.
(Reading database ... 155455 files and directories currently installed.)
Preparing to unpack .../libpcap0.8_1.8.1-6ubuntu1.18.04.2_amd64.deb ...
Unpacking libpcap0.8:amd64 (1.8.1-6ubuntu1.18.04.2) ...
Selecting previously unselected package liblinear3:amd64.
Preparing to unpack .../liblinear3_2.1.0+dfsg-2_amd64.deb ...
Unpacking liblinear3:amd64 (2.1.0+dfsg-2) ...
Selecting previously unselected package liblua5.3-0:amd64.
Preparing to unpack .../liblua5.3-0_5.3.3-1ubuntu0.18.04.1_amd64.deb ...
Unpacking liblua5.3-0:amd64 (5.3.3-1ubuntu0.18.04.1) ...
Selecting previously unselected package nmap.
Preparing to unpack .../nmap_7.60-1ubuntu5_amd64.deb ...
Unpacking nmap (7.60-1ubuntu5) ...
Setting up liblinear3:amd64 (2.1.0+dfsg-2) ...
Setting up liblua5.3-0:amd64 (5.3.3-1ubuntu0.18.04.1) ...
Setting up libpcap0.8:amd64 (1.8.1-6ubuntu1.18.04.2) ...
Setting up nmap (7.60-1ubuntu5) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
Processing triggers for libc-bin (2.27-3ubuntu1.3) ...
/sbin/ldconfig.real: /usr/local/lib/python3.7/dist-packages/ideep4py/lib/libmkldnn.so.0 is not a symbolic link



import nmap3
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("itp.org.br")


print(results)