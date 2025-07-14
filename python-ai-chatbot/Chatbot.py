import random

def create_chatbot():
  
  chatbot_data = {
      "hello": ["Hello there!", "Hi!", "Greetings!"],
      "how are you": ["I'm doing well, thanks for asking!", "I'm okay.", "I'm feeling good."],
      "bye": ["Goodbye!", "See you later!", "Farewell!"]
  }

  def get_response(user_input):
    user_input = user_input.lower()

    for keyword in chatbot_data:
      if keyword in user_input:
        return random.choice(chatbot_data[keyword])

    return "I didn't understand that."

  while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
      break
    response = get_response(user_input)
    print("Chatbot:", response)

if __name__ == "__main__":
  create_chatbot()

  