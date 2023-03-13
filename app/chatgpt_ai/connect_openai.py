from dotenv import load_dotenv
import openai
import os
load_dotenv()
openai.api_key=os.getenv('OPENAI_KEY')

def chatgpt_response(prompt):
    response = openai.Completion.create(
    engine='text-davinci-003',
        prompt=prompt,
        temperature=0.75,
        max_tokens=4000
    )
    #print(response)
    return response ['choices'][0]['text']

