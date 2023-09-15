from tkinter import *
from quiz_brain import QuizBrain

# CONSTANT:
THEME_COLOR = "#375362"


class QuizzlerInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question is getting loaded.", width=280, fill=THEME_COLOR, font=("Arial", 16, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file="images/true.png");
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        false_image = PhotoImage(file="images/false.png");
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        
        
        self.get_next_ques()
        
        self.window.mainloop()

    def get_next_ques(self):
        self.canvas["bg"] = "#fff"
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button["state"] = "disabled"
            self.false_button["state"] = "disabled"
            
            
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas["bg"] = "green"
        else:
            self.canvas["bg"] = "red"
        self.window.after(1000, self.get_next_ques)
        self.score_label["text"] = f"Score: {self.quiz.score}/{self.quiz.question_number}"
            
        
        

        