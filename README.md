# Prompt Engineering Playground

This is a simple CLI tool to experiment with different prompt engineering strategies using OpenAI’s GPT models. Great for prototyping, learning, and testing.

## 🧠 Features

- Send custom prompts to GPT (ChatCompletion API)
- Get instant responses in the terminal
- Rapid iteration for prompt engineering experiments

## 🛠 Requirements

- Python 3.10+
- `openai` package

Install dependencies:
```bash
pip install openai
```

## ▶️ How to Run

1. Set your OpenAI API key:
```python
openai.api_key = "your-api-key"
```

2. Run the script:
```bash
python prompt_tester.py
```

3. Enter prompts and see how the model responds. Try adjusting:
- Wording
- Structure
- Role instructions
- Input context

## ⚠️ Note

Do not share your API key publicly. Consider using `.env` for safety in production environments.

## 📄 License

MIT License © 2025 Your Name
