#!/usr/bin/env python3

from openai import OpenAI
import sys

client = OpenAI(api_key = "") # ENTER API KEY!
prompt = " ".join(sys.argv[1:])

system = """
    You are a command line AI assistant.
    Give brief answers with minimal formatting.
"""

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": prompt}
    ]
)

print(completion.choices[0].message.content)