from google import genai
client = genai.Client( api_key= "AIzaSyDec3s7AsDRXmaWDITmq3s-EjXmLUS1MrI")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="como cozinhar?"
)
print(response.text)