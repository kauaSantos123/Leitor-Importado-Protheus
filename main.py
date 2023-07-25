import csv
import datetime
import os
import sys
import xml.etree.ElementTree as ET
from datetime import *
from time import sleep

import pandas as pd


def remover_csv():
    try:
        os.remove('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\importado_cte.csv')
        os.remove('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\importado_nfe.csv')
        os.remove('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\unidades.txt')
    except:
        print('arquivo nao existe')
    ler_dist_cte()


def ler_dist_cte():
    agora = datetime.now()
    main_path = "U:\\02-importado\\"
    #  escrever colunas arquivo txt
    with open('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\importado_cte.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['numero', 'valor', 'Data', 'chave', 'pasta'])
    with open('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\importado_nfe.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['numero', 'valor', 'Data', 'chave', 'pasta'])
    for root, subFolder, filename in os.walk(main_path):
        for t in subFolder:
            diretorio = ("U:\\02-importado\\%s") % (t)
            try:
                with open('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\unidades.txt', 'a') as arquivo:
                    arquivo.writelines(f'Inicio: {agora} lendo a empresa : {t}\n')
                    arquivo.writelines(f'Lido a unidade: {t}\n')
            except:
                pass
            # Obter a data atual
            data_atual = datetime.now()
            # Obter o ano atual
            ano_atual = data_atual.year
            # Criar um objeto de data para o início do ano atual
            inicio_do_ano_atual = datetime(ano_atual, 1, 1)
            # Percorre todos os arquivos do diretório
            for nome_arquivo in os.listdir(diretorio):
                try:
                    # Verifica se o arquivo é um arquivo XML
                    if nome_arquivo.endswith(".xml"):
                        # Obtém as informações de modificação do arquivo
                        caminho_completo = os.path.join(
                            diretorio, nome_arquivo)
                        data_modificacao = datetime.fromtimestamp(
                            os.path.getmtime(caminho_completo))
                        # Verifica se o arquivo foi modificado nos últimos 365 dias
                        if data_modificacao > inicio_do_ano_atual:
                            # Faz algo com o arquivo
                            arquivo = str(diretorio) + ("\\") + \
                                str(nome_arquivo)
                            xml_file = arquivo
                            tree = ET.parse(xml_file)
                            root = tree.getroot()
                            # Extrair o número e a chave do CTe

                            try:
                                ns = {'cte': 'http://www.portalfiscal.inf.br/cte'}

                                numero = root.find(
                                    './/cte:infCte/cte:ide/cte:nCT', ns).text
                                valor = root.find(
                                    './/cte:infCte/cte:vPrest/cte:vTPrest', ns).text
                                Data = root.find(
                                    './/cte:infCte/cte:ide/cte:dhEmi', ns).text
                                Data = F"{Data[8:10]}/{Data[5:7]}/{Data[:4]}"
                                chave = root.find(
                                    './/cte:infCte', ns).attrib['Id'][3:]
                                pasta = arquivo
                                # Escrever o número e a chave em um arquivo CSV
                                with open('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\importado_cte.csv', 'a', newline='') as csvfile:
                                    writer = csv.writer(csvfile, delimiter=',')
                                    writer.writerow(
                                        [numero, valor, Data, chave, pasta])
                            except:
                                print("Nota")
                                arquivo = str(diretorio) + ("\\") + \
                                    str(nome_arquivo)
                                xml_file = arquivo
                                tree = ET.parse(xml_file)
                                root = tree.getroot()
                                # Extrair o número e a chave do NFe
                                try:
                                    ns = {
                                        'nfe': 'http://www.portalfiscal.inf.br/nfe'}

                                    numero = root.find(
                                        './/nfe:NFe/nfe:infNFe/nfe:ide/nfe:nNF', ns).text
                                    valor = root.find(
                                        './/nfe:NFe/nfe:infNFe/nfe:total/nfe:ICMSTot/nfe:vNF', ns).text
                                    Data = root.find(
                                        './/nfe:NFe/nfe:infNFe/nfe:ide/nfe:dhEmi', ns).text
                                    Data = F"{Data[8:10]}/{Data[5:7]}/{Data[:4]}"
                                    chave = root.find(
                                        './/nfe:protNFe/nfe:infProt/nfe:chNFe', ns).text
                                    pasta = arquivo
                                    # Escrever os dados em um arquivo CSV
                                    with open('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\importado_nfe.csv', 'a', newline='') as csvfile:
                                        writer = csv.writer(
                                            csvfile, delimiter=',')
                                        writer.writerow(
                                            [numero, valor, Data, chave, pasta])
                                    # se nao for nfe nem cte passa para error
                                except:
                                    print("erro")
                except:
                    print("erro")
            with open('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\unidades.txt', 'a') as arquivo:
                arquivo.writelines(f'Fim: {agora}\n')


    
    ler_dist_imp()


def ler_dist_imp():
    agora = datetime.now()
    main_path = "R:\\02-importado\\"
    with open('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\unidades.txt', 'a') as arquivo:
        arquivo.writelines('Passando para importadoras')
    for root, subFolder, filename in os.walk(main_path):
        for t in subFolder:
            diretorio = ("R:\\02-importado\\%s") % (t)
            try:
                with open('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\unidades.txt', 'a') as arquivo:
                    arquivo.writelines(f'Inicio: {agora} lendo a empresa : {t}\n')
                    arquivo.writelines(f'Lido a unidade: {t}\n')
            except:
                pass
            # Obter a data atual
            data_atual = datetime.now()
            # Obter o ano atual
            ano_atual = data_atual.year
            # Criar um objeto de data para o início do ano atual
            inicio_do_ano_atual = datetime(ano_atual, 1, 1)
            # Percorre todos os arquivos do diretório
            for nome_arquivo in os.listdir(diretorio):
                try:
                    # Verifica se o arquivo é um arquivo XML
                    if nome_arquivo.endswith(".xml"):
                        # Obtém as informações de modificação do arquivo
                        caminho_completo = os.path.join(
                            diretorio, nome_arquivo)
                        data_modificacao = datetime.fromtimestamp(
                            os.path.getmtime(caminho_completo))
                        # Verifica se o arquivo foi modificado nos últimos 365 dias
                        if data_modificacao > inicio_do_ano_atual:
                            # Faz algo com o arquivo
                            arquivo = str(diretorio) + ("\\") + \
                                str(nome_arquivo)
                            xml_file = arquivo
                            tree = ET.parse(xml_file)
                            root = tree.getroot()
                            # Extrair o número e a chave do CTe

                            try:
                                ns = {'cte': 'http://www.portalfiscal.inf.br/cte'}

                                numero = root.find(
                                    './/cte:infCte/cte:ide/cte:nCT', ns).text
                                valor = root.find(
                                    './/cte:infCte/cte:vPrest/cte:vTPrest', ns).text
                                Data = root.find(
                                    './/cte:infCte/cte:ide/cte:dhEmi', ns).text
                                Data = F"{Data[8:10]}/{Data[5:7]}/{Data[:4]}"
                                chave = root.find(
                                    './/cte:infCte', ns).attrib['Id'][3:]
                                pasta = arquivo
                                # Escrever o número e a chave em um arquivo CSV
                                with open('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\importado_cte.csv', 'a', newline='') as csvfile:
                                    writer = csv.writer(csvfile, delimiter=',')
                                    writer.writerow(
                                        [numero, valor, Data, chave, pasta])
                            except:
                                print("Nota")
                                arquivo = str(diretorio) + ("\\") + \
                                    str(nome_arquivo)
                                xml_file = arquivo
                                tree = ET.parse(xml_file)
                                root = tree.getroot()
                                # Extrair o número e a chave do NFe
                                try:
                                    ns = {
                                        'nfe': 'http://www.portalfiscal.inf.br/nfe'}

                                    numero = root.find(
                                        './/nfe:NFe/nfe:infNFe/nfe:ide/nfe:nNF', ns).text
                                    valor = root.find(
                                        './/nfe:NFe/nfe:infNFe/nfe:total/nfe:ICMSTot/nfe:vNF', ns).text
                                    Data = root.find(
                                        './/nfe:NFe/nfe:infNFe/nfe:ide/nfe:dhEmi', ns).text
                                    Data = F"{Data[8:10]}/{Data[5:7]}/{Data[:4]}"
                                    chave = root.find(
                                        './/nfe:protNFe/nfe:infProt/nfe:chNFe', ns).text
                                    pasta = arquivo
                                    # Escrever os dados em um arquivo CSV
                                    with open('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\importado_nfe.csv', 'a', newline='') as csvfile:
                                        writer = csv.writer(
                                            csvfile, delimiter=',')
                                        writer.writerow(
                                            [numero, valor, Data, chave, pasta])
                                    # se nao for nfe nem cte passa para error
                                except:
                                    print("erro")
                except:
                    print("erro")
            with open('Y:\\Auditoria\\DADOS\\RELATORIO IMPORTADO\\unidades.txt', 'a') as arquivo:
                arquivo.writelines(f'Fim: {agora}\n')


if __name__ == '__main__':
    remover_csv()
