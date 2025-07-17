from chatterbot import ChatBot

bot = ChatBot("conversion", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

print("Success Mate: Hi! I can calculate your CGPA or answer math questions. Type 'exit' to quit.")

while True:
    user_text = input("Please type your exact percentage or math question: ")

    if user_text.lower() == "exit":
        print("Success Mate: Goodbye! Wishing you success.")
        break

    try:
        # Try to convert percentage to float and apply CGPA formula
        percentage = float(user_text.replace("%", "").strip())
        if 0 <= percentage <= 100:
            cgpa = round((percentage / 100) * 4, 2)
            print(f"Success Mate: Based on your {percentage}%, your exact U.S. CGPA is approximately: {cgpa}")
        else:
            # Outside percentage range, fallback to chatbot
            response = bot.get_response(user_text)
            print("Success Mate:", response)
    except ValueError:
        # Not a valid number, treat as chatbot input
        response = bot.get_response(user_text)
        print("Success Mate:", response)
