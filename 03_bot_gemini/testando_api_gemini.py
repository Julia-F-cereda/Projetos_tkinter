from google import genai

client = genai.Client( api_key= "AIzaSyAwxjTXssSQ9gLXB-Q9QlATJYTk78bpE0g")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="como cozinhar?"
)
print(response.text)