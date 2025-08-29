import json
import os
import difflib

def learn_fact(question,answer):
    if os.path.exists("memory.json"):
        f = open("memory.json","r", encoding="utf-8")
        memory = json.load(f)
        f.close()
    else:
        memory = {}

    memory[f"who is {question.lower()}"] = answer

    f = open("memory.json","w", encoding="utf-8")
    json.dump(memory,f,ensure_ascii=False,indent=4)
    f.close()


def recall_answer(question):
    if os.path.exists("memory.json"):
        f = open("memory.json","r")
        memory = json.load(f)
        f.close()
    else:
        return "Hmm, I don't know that yet."
    
    question_lower = question.lower()

    if question_lower in memory:
       return memory[question_lower]
    
    closest_matches = difflib.get_close_matches(question_lower, list(memory.keys()), n=1, cutoff=0.4)

    if closest_matches:
       match = closest_matches[0]
       return memory[match]
    
    return "Hmm, I couldn't find it in my memory."
    

def greet_user():

    print("🤖 Hello! I'm MateAI or you can just call me Mate, so its time for your introduction.")
    user_name = input("\nWhat's your name: ").lower()
    if user_name == "forlone":
       print("\n🤖 Welcome Back Sir...")
    else:
       print(f"\n🤖 Nice to meet you {user_name}.")

def simple_calculator():

    print("\n🧮 Let's do a quick calculation!")

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Choose an option(1/2/3/4): "))
        
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == 1:
            return f"Result: {num1+num2}" 
        elif choice == 2:
            return f"Result: {num1-num2}" 
        elif choice == 3:
            return f"Result: {num1*num2}" 
        elif choice == 4:
            return f"Result: {num1/num2}" 
        else:
            return "❌ Invalid input."
    except:
        return "❌ Invalid choice."
    
def get_response(message):
    message = message.lower()
    
    if message.startswith("remember that"):
        try:
            fact = message.replace("remember that","").strip()
            if "is" in fact:
                question,answer = fact.split("is",1)
                question = question.strip()
                answer = answer.strip()
                learn_fact(question,answer)
                learn_fact(answer,question)
                return "Okay, I've got that."
        
            elif "that" in message:
             question,answer = message.split("that",1)
             question = question.strip()
             answer = answer.strip()
             learn_fact(question,answer)
             learn_fact(answer,question)
             return "Okay, I've got that."
            else:
             return "Please use format like 'Remember that Elon Musk is the CEO of Tesla."
        except:
           return "Apology, Something went wrong while saving."
        
    elif any(message.startswith(q) for q in ["who", "what", "where", "when", "why", "how", "at", "can", "do", "does"]):
        return recall_answer(message)

    elif any(word in message.split() for word in ["hello,hi"]):
     responce = "Hey! How you doing."
     return responce
    
  
    elif "how are you" in message or "how you doing" in message or "how you doing!" in message or "how ur doing" in message:
     responce = "I'm doing great, thanks for asking! How about you?."
     return responce


    elif "great" in message or "good" in message or "better" in message or "better than yesterday" in message:
     responce = "Good!"
     return responce
  
    elif "whats 2 + 2" in message or "what's 2 + 2" in message or "can you do some calculations" in message:
     return simple_calculator()
  
    elif "who are you" in message or "who are you?" in message:
     responce = "I'm MateAI, your future coding sidekick 😎"
     return responce
 
    else:
     return "Hmm... I'm not sure how to respond to that yet, but I'm learning!"
    

def chat():
   greet_user()
   first_time = True
   while True:
      if first_time:
         user_input = input("\nGo on! Ask Something: ").lower()
         first_time = False
      else:
         user_input = input("\n-----> ").lower()

      if user_input in ["bye","goodbye","exit","exit please","exit plz","i would like to exit","i would like to leave","ok i guess i will leave, i will catch you later","ok i guess i will leave, i catch you later","ok i guess i will leave, i'll catch you later","bye honey"]:
         exit_response = "\n🤖 MateAI: Goodbye! Keep shining ✨\n"
         print(exit_response)
         break

      response = get_response(user_input)
      print(f"\n🤖 MateAI: {response}") 


chat()  