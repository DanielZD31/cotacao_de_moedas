import requests
import tkinter as tk
from tkinter import ttk

#Função da API de Cotação de Moedas

def obter_cotacoes():
    link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    resposta = requests.get(link)
    return resposta.json()

def mostrar_cotacao():
    moeda = combo_moeda.get()
    cotacoes = obter_cotacoes()
    
    if moeda == "USD":
        resultado.set(f"Cotação do USD/BRL: {cotacoes['USDBRL']['bid']}")
    elif moeda == "EUR":
        resultado.set(f"Cotação do EUR/BRL: {cotacoes['EURBRL']['bid']}")
    elif moeda == "BTC":
        resultado.set(f"Cotação do BTC/BRL: {cotacoes['BTCBRL']['bid']}")
    else:
        resultado.set("Moeda não suportada.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Cotação de Moedas")

ttk.Label(root, text="Escolha a moeda:").pack(padx=10, pady=5)
combo_moeda = ttk.Combobox(root, values=["USD", "EUR", "BTC"])
combo_moeda.pack(padx=10, pady=5)
combo_moeda.set("USD")  

ttk.Button(root, text="Consultar", command=mostrar_cotacao).pack(padx=10, pady=5)

resultado = tk.StringVar()
ttk.Label(root, textvariable=resultado).pack(padx=10, pady=5)

root.mainloop()
