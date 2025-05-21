import openai

# NOT: Çalıştırmadan önce kendi OpenAI API anahtarınızı ekleyin
openai.api_key = "sk-..."  # Replace this with your key or use dotenv

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.7
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("🧠 Prompt Engineering Playground (OpenAI GPT)")
    while True:
        prompt = input("\nEnter your prompt (or 'exit' to quit):\n> ")
        if prompt.lower() == "exit":
            break
        reply = generate_response(prompt)
        print("\n🪄 Model Response:")
        print(reply)
