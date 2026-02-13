
class ConversationMemory:
    """
    In-memory conversation store that tracks system, user, and assistant messages, 
    as well as tool/function call requests.
    """
    def __init__(self, system_prompt: str):
        self.messages = [{
            "role": "system",
            "content": [{
                "type": "input_text",
                "text": system_prompt
            }]
        }]

    def add_user(self, content: str):
        self.messages.append({
            "role": "user", 
            "content": [{
                "type": "input_text",
                "text": content
            }]
        })

    def add_assistant(self, content: str):
        self.messages.append({
            "role": "assistant",
            "content": [{
                "type": "output_text",
                "text": content
            }]
        })

    def add_response_tool(self, response: object):
        self.messages.append(response.output[0].model_dump())

    def add_tool_output(self, tool_call_id: str, content: str):
        self.messages.append({
            "type": "function_call_output",
            "call_id": tool_call_id,
            "output": content
        })

    def all(self):
        return self.messages
