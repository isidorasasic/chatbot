def summarize(client, model, messages):
    summary_prompt = (
        "Summarize the conversation so far in a concise, neutral manner."
    )

    response = client.responses.create(
        model=model,
        temperature=0,
        input=messages + [{"role": "user", "content": summary_prompt}]
    )

    return response.output_text
