## Descrição do Código💹💰

Este código cria uma aplicação gráfica simples em Python que consulta e exibe as cotações de moedas utilizando a API `awesomeapi`. A interface é construída com a biblioteca Tkinter.

### Funcionalidades

- **Consulta de Cotações de Moedas:** Permite ao usuário consultar a cotação das seguintes moedas em relação ao Real Brasileiro (BRL): Dólar (USD), Euro (EUR) e Bitcoin (BTC).
- **Interface Gráfica:** Desenvolvida com Tkinter, inclui um rótulo, uma caixa de seleção (Combobox) para escolher a moeda e um botão para realizar a consulta.

### Como Funciona

1. **Função `obter_cotacoes()`:** Faz uma requisição HTTP à API de cotações e retorna os dados em formato JSON.
2. **Função `mostrar_cotacao()`:** Obtém a moeda selecionada pelo usuário e atualiza o rótulo na interface gráfica com a cotação correspondente. Se a moeda não estiver na lista, exibe uma mensagem de "Moeda não suportada".
3. **Configuração da Interface:**
   - **Janela Principal:** Configurada com o título "Cotação de Moedas".
   - **Caixa de Seleção:** Permite ao usuário escolher entre USD, EUR e BTC, com USD como valor padrão.
   - **Botão de Consulta:** Aciona a função `mostrar_cotacao()` quando clicado, atualizando a cotação exibida.
   - **Rótulo de Resultado:** Exibe a cotação atual ou uma mensagem de erro, dependendo da moeda selecionada.

### Execução

A aplicação é executada com o comando `root.mainloop()`, que mantém a janela aberta e interativa até que o usuário a feche.
