
class ConversationMemory:
    def __init__(self, system_prompt: str):
        self.messages = [{"role": "system", "content": system_prompt}]

    def add_user(self, content: str):
        self.messages.append({"role": "user", "content": content})

    def add_assistant(self, content: str):
        self.messages.append({"role": "assistant", "content": content})

    def add_response_tool(self, response_function_tool_call: object):
        self.messages.append(response_function_tool_call[0])

    def add_tool(self, tool_call_id: str, content: str):
        self.messages.append({
            "type": "function_call_output",
            "call_id": tool_call_id,
            "output": content
        })

    def all(self):
        return self.messages
