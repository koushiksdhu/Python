class ChooseQuestion:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        fetch_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        
    def has_next_question(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self):
        if(self.fetch_answer == self.current_question.answer):
            self.score += 1
