from icecream import ic
import html


class QuizBrain:
    def __init__(self, questions):
        self.all_questions = questions
        self.current_question = []

    def next_question(self):
        self.current_question.append(html.unescape(self.all_questions[len(self.current_question)]["question"]))
        return f"Q.{len(self.current_question)}: {self.current_question[-1]}", self.current_question[-1]["answer"] == "True"

    def check_answer(self):
        return self.current_question[-1]["answer"] == "True"