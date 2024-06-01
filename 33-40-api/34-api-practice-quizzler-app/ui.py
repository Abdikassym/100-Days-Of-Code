from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg='white')
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="LOREM IPSUM",
                                                     font=("Arial", 20, 'italic'),
                                                     width=280)

        self.score_label = Label(text=f"Score: {self.quiz.score}/10",  highlightthickness=0, background=THEME_COLOR,
                                 fg='white')
        self.score_label.grid(row=0, column=1)

        right_image = PhotoImage(file='images/true.png')
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.check_answer_true)
        self.right_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.check_answer_false)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/10")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "You have reached the end of the quiz.")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def check_answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(500, func=self.get_next_question)
