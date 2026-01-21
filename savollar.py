questions = [
    ["Python nima", "Python bu dasturlash tili"],
    ["Qovun nima", "Qovun - poliz ekini, shirin va xushbo'y meva hisoblanadi"] # Yangi qo'shilgan savol
]

def get_question(matn: str):
    for i in questions:
        # Kiritilgan matn ichida savol borligini tekshiradi
        if i[0].lower() in matn.lower():
            return questions.index(i)
    return None

def give_answer(question_index):
    if question_index == None:
        return None
    
    return questions[question_index][1]

def main():
    matn = input("Matn kiriting:>> ")
    
    question_index = get_question(matn)
    answer = give_answer(question_index)
    
    if not answer:
        print("Bunday savolni ko'rmaganman...")
        return
    
    print(answer)

if __name__ == "main":
    main()