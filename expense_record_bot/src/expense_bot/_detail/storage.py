import json
import logging
from pathlib import Path
from typing import TypedDict

logger = logging.getLogger(__name__)
_DATA_DIRECTORY = Path("data")
_EXPENSES_FILE = _DATA_DIRECTORY / "expenses.json"


class Expense(TypedDict):
    """Data structure for a single expense.

    Attributes
    ----------
    id : int
        Unique number of record.
    amount : float
        Expense amount.
    category : str
        Expense category.
    description : str
        Short description.
    date : str
        Date the expense was added.
    """

    id: int
    amount: float
    category: str
    description: str
    date: str


def load_all_expenses() -> dict[str, list[Expense]]:
    """
    Loads all expenses from the shared JSON file.

    Returns
    -------
    dict[str, list[Expense]]
        Dictionary, where the key is a user’s Telegram ID (str), and the value is a list of its expenses.
    """
    if not _EXPENSES_FILE.exists():
        return {}
    try:
        with _EXPENSES_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        logger.error("Error reading JSON file.")
        return {}


def save_all_expenses(data: dict[str, list[Expense]]) -> None:
    """
    Saves the structure of all expenses in a JSON file.

    Parameters
    ----------
    data : dict[str, list[Expense]]
        Dictionary with all users expenses.
    """
    _DATA_DIRECTORY.mkdir(exist_ok=True)
    with _EXPENSES_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
