import os
import dataBase
score=0
def askQuestion(no):
    quiz=dataBase.Quiz_dict[no]
    sub_question=quiz['question']
    option=quiz['option']
    sub_answer=quiz['answer']
    return f'{sub_question}\n{option}',sub_answer
for i in range(1,len(dataBase.Quiz_dict)+1):
    question,answer=askQuestion(i-1)
    print(f'{i}.{question}')
    user=input('enter your choice(A/B/C/D) :').lower()
    os.system('cls')
    if user==answer:
        score += 1
        print(f'correct\n your score is {score}/{i}')
    else:
        print(f'wrong\n the correct answer is {answer}\nyour score is {score}/{i}')





