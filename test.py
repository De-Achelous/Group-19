

# Loading question and answer from text file
def load_qna():
    questions = []
    answers = []
    with open('QNA.txt') as text:
        for line in text.readlines():
            split = line.split("--")
            questions.append(split[0])
            answers.append(split[1])
        text.close
    return questions,answers

def process(input):
    
    err_message="Sorry I cann't understand your question!"
    
    if (input.lower()==load_qna()[0][0].lower())or(input.lower()=="hours"):
        return load_qna()[1][0]
    elif (input.lower()==load_qna()[0][1].lower())or(input.lower()=="shipment"):
        return load_qna()[1][1]
    elif (input.lower()==load_qna()[0][2].lower())or(input.lower()=="contact"):
        return load_qna()[1][2]
    elif (input.lower()==load_qna()[0][3].lower())or(input.lower()=="help"):
        return load_qna()[1][3]
    else:
        return err_message
    
 
  
    
##print(process("when does the store open/close?"))

        
