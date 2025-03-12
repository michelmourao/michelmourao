# API Key: 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
# pip install openai
# https://platform.openai.com/docs/overview

from openai import OpenAI

from rich.markdown import Markdown
from rich.console import Console

historico = [
    {"role": "system", "content": "you're a helpful assistant."}  # Contexto inicial
]

client = OpenAI()


while True:
    print("")
    user_input = input("You: ")
    print("")

    if user_input.lower() in ["sair", "exit", "quit"]:
        print("\nConversa encerrada. Histórico descartado.")
        historico.clear()
        break
    
    if user_input.lower() in ["historico", "#hist"]:
        print(historico)

    historico.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=historico,
        stream=True
    )

    content = ""

    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")
            content += chunk.choices[0].delta.content

    historico.append({"role": "assistant", "content": content})
    
# console = Console()
# console.print(Markdown(completion.choices[0].message.content))
# #print(completion.choices[0].message.content)

