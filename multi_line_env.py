from dotenv import load_dotenv
import os
import json
load_dotenv()
x = json.loads(os.getenv("test"))

for y in x:
    print(y)

print(x[1])
