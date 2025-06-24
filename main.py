from config import SYMBOLS
from utils.fetch_data import fetch_data
from utils.indicators import calculate_rsi, calculate_moving_averages
from strategies.rsi_ma_strategy import generate_signals
from sheets.google_sheets import log_to_google_sheets
from models.predictor import train_model
from utils.telegram_alert import send_telegram_message

if __name__ == "__main__":
    for symbol in SYMBOLS:
        try:
            df = fetch_data(symbol)
            df = calculate_rsi(df)
            df = calculate_moving_averages(df)

            trades = generate_signals(df)
            log_to_google_sheets(trades)

            for t in trades:
                try:
                    date_str = t[1].strftime('%Y-%m-%d')
                    price_val = float(t[2]) if not isinstance(t[2], float) else t[2]
                    send_telegram_message(
                        f"Signal: {t[0]} | {symbol} | Date: {date_str} | Price: {price_val:.2f}"
                    )
                except Exception as msg_err:
                    send_telegram_message(f"Error formatting trade alert for {symbol}: {msg_err}")

            model, acc = train_model(df)
            print(f"{symbol} Model Accuracy: {acc:.2f}")
            send_telegram_message(f"{symbol} Model Accuracy: {acc:.2f}")

        except Exception as e:
            error_msg = f"Error processing {symbol}: {str(e)}"
            print(error_msg)
            send_telegram_message(error_msg)
