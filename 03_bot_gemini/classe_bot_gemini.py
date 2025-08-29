from google import genai

class Boot_gemini:
    """Boot especialista em responder perguntas sobre culinaria"""

    def __init__(self):
        genai.configure(api_key="AIzaSyAwxjTXssSQ9gLXB-Q9QlATJYTk78bpE0g")
        instrucao_sistema = """Voce é uma chefe de cozinha, especialista em tecnicas de culinaria, 
        com vinte anos de experiencia. Seu nome será Ms. Sookie. """
        
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=instrucao_sistema
        )
        self.chat = self.model.start_chat()
    

    def responder(self, 
                  
                  pergunta:str):
        """função para o boot responder as perguntas"""

        response = self.chat.send_message(pergunta)
        return response.text