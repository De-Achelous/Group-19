from Returns import Returns
from Refund import refund
from test import load_qna, process
import time

def main():
    retbot = Returns()
    print("Hello!")
    time.sleep(2)
    howareyou = str(input("How are you today?"))
    time.sleep(1.2)
    print("That's good, I am doing well!")
    time.sleep(2)

    while True:
        time.sleep(1)
        response = str(input("How may I help you today?"))
        if "return" in response.lower():
            time.sleep(2)
            retbot.Return_Process()
        elif "refund" in response.lower():
            time.sleep(2)
            refund()
        elif "question" in response.lower():
            time.sleep(2)
            print("hi what can i help you with ?")
            message = input()
            process(message)

        time.sleep(2)
        yesorno = str(input("Is there anything else I can help you with? (yes/no)"))

        if yesorno.lower() == "yes":
            pass
        elif yesorno.lower() == "no":
            time.sleep(2)
            print("Thank you for your time! Goodbye!")
            break





main()