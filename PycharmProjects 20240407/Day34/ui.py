from tkinter import *
import html
import requests

DARK_BLUE = "#173342"; DARKER_BLUE = "#202040"; PINK = "#FFC0FF"
GO_GREEN = "#448844"; NO_RED = "#884444"

class Quinterface:

    def __init__(self):
        get_api = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
        get_api.raise_for_status(); question_data = get_api.json()['results']

        self.questions = []; self.current_question = []
        for x in question_data: self.questions.append({"question": x["question"], "answer": x["correct_answer"] == "True"})
        self.current_question.append(html.unescape(self.questions[len(self.current_question)]["question"]))

        self.window = Tk()
        self.window.title("Cockfudge")
        self.window.config(padx=20, pady=20, bg=DARK_BLUE)
        self.score = 0

        self.score_board = Label(text=f"Score: {self.score} / {len(self.current_question)}",
                           padx=10, pady=10, fg=PINK, bg=DARKER_BLUE, font=('Arial', 20, 'italic'))
        self.score_board.grid(row=0, column=0, columns=2, padx=20, pady=10)
        self.question_box = Canvas(self.window, background='black', width=300, height=250)
        self.question_box.grid(row=1, column=0, columnspan=2)
        self.question_text = self.question_box.create_text(150, 125, width=280, fill=DARK_BLUE, font=("calibri", 20, "normal"))

        x = (PhotoImage(file="images/false.png")); y = PhotoImage(file="images/true.png")
        self.tick = Button(image=y, highlightthickness=0, command=self.tick)
        self.cross = Button(image=x, highlightthickness=0, command=self.cross)
        self.cross.grid(row=2, column=0); self.tick.grid(row=2, column=1)
        self.quit = Button(text="QUIT", highlightthickness=0, command=self.close)
        self.quit.grid(row=2, column=0, columns=2)

        self.question_box.itemconfig(self.question_text,
                text="Q" + str(len(self.current_question)) + ": " + str(self.current_question[-1]["question"]))
        self.window.mainloop()


    def chex(self, guess):
        win = guess == (self.current_question[-1]["answer"] == "True")
        self.score += win
        self.score_board.config(text=f"Score: {self.score} / {len(self.current_question)}")
        self.question_box.config(bg=(NO_RED, GO_GREEN)[win])
        self.question_box.itemconfig(self.question_text, text=(("Wrong!", "Correct!")[win]))
        self.window.after(1000, self.get_nect_quet)

    def get_nect_quet(self):
        self.question_box.config(bg="black")

        if len(self.current_question) <= len(self.questions):
            self.score_board.config(text=f"Score: {self.score} / {len(self.current_question)}")
            self.current_question.append(self.questions[len(self.current_question)]["questions"])
            self.question_box.itemconfig(self.question_text, text=self.current_question[-1]["question"])
        else:
            self.question_box.itemconfig(self.question_text, text="Game over")
            self.tick.config(state='disabled')
            self.cross.config(state='disabled')


    def tick(self): self.chex(1)
    def cross(self): self.chex(0)
    def close(self): self.window.destroy()

