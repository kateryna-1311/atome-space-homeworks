import logging
from datetime import datetime

from expense_bot._detail.storage import Expense, load_all_expenses, save_all_expenses

logger = logging.getLogger(__name__)


def get_expenses(user_id: str) -> list[Expense]:
    """
    Gets a list of expenses for a particular user by their Telegram ID.

    Parametrs
    ---------
    user_id : str
        User`s Telegram ID

    Returns
    -------
    list[Expense]
        Returns list of user`s expenses, empty if not expense.
    """
    all_data = load_all_expenses()
    return all_data.get(user_id, [])


def add_expense(user_id: str, amount: float, category: str, description: str) -> int:
    """
    Adds a new expense to the user.

    Parametrs
    ---------
    user_id : str
        User`s Telegram ID.
    amount : float
        Amount of expenses.
    category : str
        Category of expenses.
    descriptions : str
        Short description of expense.

    Reterns
    -------
    int
        Number of new expense
    """
    all_data = load_all_expenses()
    if user_id not in all_data:
        all_data[user_id] = []
    user_expenses = all_data[user_id]
    new_id = len(user_expenses) + 1
    new_expense: Expense = {
        "id": new_id,
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    user_expenses.append(new_expense)
    all_data[user_id] = user_expenses
    save_all_expenses(all_data)
    logger.info("Expense saved for user %s", user_id)
    return new_id


def delete_expense(user_id: str, expense_id: int) -> bool:
    """Removes the user’s expense by ID.

    Parameters
    ----------
    user_id : str
        User`s Telegram ID.
    expense_id : int
        The number of the expense to delete.

    Returns
    -------
    bool
        True if successfully deleted. False if expense not found.
    """
    all_data = load_all_expenses()
    if user_id not in all_data:
        return False
    user_expenses = all_data[user_id]
    for index, expense in enumerate(user_expenses):
        if expense["id"] == expense_id:
            user_expenses.pop(index)
            for i, exp in enumerate(user_expenses):
                exp["id"] = i + 1
            all_data[user_id] = user_expenses
            save_all_expenses(all_data)
            logger.info("Expense %d deleted for user %s", expense_id, user_id)
            return True
    return False
