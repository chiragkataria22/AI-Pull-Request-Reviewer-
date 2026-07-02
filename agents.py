from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def run_agent(role, code):

    prompt = f"""
    You are a {role}.

    Review this code:

    {code}

    Return findings.
    """

    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    return response.choices[0].message.content