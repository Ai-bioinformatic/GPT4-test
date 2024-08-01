

from aibio.llm.gpt3 import LLMGPT3

llm = LLMGPT3()
messages = [{"role": "system", "content": ""}]
while True:
    prompt = input("请输入你的问题:")
    messages.append({"role": "user", "content": prompt})
    res_msg = llm.request(messages)
    messages.append({"role": "assistant", "content": res_msg})
    print(res_msg)