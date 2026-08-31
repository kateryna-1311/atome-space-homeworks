import logging
import os

from dotenv import load_dotenv
from expense_bot import handlers
from telegram.ext import Application, CommandHandler, MessageHandler, filters

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Initialize configurations, register handlers, and start the Telegram bot.

    Raises
    ------
    ValueError
        If the `BOT_TOKEN` environment variable is missing or empty.
    """
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("`BOT_TOKEN` is not set in environment variables.")
    application = Application.builder().token(bot_token).build()
    application.add_handler(CommandHandler("start", handlers.cmd_start))
    application.add_handler(CommandHandler("help", handlers.cmd_help))
    application.add_handler(CommandHandler("add", handlers.cmd_add))
    application.add_handler(CommandHandler("list", handlers.cmd_list))
    application.add_handler(CommandHandler("delete", handlers.cmd_delete))
    application.add_handler(CommandHandler("stats", handlers.cmd_stats))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.on_text_message)
    )
    logger.info("Bot has started successfully")
    application.run_polling()


main()
