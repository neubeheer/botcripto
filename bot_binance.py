import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 🔹 Configuração do Google Sheets
SHEET_NAME = "Crypto Bot"
WORKSHEET_NAME = "Sheet1"
JSON_CREDENTIALS_FILE = "credenciais.json"

# 🔹 Binance API URL
BINANCE_URL = "https://api.binance.com/api/v3/ticker/price?symbol="

# 🔹 Lista de criptos para monitorar
CRIPTO_LIST = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]

# 🔹 Conectar ao Google Sheets
def conectar_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_CREDENTIALS_FILE, scope)
    client = gspread.authorize(creds)
    return client.open(SHEET_NAME).worksheet(WORKSHEET_NAME)

# 🔹 Obter preço da Binance
def obter_preco(moeda):
    response = requests.get(BINANCE_URL + moeda).json()
    return response["price"]

# 🔹 Atualizar Google Sheets
def atualizar_planilha():
    sheet = conectar_sheets()
    for i, cripto in enumerate(CRIPTO_LIST):
        preco = obter_preco(cripto)
        sheet.update_cell(i + 2, 2, preco)  # Atualiza coluna B

if __name__ == "__main__":
    atualizar_planilha()
    print("✅ Preços atualizados com sucesso!")
