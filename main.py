import ccxt
import requests

# Configura le chiavi API
api_key = 'TUA_API_KEY'
api_secret = 'TUA_API_SECRET'
exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
})

# Configura le informazioni del bot Telegram
telegram_token = 'IL_TUO_TOKEN_TELEGRAM'
chat_id = 'IL_TUO_CHAT_ID'

# Funzione per ottenere il prezzo attuale di Bitcoin
def get_bitcoin_price():
    ticker = exchange.fetch_ticker('BTC/USDT')
    return ticker['ask']

# Funzione per inviare notifiche via Telegram
def send_telegram_notification(message):
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message}
    requests.post(url, json=params)

# Funzione principale del bot
def main():
    bitcoin_price = get_bitcoin_price()
    message = f'Prezzo attuale di Bitcoin: ${bitcoin_price}'
    send_telegram_notification(message)

if __name__ == "__main__":
    main()
