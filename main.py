from config import parse_args
from chat_app import ChatbotApp
from dotenv import load_dotenv

from tools import get_current_date


# load .env into environment variables
load_dotenv()


def main():
    parsed_args = parse_args()
    ChatbotApp(parsed_args).run()


if __name__ == "__main__":
    main()