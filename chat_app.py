from openai import OpenAI
import os
from memory import ConversationMemory
from tools import TOOLS, use_tool


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
        self.memory = ConversationMemory(config.system_prompt)

    def run(self):
        print("Chatbot started. Type 'exit' to quit.\n")

        while True:
            user_input = input("User: ").strip()
            if user_input.lower() == "exit":
                break

            self.memory.add_user(user_input)

            response = self.client.responses.create(
                model=self.model,
                temperature=self.temperature,
                input=self.memory.all(),
                tools=TOOLS if self.enable_tools else None
            )

            self.memory.add_response_tool(response.output)

            # debug
            # print(self.memory.all())

            # Check for tool calls
            tool_calls = [
                item for item in response.output
                if item.type == "function_call"
            ]

            # print(tool_calls)

            if tool_calls:
                # print(len(tool_calls))
                for tool_call in tool_calls:
                    # print(tool_call.name)
                    tool_result = use_tool(tool_call)

                    #  DEBUG
                    # print(tool_result)

                    self.memory.add_tool(
                        tool_call_id=tool_call.call_id,
                        content=tool_result,
                    )

                    # DEBUG
                    # print(self.memory.all())

                #DEBUG    
                # print(self.memory.all())

                # Second call after tools executed
                follow_up = self.client.responses.create(
                    model=self.model,
                    temperature=self.temperature,
                    input=self.memory.all(),
                    tools=TOOLS
                )

                assistant_reply = follow_up.output_text
            else:
                assistant_reply = response.output_text

            self.memory.add_assistant(assistant_reply)

            # DEBUG
            # print(self.memory.all())

            print(f"\nAssistant: {assistant_reply}\n")
