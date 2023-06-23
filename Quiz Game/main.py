from questions_bank import questions_data
from QuestionClass import Question
from choose_question import ChooseQuestion

question_bank = [] # contains lists of question objects.
for question in questions_data:
    qstn = question["text"]
    ans = question["ans"]
    new_question = Question(qstn, ans)
    question_bank.append(new_question)
    
quiz = ChooseQuestion(question_bank)

while (quiz.has_next_question()):
    quiz.next_question()
    
# for question in question_bank:
#     print(question.text)
#     print(question.ans)