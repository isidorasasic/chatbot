from helpers import load_prompt

SUMMARY_KEYWORDS = [
    "summarize",
    "summary",
    "summarization"
    "sum up",
    "recap",
    "tl;dr",
    "what did we talk about",
    "catch me up"
]


def is_summary(text: str) -> bool:
    """
    Determine whether the given text appears to be request for a summary
    by checking for the presence of any predefined summary-related keywords.

    Args:
        text (str): The text to inspect.

    Returns:
        True if at least one keyword from SUMMARY_KEYWORDS is present in the text;
        otherwise, False.
    """
    return any(key in text.lower() for key in SUMMARY_KEYWORDS)


def build_summary_request(conversation: list[dict]) -> list[dict]:
    """
    Build summary request by appending the summary prompt to the existing conversation.

    Args:
        conversation (list[dict]): The existing conversation represented as a list of message
            dictionaries

    Returns:
        A new list containing all items from conversation plus one additional
        user message with the summary prompt.
    """
    return conversation + [
        {
            "role": "user",
            "content": [{
                "type": "input_text",
                "text": (
                    load_prompt("summary_prompt.md")
                )
            }]
        }
    ]