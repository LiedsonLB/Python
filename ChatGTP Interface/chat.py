import openai

openai.api_key = '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'
while True:
    model_engine = "text-davinci-003"
    prompt = input('O que deseja saber ? ')
    if 'exit' in prompt or 'quit' in prompt:
        break

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,stop=None,
        temperature=0.5)
    
    response = completion.choices[0].text
    print(response)