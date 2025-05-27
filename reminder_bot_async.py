# reminder_bot_async.py

import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        minutes = int(context.args[0])
        task = ' '.join(context.args[1:])

        print(f"Received reminder request: {minutes} min - {task}")
        await update.message.reply_text(
            f"Reminder set: I'll remind you in {minutes} minute(s) to {task}"
        )

        await asyncio.sleep(minutes * 60)
        print("Reached reminder send block")

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"⏰ Reminder: {task}"
        )

    except (IndexError, ValueError) as e:
        print(f"Error parsing command: {e}")  # Debug line
        await update.message.reply_text("Usage: /remind <minutes> <task>")

if __name__ == "__main__":
    print("Bot is starting...")  # Debug line
    app = ApplicationBuilder().token("7297745936:AAF8_k7pzXZS9_0xXRv9YL5hBE93bf01mPw").build()
    app.add_handler(CommandHandler("remind", remind))
    print("Bot is polling...")  # Debug line
    app.run_polling()
