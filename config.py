import argparse

def parse_args():
    """
    Build and parse command-line arguments for the console chatbot.

    Parsed arguments:
        - model (str): The model name to use (for example, "gpt-4.1").
        - temperature (float): Sampling temperature for generation.
        - enable_tools (bool): Boolean flag controlling whether tool calls are enabled.
        - system_prompt (str): A system message used to initialize the conversation memory.

    Returns
        - argparse.Namespace with above mentioned attributes.
    """

    parser = argparse.ArgumentParser(description="console chatbot")
    parser.add_argument("--model", default="l2-gpt-4.1")
    parser.add_argument("--temperature", type=float, default=1)
    parser.add_argument("--enable-tools", default=True)
    parser.add_argument(
        "--system-prompt",
        default=(
            "You are a helpful assistant who maintains a consistent, "
            "professional tone."
        )
    )

    return parser.parse_args()
