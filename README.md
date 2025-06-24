# 📊 Algo-Trading System with ML & Automation

This is a Python-based mini algorithmic trading system that:
- Fetches stock data via Yahoo Finance
- Applies a combined RSI + Moving Average crossover strategy
- Logs trades & metrics to Google Sheets
- Uses a Decision Tree ML model for price direction prediction
- Sends real-time alerts to Telegram

---

## 🚀 Features

| Feature                                | Status |
|----------------------------------------|--------|
| Fetch stock data (Yahoo Finance)       | ✅      |
| RSI < 30 + 20DMA > 50DMA strategy      | ✅      |
| 6-month backtest                       | ✅      |
| Decision Tree model on RSI, MACD, Volume | ✅   |
| Prediction accuracy logged             | ✅      |
| Log trades to Google Sheets            | ✅      |
| Portfolio P&L & summary tabs           | ✅      |
| 📢 Telegram alerts for signals/errors  | ✅      |
| Modular Python code                    | ✅      |

---
## ⚙️ Setup Instructions

1. **Clone repo / unzip**
   
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Google Sheets Setup**

   - Create Google Sheet: Algo_Trade_Log
   - Add worksheet: Trade_Log
   - Share it with your service account email (from creds.json)
     
4. **Telegram Setup**
   - Talk to @BotFather to create a bot → get token
     
   - Message your bot →
     run:
     https://api.telegram.org/your-bot-token/getUpdates
     
   - Copy "chat": { "id": 123456789 } as your TELEGRAM_CHAT_ID
     
   - Update config.py:
     
     TELEGRAM_BOT_TOKEN = "your-bot-token"
     TELEGRAM_CHAT_ID = "your-chat-id"
     
5. **Run the bot**
   ```bash
   python main.py
   ```

---

## 📬 Output Samples

Google Sheet gets:

['Buy', '2025-06-24', 2600.15]
['Sell', '2025-06-27', 2705.20]

Telegram gets:

Signal: Buy | RELIANCE.NS | Date: 2025-06-24 | Price: 2600.15  
RELIANCE.NS Model Accuracy: 0.45

---

## 🧠 Tech Stack

- Python, Pandas, scikit-learn
- gspread, oauth2client
- Yahoo Finance API (via yfinance)
- Telegram Bot API

---

## 👩‍💻 Author

**Thasniem Fathima J**  
🌐 GitHub: [Thasniem](https://github.com/Thasniem)  
💼 LinkedIn: [Thasniem Fathima J](https://www.linkedin.com/in/thasniem-fathima-engineering-student)

---

## 📦 Optional Enhancements

- ✅ Cron job for daily execution
- 📈 Plot backtest results
- 📊 Portfolio analytics dashboard
- 🔒 .env secrets loader

---

## ✅ License

MIT — feel free to use, modify, and share!
