from expense_bot.expenses import add_expense, delete_expense, get_expenses
from expense_bot.keyboards import MENU_ADD, MENU_DELETE, MENU_HELP, MENU_LIST, MENU_STATS, main_menu_keyboard
from telegram import Update
from telegram.ext import ContextTypes

_HELP_TEXT = (
    "📋 **Команди бота:**\n\n"
    "/add <сума> <категорія> <опис> — додати нову витрату\n"
    "/list — показати список витрат\n"
    "/stats — показати статистику витрат\n"
    "/delete <номер> — видалити витрату за номером\n"
    "/help — показати це повідомлення"
)


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Processes the /start command and displays the main menu.

    Parameters
    ----------
    update : Update
        Data regarding the message and the user.
    context : ContextTypes.DEFAULT_TYPE
        Interaction with the bot.
    """
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"Привіт, {user_name}!\n\n"
        "Я допоможу тобі вести облік особистих витрат. \n\n" + _HELP_TEXT,
        reply_markup=main_menu_keyboard(),
    )


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle the /help command

    Parameters
    ----------
    update : Update
        Data regarding the message and the user.
    context : ContextTypes.DEFAULT_TYPE
        The execution context object.
    """
    await update.message.reply_text(_HELP_TEXT)


async def cmd_add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /add <сума> <категорія> <опис> command.

    Parameters
    ----------
    update : Update
        The incoming Telegram update object.
    context : ContextTypes.DEFAULT_TYPE
        Object containing the arguments list in `context.args`.
    """
    if not context.args or len(context.args) < 2:
        await update.message.reply_text(
            "Вкажіть параметри: /add <сума> <категорія> [опис]\n"
            "Приклад: `/add 150.50 Їжа Обід у кафе`",
            parse_mode="Markdown",  # форматирование текста
        )
        return
    try:
        amount = float(context.args[0])
        category = context.args[1]
        description = " ".join(context.args[2:]) if len(context.args) > 2 else "-"
        user_id = str(update.effective_user.id)
        expense_id = add_expense(user_id, amount, category, description)
        await update.message.reply_text(
            f"Витрату №{expense_id} додано!\n"
            f"Сума: {amount} грн\n"
            f"Категорія: {category}\n"
            f"Опис: {description}"
        )
    except ValueError:
        await update.message.reply_text("Некоректна сума! Будь ласка, вкажіть число.")


async def cmd_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /list command and display a formatted list of all user expenses.

    Parameters
    ----------
    update : Update
        The incoming Telegram update object.
    context : ContextTypes.DEFAULT_TYPE
        The execution context object.
    """
    user_id = str(update.effective_user.id)
    user_expenses = get_expenses(user_id)
    if not user_expenses:
        await update.message.reply_text("Ваш список витрат порожній.")
        return
    response = "**Ваші витрати:**\n\n"
    for exp in user_expenses:
        response += (
            f"**{exp['id']}.** {exp['amount']} грн — {exp['category']} "
            f"({exp['description']}) | _{exp['date']}_\n"
        )
    await update.message.reply_text(response, parse_mode="Markdown")


async def cmd_delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /delete command to remove.

    Parameters
    ----------
    update : Update
        The incoming Telegram update object.
    context : ContextTypes.DEFAULT_TYPE
       Object containing the target entry index in `context.args`.
    """
    if not context.args:
        await update.message.reply_text(
            "Вкажіть номер запису для видалення. Приклад: `/delete 2`",
            parse_mode="Markdown",
        )
        return
    try:
        expense_id = int(context.args[0])
        user_id = str(update.effective_user.id)
        success = delete_expense(user_id, expense_id)
        if success:
            await update.message.reply_text(f"Витрату №{expense_id} успішно видалено.")
        else:
            await update.message.reply_text(
                f"Витрату з номером {expense_id} не знайдено."
            )
    except ValueError:
        await update.message.reply_text("Номер запису має бути цілим числом!")


async def cmd_stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /stats command, calculate total expenditure, and aggregate by category.

    Parameters
    ----------
    update : Update
        The incoming Telegram update object.
    context : ContextTypes.DEFAULT_TYPE
        The execution context object.
    """
    user_id = str(update.effective_user.id)
    user_expenses = get_expenses(user_id)
    if not user_expenses:
        await update.message.reply_text(
            "Немає даних для статистики. Список витрат порожній."
        )
        return
    total_sum = sum(exp["amount"] for exp in user_expenses)
    category_totals: dict[str, float] = {}
    for exp in user_expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0.0) + exp["amount"]
    response = "**Статистика витрат:**\n\n"
    response += f"**Загальна сума:** {total_sum:.2f} грн\n"  # округление до двух чисел после запятой
    response += "──────────────────\n"
    response += "**По категоріях:**\n"
    for category, sum_amount in category_totals.items():
        response += f"• {category}: {sum_amount:.2f} грн\n"
    await update.message.reply_text(response, parse_mode="Markdown")


async def on_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle interactions with the text buttons of the main Reply-keyboard.

    Parameters
    ----------
    update : Update
        The incoming Telegram update object containing the pressed button text.
    context : ContextTypes.DEFAULT_TYPE
        The execution context object.
    """
    text = update.message.text
    if text == MENU_ADD:
        await update.message.reply_text(
            "Щоб додати витрату, введіть команду у форматі:\n"
            "`/add <сума> <категорія> <опис>`\n\n"
            "Наприклад: `/add 250.00 Транспорт Таксі`",
            parse_mode="Markdown",
        )
    elif text == MENU_DELETE:
        await update.message.reply_text(
            "Щоб видалити витрату, введіть її номер після команди `/delete`.\n"
            "Наприклад: `/delete 1`",
            parse_mode="Markdown",
        )
    elif text == MENU_LIST:
        await cmd_list(update, context)
    elif text == MENU_STATS:
        await cmd_stats(update, context)
    elif text == MENU_HELP:
        await cmd_help(update, context)
    else:
        await update.message.reply_text(
            "Невідома команда. Будь ласка, використовуйте кнопки меню або /help."
        )
