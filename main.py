from Returns import Returns
from Refund import refund
from test import load_qna, process
import PySimpleGUI as sg
import time

# Set theme for the GUI
sg.theme("DarkAmber")

question = "Hello! How are you today?"
layout = [[sg.Text("", key="-RECORDS-")],
          [sg.Text(question, key="-BOT-")],
          [sg.Input(key="-HUMAN-")],
          [sg.Button("OK"), sg.Button("EXIT")]]

window = sg.Window("Chatbot", layout)

while True:
    event, values = window.read()
    # print(event, values)
    # print(values["-IN-"])
    if event in (None, 'EXIT'):
        break

    # Save the old chat records & current questions
    Text = window["-RECORDS-"].get()
    Question = window["-BOT-"].get()

    # Update the chat records
    window["-RECORDS-"].update(Text + "\n" + Question + ":\n" + values['-HUMAN-'])

    # Process the user's greeting and give response, some nlp apis can goes here.
    IN = values['-HUMAN-']
    time.sleep(0.5)
    if "good" in IN.lower():
        window["-BOT-"].update("That's good!")
    if "bad" in IN.lower():
        window["-BOT-"].update("Sorry to hear that!")
    # time.sleep(0.5)

    Question = window["-BOT-"].get()
    Text = window["-RECORDS-"].get()
    window["-RECORDS-"].update("\n" + Text + "\n" + Question + ":\n")

    # Bot ask for a job
    window["-BOT-"].update("How can I help you today?")
    IN = values['-HUMAN-']
    if "return" in IN.lower():
        print("return")
    elif "refund" in IN.lower():
        print("refund")
    elif "question" in IN.lower():
        print("question")

    Question = window["-BOT-"].get()
    Text = window["-RECORDS-"].get()
    window["-RECORDS-"].update("\n" + Text + "\n" + Question + ":\n")

    # End of conversation
    window["-BOT-"].update("Is there anything else I can help you with? (yes/no)")
    IN = values['-HUMAN-']
    if "yes" in IN.lower():
        continue
    if "no" in IN.lower():
        exit(1)

window.close()
exit()


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

# main()
