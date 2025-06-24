from openai import OpenAI

client = OpenAI(api_key="")

models = client.models.list()

for model in models.data:
    print(model.id)
