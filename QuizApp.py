import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self):
        self.quiz_data = [
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter", "Venus"],
                "correct_answer": 1
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Vincent Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
                "correct_answer": 2
            },
            {
                "question": "What is the smallest prime number?",
                "options": ["0", "1", "2", "3"],
                "correct_answer": 2
            },
            {
                "question": "In which year did the Titanic sink?",
                "options": ["1905", "1910", "1912", "1915"],
                "correct_answer": 2
            },
            {
                "question": "What is the capital of Australia?",
                "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
                "correct_answer": 2
            },
        ]
        self.current_question_index = 0
        self.score = 0

        self.window = tk.Tk()
        self.window.title("Quiz App")

        self.question_label = tk.Label(self.window, text="", wraplength=400)
        self.question_label.pack(pady=20)

        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.options_frame, text="", width=30, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_question_button = tk.Button(self.window, text="Next Question", width=30, command=self.next_question)
        self.next_question_button.pack(pady=20)

        self.load_question()

    def start_quiz(self):
        self.window.mainloop()

    def load_question(self):
        question_data = self.quiz_data[self.current_question_index]
        # Debug statement to print current question data
        print("Loading question:", question_data)
        if "options" in question_data:
            self.question_label.config(text=question_data["question"])
            options = question_data["options"]
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
        else:
            print(f"Error: 'options' key not found in question {self.current_question_index}")

    def check_answer(self, selected_option):
        question_data = self.quiz_data[self.current_question_index]
        correct_answer_index = question_data["correct_answer"]
        if selected_option == correct_answer_index:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", "Your answer is incorrect!")

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index == len(self.quiz_data):
            messagebox.showinfo("Quiz Over", f"Quiz finished. Your score: {self.score}/{len(self.quiz_data)}")
            self.window.quit()  # This will quit the main loop and close the application
        else:
            self.load_question()

    def reset_quiz(self):
        self.current_question_index = 0
        self.score = 0
        self.load_question()

quiz_app = QuizApp()
quiz_app.start_quiz()
