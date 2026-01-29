import json
from datetime import datetime, timedelta


def get_current_date() -> str:
    """
    Return the current local system date in ISO format.

    Returns
        - str: Current date as an ISO-formatted string.
    """
    return datetime.now().date().isoformat()


def add_days_to_date(date: str, days: int) -> str:
    """
    Add/substract the number of days from the date.

    Args
        - date (str): Date to add/substract days from.
        - days (int): Number of days to add to date.

    Returns
        - str: New date
    """
    base_date = datetime.strptime(date, "%Y-%m-%d").date()
    return (base_date + timedelta(days=days)).isoformat()


TOOLS = [
    {
        "type": "function",
        "name": "get_current_date",
        "description": "Returns the current system date.",
        "parameters": {
            "type": "object",
            "properties": {}
        },
    },
    {
        "type": "function",
        "name": "add_days_to_date",
        "description": "Adds or subtracts days from a given date.",
        "parameters": {
            "type": "object",
            "properties": {
                "date": {"type": "string"},
                "days": {"type": "integer"},
            },
            "required": ["date", "days"],
        },
    },
]


def use_tool(tool_call):
    """
    Logic for choosing the tool to be used.
    
    Args:
        - tool_call: Tool call object returned from LLM response

    Returns:
        - str: get_current_date or add_days_to_date function output depending on the input parameter
    """
    if tool_call.name == "get_current_date":
        return get_current_date()
    if tool_call.name == "add_days_to_date":
        args = json.loads(tool_call.arguments)
        return add_days_to_date(args["date"], args["days"])
