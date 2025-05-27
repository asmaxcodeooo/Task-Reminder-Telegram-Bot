import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('7297745936:AAF8_k7pzXZS9_0xXRv9YL5hBE93bf01mPw')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your reminder bot. Use /remind <minutes> <task> to set a reminder.")

async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        minutes = int(context.args[0])
        task = ' '.join(context.args[1:])
        await update.message.reply_text(f"Reminder set: I'll remind you in {minutes} minutes to {task}")
    except (IndexError, ValueError):
        await update.message.reply_text("Usage: /remind <minutes> <task>")
# 2. Reminder function
async def send_reminder(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=context.job.chat_id,
        text=f"🔔 REMINDER: {context.job.data}"
    )
def main():
    app = Application.builder().token('7297745936:AAF8_k7pzXZS9_0xXRv9YL5hBE93bf01mPw').build()
    
    # Register commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("remind", remind))
    app.add_handler(CommandHandler("add", remind))  # Alias for /remind
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()