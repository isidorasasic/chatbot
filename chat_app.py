from openai import OpenAI
import os
from memory import ConversationMemory
from tools import TOOLS, use_tool
from summarization import is_summary, build_summary_request


class ChatbotApp:
    """
    Console-based chat application that wraps the OpenAI Responses API, 
    maintains conversational memory, and optionally executes tool calls returned by the model.

    Args
    - config: An object containing parsed arguments.
    """
    def __init__(self, config):

        # Create OpenAI chat client for interaction with models
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
            base_url=os.environ.get("BASE_URL")
        )

        self.model = config.model
        self.temperature = config.temperature
        self.enable_tools = config.enable_tools
        self.memory = ConversationMemory(config.system_prompt.format(
            date_tools_status="ENABLED" if config.enable_tools else "DISABLED"
        ))

    def run(self):
        print("Chatbot started. Type 'exit' to quit.\n")

        while True:
            user_input = input("User: ").strip()
            if user_input.lower() == "exit":
                break

            self.memory.add_user(user_input)

            # check if user asks for conversation summary
            if is_summary(user_input):
                print("\nEntered summary mode\n")
                input_text = build_summary_request(self.memory.all())
                tools = None
            else:
                input_text=self.memory.all()
                tools=TOOLS if self.enable_tools else None

            response = self.client.responses.create(
                model=self.model,
                temperature=self.temperature,
                input=input_text,
                tools=tools
            )

            # debug
            # print(self.memory.all())

            # Check for tool calls
            tool_call = next(
                (item for item in response.output if item.type == "function_call"),
                None
            )

            while tool_call:
                self.memory.add_response_tool(response)
                tool_result = use_tool(tool_call)
                self.memory.add_tool_output(
                    tool_call_id=tool_call.call_id,
                    content=tool_result,
                )

                # DEBUG
                # print(self.memory.all())

                response = self.client.responses.create(
                    model=self.model,
                    temperature=self.temperature,
                    input=self.memory.all(),
                    tools=TOOLS if self.enable_tools else None
                )

                tool_call = next(
                    (item for item in response.output if item.type == "function_call"),
                    None
                )

            assistant_reply = response.output_text

            self.memory.add_assistant(assistant_reply)

            # DEBUG
            print(self.memory.all())

            print(f"\nAssistant: {assistant_reply}\n")
