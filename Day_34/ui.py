from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.root = Tk()
        self.root.title("Quizzler")
        self.root.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0

        # Score label
        self.score_label = Label(text=f"Score: {self.score}", font=(FONT_NAME, 20), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=1, column=2)

        # Canvas for question text
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="Loading questions...", fill=THEME_COLOR,
                                                     font=(FONT_NAME, 15, "italic"), width=280)

        # Buttons
        # True button
        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=self.true_btn_click)
        self.true_btn.grid(row=3, column=2)

        # False button
        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=self.false_btn_click)
        self.false_btn.grid(row=3, column=1)

        # Check if question_list is empty
        if len(self.quiz_brain.question_list) == 0:
            # If the API did not load questions, show an error message
            self.canvas.itemconfig(self.question_text, text="Error: Unable to load questions from API.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
        else:
            # If questions are available, start the quiz
            self.get_next_question()



        self.root.mainloop()

    def get_next_question(self):
        # Reset canvas color to white for each new question
        self.canvas.config(bg="white")

        if self.quiz_brain.still_has_questions():
            question_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        else:
            # No more questions, display final score
            self.canvas.itemconfig(self.question_text, text=f"Your Final score is {self.quiz_brain.score}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_btn_click(self):
        self.give_feedback(self.quiz_brain.check_answer("true"))

    def false_btn_click(self):
        self.give_feedback(self.quiz_brain.check_answer("false"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # Move to the next question after a delay
        self.root.after(1000, self.get_next_question)