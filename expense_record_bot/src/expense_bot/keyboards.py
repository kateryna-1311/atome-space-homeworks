from telegram import KeyboardButton, ReplyKeyboardMarkup

MENU_ADD = "Додати витрату"
MENU_DELETE = "Видалити витрату"
MENU_LIST = "Список витрат"
MENU_STATS = "Статистика"
MENU_HELP = "Допомога"


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    """Create main bot menu in the reply-leyboard from.

    Returns
    -------
    ReplyKeyboardMarkup
        Telegram keyboard with action buttons.
    """
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton(MENU_ADD), KeyboardButton(MENU_DELETE)],
            [KeyboardButton(MENU_LIST), KeyboardButton(MENU_STATS)],
            [KeyboardButton(MENU_HELP)],
        ],
        resize_keyboard=True,
        one_time_keyboard=False,
    )
