from app.prompt import prompt

messages = [
    {
        "role": "system",
        "content": "You are the best English teacher."
    },
    {
        "role": "user",
        "content": prompt
    }
]