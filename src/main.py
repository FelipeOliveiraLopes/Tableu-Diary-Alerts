import os
import requests
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações de e-mail
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

def fetch_tableau_data():
    """Extrai dados do dashboard do Tableau."""
    # Exemplo de chamada para uma API fictícia do Tableau
    url = "https://api.tableau.com/v1/data"
    headers = {"Authorization": f"Bearer {os.getenv('TABLEAU_API_KEY')}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Erro ao conectar com Tableau: {response.status_code}")

def process_data(data):
    """Processa os dados extraídos."""
    # Exemplo de processamento de dados
    processed_data = data.groupby("categoria").agg({"valor": "sum"})
    return processed_data

def send_email(summary):
    """Envia um e-mail com o resumo dos dados."""
    # Configuração do e-mail
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = "Relatório Diário de Dados - Tableau"

    # Corpo do e-mail
    body = f"Prezado,\n\nSegue o resumo dos dados do dia:\n\n{summary.to_string(index=False)}\n\nAtenciosamente,\nEquipe de Dados"
    msg.attach(MIMEText(body, "plain"))

    # Envio do e-mail
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)

def main():
    """Função principal que coordena o fluxo de execução."""
    print("Iniciando extração de dados do Tableau...")
    data = fetch_tableau_data()

    print("Processando dados...")
    summary = process_data(data)

    print("Enviando e-mail com o resumo...")
    send_email(summary)
    print("E-mail enviado com sucesso!")

if __name__ == "__main__":
    main()