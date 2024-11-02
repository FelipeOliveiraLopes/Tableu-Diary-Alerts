# Tableau Daily Alerts

Este projeto automatiza o envio de alertas diários com dados extraídos de um dashboard do Tableau. O script em Python acessa o Tableau, extrai dados de D-1, processa-os e envia um resumo por e-mail.

## Funcionalidades

- Conexão automática com o Tableau para extração de dados
- Processamento e análise de dados com `pandas`
- Envio de e-mails automatizado usando `smtplib`

## Como Configurar e Executar

1. Instale as dependências usando:
   ```bash
   pip install -r requirements.txt