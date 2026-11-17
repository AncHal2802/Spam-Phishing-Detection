import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from src.pipeline import analyze_message

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Replace with your actual token from BotFather
TOKEN = "8642994825:AAG0GyInYjQvSZxkjRO5dTkFTyV2rnUfKEU"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if not text:
        return

    # Run your two-stage pipeline
    r = analyze_message(text)

    # Format the response
    response = (
        f"🛡️ *Analysis Results*\n\n"
        f"• *Spam Probability:* `{r['spam_prob']:.1%}`\n"
        f"• *Verdict:* *{r['verdict']}*\n"
    )

    if r["urls"]:
        response += "\n🔗 *Detected Links:*\n"
        for u in r["urls"]:
            response += f"• `{u['url']}`\n  Phishing Prob: **{u['phishing_prob']:.1%}**\n"
    else:
        response += "\nℹ️ *No web URLs detected.*"

    await update.message.reply_text(response, parse_mode="Markdown")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).connect_timeout(30).read_timeout(30).write_timeout(30).build()
    
    # Listen to any text message sent to the bot
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("🤖 Telegram Bot is running... Press Ctrl+C to stop.")
    app.run_polling()