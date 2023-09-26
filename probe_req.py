#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo tenta 
  fazer a localização
  de clientes conectados
  aos pontos de acessos
  wifi com o Dot11ProbeReq

  Modificado em 19 de dezembro de 2016
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importação das bibliotecas necessárias
from scapy.all import *


interface ='wlan1mon' # Interface de rede escolhida
probe_req = []        # Lista vazia
ap_name = raw_input("Coloque o nome do SSID: ")  # O nome do SSID a ser colocado


# Função que faz a tentativa de verificação de clientes ao roteador 
def probesniff(fm):
	if fm.haslayer(Dot11ProbeReq): # O 'Dot11ProbeReq' que faz a localização de clientes ao ponto de acesso sem fio.
		client_name = fm.info
		if client_name == ap_name :
			if fm.addr2 not in probe_req:
				print "Novo pedido de sonda: ", client_name 
				print "MAC do cliente: ", fm.addr2
				probe_req.append(fm.addr2)
			
sniff(iface= interface,prn=probesniff)










