#------------------------------------------------------
# Projeto Pokedex
# Gabriel Carvalho, Lucas Cupertino, Otávio Felipe
#------------------------------------------------------

import mysql.connector
import tkinter as tk
from tkinter import ttk

#------------------------------Conectando com BD-----------------------------
mydb = mysql.connector.connect( host = "localhost",
                                   user = "root",
                                   password = "password",
                                   database = "projeto")
cursor = mydb.cursor()

#------------------------------------ABAS------------------------------------
root = tk.Tk()
root_tabs = ttk.Notebook(root)
root.title("Projeto Pokédex")

tabParametros = ttk.Frame(root_tabs)
tabResultados = ttk.Frame(root_tabs)
root_tabs.add(tabParametros, text = "Parâmetros da pesquisa")
root_tabs.add(tabResultados, text = "Resultados da pesquisa")
root_tabs.pack()

#----------------------------------FRAMES-----------------------------------
frameNum = tk.LabelFrame(tabParametros, text="Escolha intervalo de id")
frameNum.grid(row=0, column=0)

frameTipos = tk.LabelFrame(tabParametros, text="Escolha tipos desejados")
frameTipos.grid(row=0, column=1)

frameFraqueza = tk.LabelFrame(tabParametros, text="Escolha fraquezas desejadas")
frameFraqueza.grid(row=0, column = 2)

frameTreinadores = tk.LabelFrame(tabParametros, text="Escolha um treinador se desejar")
frameTreinadores.grid(row=0, column = 3)

frameResultados = tk.LabelFrame(tabResultados, text = "Resultados da pesquisa")
frameResultados.grid(row = 1, column=0)

#---------------------------Variaveis Importantes---------------------------
listaLabels = []
menorNumero = tk.Entry(frameNum)
maiorNumero = tk.Entry(frameNum)
queroAgua = tk.BooleanVar()
queroDragao = tk.BooleanVar()
queroEletrico = tk.BooleanVar()
queroFada = tk.BooleanVar()
queroFantasma = tk.BooleanVar()
queroFogo = tk.BooleanVar()
queroGelo = tk.BooleanVar()
queroGrama = tk.BooleanVar()
queroInseto = tk.BooleanVar()
queroLutador = tk.BooleanVar()
queroMetal = tk.BooleanVar()
queroNormal = tk.BooleanVar()
queroPedra = tk.BooleanVar()
queroPsiquico = tk.BooleanVar()
queroVenenoso = tk.BooleanVar()
queroSombrio = tk.BooleanVar()
queroTerra = tk.BooleanVar()
queroVoador = tk.BooleanVar()
fraquezaAgua = tk.BooleanVar()
fraquezaDragao = tk.BooleanVar()
fraquezaEletrico = tk.BooleanVar()
fraquezaFada = tk.BooleanVar()
fraquezaFantasma = tk.BooleanVar()
fraquezaFogo = tk.BooleanVar()
fraquezaGelo = tk.BooleanVar()
fraquezaGrama = tk.BooleanVar()
fraquezaInseto = tk.BooleanVar()
fraquezaLutador = tk.BooleanVar()
fraquezaMetal = tk.BooleanVar()
fraquezaNormal = tk.BooleanVar()
fraquezaPedra = tk.BooleanVar()
fraquezaPsiquico = tk.BooleanVar()
fraquezaVenenoso = tk.BooleanVar()
fraquezaSombrio = tk.BooleanVar()
fraquezaTerra = tk.BooleanVar()
fraquezaVoador = tk.BooleanVar()
queroBrock = tk.BooleanVar()
queroMisty = tk.BooleanVar()
queroSurge = tk.BooleanVar()
queroErika = tk.BooleanVar()
queroKoga = tk.BooleanVar()
queroSabrina = tk.BooleanVar()
queroBlaine = tk.BooleanVar()
queroGiovanni = tk.BooleanVar()
queroLorelei = tk.BooleanVar()
queroBruno = tk.BooleanVar()
queroAgatha = tk.BooleanVar()
queroLance = tk.BooleanVar()
queroBlue = tk.BooleanVar()
queroTrace = tk.BooleanVar()

#----------------------------Funções Importantes----------------------------
def limparLabels():
    for label in listaLabels:
        label.config(text="")

def filtraPokemon():
    limparLabels()
    filtro1 = "WITH filtro1 AS( SELECT * FROM pokemon WHERE pokemon_id >= " + menorNumero.get() + "), "
    filtro2 = "filtro2 AS( SELECT * FROM filtro1 WHERE pokemon_id <= " + maiorNumero.get() + ")"
    filtroCounter = 2
    filtroTipos = ""
    #Filtrando tipos
    if(queroAgua.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='agua') "
    if(queroDragao.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='dragao') "
    if(queroEletrico.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='eletrico') "
    if(queroFada.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='fada') "
    if(queroFantasma.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='fantasma') "
    if(queroFogo.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='fogo') "
    if(queroGelo.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='gelo') "
    if(queroGrama.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='grama') "
    if(queroInseto.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='inseto') "
    if(queroLutador.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='lutador') "
    if(queroMetal.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='metal') "
    if(queroNormal.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='normal') "
    if(queroPedra.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='pedra') "
    if(queroPsiquico.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='psiquico') "
    if(queroVenenoso.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='venenoso') "
    if(queroSombrio.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='sombrio') "
    if(queroTerra.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='terra') "
    if(queroVoador.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, tem_tipo t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='voador') "
    #Filtrando fraquezas
    if(fraquezaAgua.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='agua') "
    if(fraquezaDragao.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='dragao') "
    if(fraquezaEletrico.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='eletrico') "
    if(fraquezaFada.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='fada') "
    if(fraquezaFantasma.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='fantasma') "
    if(fraquezaFogo.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='fogo') "
    if(fraquezaGelo.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='gelo') "
    if(fraquezaGrama.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='grama') "
    if(fraquezaInseto.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='inseto') "
    if(fraquezaLutador.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='lutador') "
    if(fraquezaMetal.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='metal') "
    if(fraquezaNormal.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='normal') "
    if(fraquezaPedra.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='pedra') "
    if(fraquezaPsiquico.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='psiquico') "
    if(fraquezaVenenoso.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='venenoso') "
    if(fraquezaSombrio.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='sombrio') "
    if(fraquezaTerra.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='terra') "
    if(fraquezaVoador.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, fraqueza t WHERE f.pokemon_id = t.pokemon_id AND t.tipo='voador') "
    if(queroBrock.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Brock')"
    if(queroMisty.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Misty')"
    if(queroSurge.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Lt. Surge')"
    if(queroErika.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Erika')"
    if(queroKoga.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Koga')"
    if(queroSabrina.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Sabrina')"
    if(queroBlaine.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Blaine')"
    if(queroGiovanni.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Giovanni')"
    if(queroLorelei.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Lorelei')"
    if(queroBruno.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Bruno')"
    if(queroAgatha.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Agatha')"
    if(queroLance.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Lance')"
    if(queroBlue.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Blue')"
    if(queroTrace.get()):
        filtroCounter += 1
        filtroTipos += ", filtro"+str(filtroCounter)+" AS( SELECT DISTINCT f.pokemon_id, f.nome, f.altura, f.peso FROM filtro"+str(filtroCounter-1)+ " f, colecao t WHERE f.pokemon_id = t.pokemon_id AND t.nome_treinador='Trace')"
    query = "SELECT * FROM filtro" + str(filtroCounter) + ";";
    comando = cursor.execute(filtro1 + filtro2 + filtroTipos + query);
    i=1
    for pokemon in cursor:
        #pokemon_id
        listaLabels.append(tk.Label(tabResultados, text=str(pokemon[0])))
        listaLabels[-1].grid(row=i, column=0)
        #nome
        listaLabels.append(tk.Label(tabResultados, text=str(pokemon[1])))
        listaLabels[-1].grid(row=i, column=1)
        #altura
        listaLabels.append(tk.Label(tabResultados, text=str(pokemon[2]) + "cm"))
        listaLabels[-1].grid(row=i, column=2)
        #peso
        listaLabels.append(tk.Label(tabResultados, text=str(pokemon[3]) + " gramas\t\t"))
        listaLabels[-1].grid(row=i, column=3)
        i += 1

#---------------tabParametros: selecionar parâmetros do filtro--------------
menorNumero.insert(0, 0)
menorNumero.grid(row=0,column=0)

maiorNumero.insert(0, 151)
maiorNumero.grid(row=1, column=0)

#------------------------------BOTOES TIPO----------------------------------
botaoAgua = tk.Checkbutton(frameTipos, text="Água", variable=queroAgua, onvalue=True, offvalue=False)
botaoAgua.grid(row=0, column=0)

botaoDragao = tk.Checkbutton(frameTipos, text="Dragão", variable=queroDragao, onvalue=True, offvalue=False)
botaoDragao.grid(row=1, column=0)

botaoEletrico = tk.Checkbutton(frameTipos, text="Elétrico", variable=queroEletrico, onvalue=True, offvalue=False)
botaoEletrico.grid(row=2, column=0)

botaoFada = tk.Checkbutton(frameTipos, text="Fada", variable=queroFada, onvalue=True, offvalue=False)
botaoFada.grid(row=3, column=0)

botaoFantasma = tk.Checkbutton(frameTipos, text="Fantasma", variable=queroFantasma, onvalue=True, offvalue=False)
botaoFantasma.grid(row=4, column=0)

botaoFogo = tk.Checkbutton(frameTipos, text="Fogo", variable=queroFogo, onvalue=True, offvalue=False)
botaoFogo.grid(row=5, column=0)

botaoGelo = tk.Checkbutton(frameTipos, text="Gelo", variable=queroGelo, onvalue=True, offvalue=False)
botaoGelo.grid(row=6, column=0)

botaoGrama = tk.Checkbutton(frameTipos, text="Grama", variable=queroGrama, onvalue=True, offvalue=False)
botaoGrama.grid(row=7, column=0)

botaoInseto = tk.Checkbutton(frameTipos, text="Inseto", variable=queroInseto, onvalue=True, offvalue=False)
botaoInseto.grid(row=8, column=0)

botaoLutador = tk.Checkbutton(frameTipos, text="Lutador", variable=queroLutador, onvalue=True, offvalue=False)
botaoLutador.grid(row=9, column=0)

botaoMetal = tk.Checkbutton(frameTipos, text="Metal", variable=queroMetal, onvalue=True, offvalue=False)
botaoMetal.grid(row=10, column=0)

botaoNormal = tk.Checkbutton(frameTipos, text="Normal", variable=queroNormal, onvalue=True, offvalue=False)
botaoNormal.grid(row=11, column=0)

botaoPedra = tk.Checkbutton(frameTipos, text="Pedra", variable=queroPedra, onvalue=True, offvalue=False)
botaoPedra.grid(row=12, column=0)

botaoPsiquico = tk.Checkbutton(frameTipos, text="Psíquico",variable=queroPsiquico, onvalue=True, offvalue=False)
botaoPsiquico.grid(row=13, column=0)

botaoVenenoso = tk.Checkbutton(frameTipos, text="Venenoso", variable=queroVenenoso, onvalue=True, offvalue=False)
botaoVenenoso.grid(row=14, column=0)

botaoSombrio = tk.Checkbutton(frameTipos, text="Sombrio", variable=queroSombrio, onvalue=True, offvalue=False)
botaoSombrio.grid(row=15, column=0)

botaoTerra = tk.Checkbutton(frameTipos, text="Terra",variable=queroTerra, onvalue=True, offvalue=False)
botaoTerra.grid(row=16, column=0)

botaoVoador = tk.Checkbutton(frameTipos, text="Voador", variable=queroVoador, onvalue=True, offvalue=False)
botaoVoador.grid(row=17, column=0)


#----------------------------BOTOES FRAQUEZA--------------------------------
botaoFraquezaAgua = tk.Checkbutton(frameFraqueza, text="Água", variable=fraquezaAgua, onvalue=True, offvalue=False)
botaoFraquezaAgua.grid(row=0, column=0)

botaoFraquezaDragao = tk.Checkbutton(frameFraqueza, text="Dragão", variable=fraquezaDragao, onvalue=True, offvalue=False)
botaoFraquezaDragao.grid(row=1, column=0)

botaoFraquezaEletrico = tk.Checkbutton(frameFraqueza, text="Elétrico", variable=fraquezaEletrico, onvalue=True, offvalue=False)
botaoFraquezaEletrico.grid(row=2, column=0)

botaoFraquezaFada = tk.Checkbutton(frameFraqueza, text="Fada", variable=fraquezaFada, onvalue=True, offvalue=False)
botaoFraquezaFada.grid(row=3, column=0)

botaoFraquezaFantasma = tk.Checkbutton(frameFraqueza, text="Fantasma", variable=fraquezaFantasma, onvalue=True, offvalue=False)
botaoFraquezaFantasma.grid(row=4, column=0)

botaoFraquezaFogo = tk.Checkbutton(frameFraqueza, text="Fogo", variable=fraquezaFogo, onvalue=True, offvalue=False)
botaoFraquezaFogo.grid(row=5, column=0)

botaoFraquezaGelo = tk.Checkbutton(frameFraqueza, text="Gelo", variable=fraquezaGelo, onvalue=True, offvalue=False)
botaoFraquezaGelo.grid(row=6, column=0)

botaoFraquezaGrama = tk.Checkbutton(frameFraqueza, text="Grama", variable=fraquezaGrama, onvalue=True, offvalue=False)
botaoFraquezaGrama.grid(row=7, column=0)

botaoFraquezaInseto = tk.Checkbutton(frameFraqueza, text="Inseto", variable=fraquezaInseto, onvalue=True, offvalue=False)
botaoFraquezaInseto.grid(row=8, column=0)

botaoFraquezaLutador = tk.Checkbutton(frameFraqueza, text="Lutador", variable=fraquezaLutador, onvalue=True, offvalue=False)
botaoFraquezaLutador.grid(row=9, column=0)

botaoFraquezaMetal = tk.Checkbutton(frameFraqueza, text="Metal", variable=fraquezaMetal, onvalue=True, offvalue=False)
botaoFraquezaMetal.grid(row=10, column=0)

botaoFraquezaNormal = tk.Checkbutton(frameFraqueza, text="Normal", variable=fraquezaNormal, onvalue=True, offvalue=False)
botaoFraquezaNormal.grid(row=11, column=0)

botaoFraquezaPedra = tk.Checkbutton(frameFraqueza, text="Pedra", variable=fraquezaPedra, onvalue=True, offvalue=False)
botaoFraquezaPedra.grid(row=12, column=0)

botaoFraquezaPsiquico = tk.Checkbutton(frameFraqueza, text="Psíquico", variable=fraquezaPsiquico, onvalue=True, offvalue=False)
botaoFraquezaPsiquico.grid(row=13, column=0)

botaoFraquezaVenenoso = tk.Checkbutton(frameFraqueza, text="Venenoso", variable=fraquezaVenenoso, onvalue=True, offvalue=False)
botaoFraquezaVenenoso.grid(row=14, column=0)

botaoFraquezaSombrio = tk.Checkbutton(frameFraqueza, text="Sombrio", variable=fraquezaSombrio, onvalue=True, offvalue=False)
botaoFraquezaSombrio.grid(row=15, column=0)

botaoFraquezaTerra = tk.Checkbutton(frameFraqueza, text="Terra", variable=fraquezaTerra, onvalue=True, offvalue=False)
botaoFraquezaTerra.grid(row=16, column=0)

botaoFraquezaVoador = tk.Checkbutton(frameFraqueza, text="Voador", variable=fraquezaVoador, onvalue=True, offvalue=False)
botaoFraquezaVoador.grid(row=17, column=0)

#---------------------------BOTOES TREINADOR--------------------------------

botaoBrock = tk.Checkbutton(frameTreinadores, text="Brock", variable=queroBrock, onvalue=True, offvalue=False)
botaoBrock.grid(row=0, column=0)

botaoMisty = tk.Checkbutton(frameTreinadores, text="Misty", variable=queroMisty, onvalue=True, offvalue=False)
botaoMisty.grid(row=1, column=0)

botaoSurge = tk.Checkbutton(frameTreinadores, text="Lt. Surge", variable=queroSurge, onvalue=True, offvalue=False)
botaoSurge.grid(row=2, column=0)

botaoErika = tk.Checkbutton(frameTreinadores, text="Erika", variable=queroErika, onvalue=True, offvalue=False)
botaoErika.grid(row=3, column=0)

botaoKoga = tk.Checkbutton(frameTreinadores, text="Koga", variable=queroKoga, onvalue=True, offvalue=False)
botaoKoga.grid(row=4, column=0)

botaoSabrina = tk.Checkbutton(frameTreinadores, text="Sabrina", variable=queroSabrina, onvalue=True, offvalue=False)
botaoSabrina.grid(row=5, column=0)

botaoBlaine = tk.Checkbutton(frameTreinadores, text="Blaine", variable=queroBlaine, onvalue=True, offvalue=False)
botaoBlaine.grid(row=6, column=0)

botaoGiovanni = tk.Checkbutton(frameTreinadores, text="Giovanni", variable=queroGiovanni, onvalue=True, offvalue=False)
botaoGiovanni.grid(row=7, column=0)

botaoLorelei = tk.Checkbutton(frameTreinadores, text="Lorelei", variable=queroLorelei, onvalue=True, offvalue=False)
botaoLorelei.grid(row=8, column=0)

botaoBruno = tk.Checkbutton(frameTreinadores, text="Bruno", variable=queroBruno, onvalue=True, offvalue=False)
botaoBruno.grid(row=9, column=0)

botaoAgatha = tk.Checkbutton(frameTreinadores, text="Agatha", variable=queroAgatha, onvalue=True, offvalue=False)
botaoAgatha.grid(row=10, column=0)

botaoLance = tk.Checkbutton(frameTreinadores, text="Lance", variable=queroLance, onvalue=True, offvalue=False)
botaoLance.grid(row=11, column=0)

botaoBlue = tk.Checkbutton(frameTreinadores, text="Blue", variable=queroBlue, onvalue=True, offvalue=False)
botaoBlue.grid(row=12, column=0)

botaoTrace = tk.Checkbutton(frameTreinadores, text="Trace", variable=queroTrace, onvalue=True, offvalue=False)
botaoTrace.grid(row=13, column=0)

#----------------tabResultados: exibir resultados da pesquisa---------------

botao = tk.Button(tabResultados, text = "Calcular resultado da pesquisa", command=filtraPokemon)
botao.grid(row = 0, column = 0)


root.mainloop()
mydb.close()
