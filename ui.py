THEME_COLOR = "#383e4e"
from tkinter import *
from PIL import Image
from PIL import ImageTk
from numpy import tile
from quiz_brain import QuizBrain
from tkinter import messagebox

class QuizUi:
    def __init__(self,quizbrain:QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("QuizBrain")
        self.window.geometry("500x500")
        self.window_icon = ImageTk.PhotoImage(file="quiz.jpg")
        self.window.iconphoto(False,self.window_icon)
        self.window.config(background=THEME_COLOR,padx=20,pady=20)
        self.score_label = Label(text="Score:",bg=THEME_COLOR,fg="white",font=("Courier", 13))
        self.score_label.place(x=330,y=10)
        self.canvas = Canvas(width=420,height=250,bg="white")
        self.canvas.place(x=18,y=60)
        self.question_text = self.canvas.create_text(210,125,font=("Courier", 15,"bold"),width=400,text="Sample",fill=THEME_COLOR)
        self.true_image = Image.open('true.png')
        self.true_image = self.true_image.resize((100, 100))
        self.true_image = ImageTk.PhotoImage(self.true_image)
        self.false_image = Image.open('false.png')
        self.false_image = self.false_image.resize((100, 100))
        self.false_image = ImageTk.PhotoImage(self.false_image)
        # self.true_image = PhotoImage(file="true.png")
        # self.false_image = PhotoImage(file="false.png")
        self.button1 = Button(self.window,image=self.true_image,command=lambda t="True": self.checkAnswer(t))
        self.button1.place(x=60,y=350)
        self.button2 = Button(self.window,image=self.false_image,command=lambda t="False": self.checkAnswer(t))
        self.button2.place(x=280,y=350)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            if self.quiz.score>7:
                self.canvas.itemconfig(self.question_text,text=f"You have reached the end of the Quiz. Your Score= {self.quiz.score}/10. \n\n   Good Job🙌")
            else:
                self.canvas.itemconfig(self.question_text,text=f"You have reached the end of the Quiz. Your Score= {self.quiz.score}/10. \n\n   Better Luck Next Time😛")
                self.button1.config(state="disabled")
                self.button2.config(state="disabled")
            choice = messagebox.askquestion(title="Quiz Over",message="Do you want to start another Quiz?")
            if choice == "yes":
                self.window.destroy()
                self.quiz.clear_all()
                QuizUi(self.quiz)
            if choice == "no":
                self.window.destroy()
    def checkAnswer(self,t):
        if t == "True":
            correct_answer = self.quiz.check_answer("True")
        if t == "False":
            correct_answer = self.quiz.check_answer("False")
        self.give_feedback(t,correct_answer)
    def give_feedback(self,t,correct_answer):
        if correct_answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red") 
        self.window.after(1000,self.get_question)

# QuizUi()