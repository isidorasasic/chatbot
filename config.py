import argparse

def parse_args():

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
