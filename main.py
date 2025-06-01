from openai import OpenAI

client = OpenAI(api_key="") #create and paste your OpenAI api key here from https://platform.openai.com/api-keys

def chatwithai(prompt):
    response = client.chat.completions.create(model="gpt-4o",
    messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content.strip()
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "q", "byhe"]:
            print("Exiting the chat. Goodbye!")
            break   
        response = chatwithai(user_input)
        print(f"AI: {response}")