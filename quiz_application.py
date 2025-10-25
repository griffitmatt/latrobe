import tkinter as tk
from tkinter import messagebox
import random
import webbrowser

#Sample quiz questions for study (Crimainal Law Victoria)
# Dictionary Format
# Question - Quiz question
# Options - Possible Answers
# Answer - Answer
# Explanation - Provides brief explanation of answer
# learnmore - Weblink for more detailed information about answer 
questions = [
    {
        "question": "Which of the following best describes the 'burden of proof' in the Victorian criminal justice system?",
        "options": [
            "The responsibility of the accused to prove their innocence.",
            "The responsibility of the prosecution to prove the accused's guilt.",
            "The responsibility of the jury to determine the outcome of the trial",
            "The responsibility of the judge to ensure a fair trial."
        ],
        "answer": "The responsibility of the prosecution to prove the accused's guilt.",
        "explanation": "In Victoria, the burden of proof lies with the prosecution, which must prove guilt beyond reasonable doubt.",
        "learnmore": "https://www.legislation.vic.gov.au/"
    },
    {
        "question": "An accused person in Victoria has the right to remain silent when questioned by police. Which case is a key common law authority for this right?",
        "options": [
            "Mabo v Queensland (No 2) (1992)",
            "Petty v R (1991) 173 CLR 95",
            "Dietrich v The Queen (1992) 177 CLR 292",
            "VR v L (1991) 174 CLR 379"
        ],
        "answer": "Petty v R (1991) 173 CLR 95",
        "explanation": "The High Court in Petty v R affirmed the principle of the right to silence.",
        "learnmore": "https://jade.io/article/67668"
    },
    {
        "question": "Which court typically hears summary offenses in Victoria?",
        "options": [
            "The High Court of Australia",
            "The County Court of Victoria",
            "The Magistrates' Court of Victoria",
            "The Supreme Court of Victoria"
        ],
        "answer": "The Magistrates' Court of Victoria",
        "explanation": "Summary offences are generally heard in the Magistrates' Court.",
        "learnmore": "https://www.mcv.vic.gov.au/"
    },
    {
        "question": "Which piece of legislation primarily guides sentencing in Victoria?",
        "options": [
            "The Crimes Act 1958 (Vic)",
            "The Evidence Act 2008 (Vic)",
            "The Sentencing Act 1991 (Vic)",
            "The Bail Act 1977 (Vic)"
        ],
        "answer": "The Sentencing Act 1991 (Vic)",
        "explanation": "This Act sets out the framework and principles for sentencing.",
        "learnmore": "https://content.legislation.vic.gov.au/sites/default/files/2025-09/91-49aa231-authorised.pdf"
    },
    {
        "question": "In a jury trial for an indictable offense in Victoria, what is the jury's primary role?",
        "options": [
            "To determine the appropriate sentence if there is a conviction.",
            "To rule on complex points of law.",
            "To determine questions of fact and deliver a verdict.",
            "To present the prosecution's opening statement and closing argument."
        ],
        "answer": "To determine questions of fact and deliver a verdict.",
        "explanation": "Juries decide questions of fact, while judges handle questions of law.",
        "learnmore": "https://www.judicialcollege.vic.edu.au/"
    },
    {
        "question": "In Victoria, which legal body is typically responsible for appeals against conviction or sentence from the County Court?",
        "options": [
            "The Federal Circuit and Family Court.",
            "The High Court of Australia.",
            "The Court of Appeal (Victorian Supreme Court).",
            "The Magistrates' Court."
        ],
        "answer": "The Court of Appeal (Victorian Supreme Court).",
        "explanation": "The Court of Appeal reviews decisions from the County and Supreme Courts.",
        "learnmore": "https://www.supremecourt.vic.gov.au/"
    },
     {
        "question": "What is the purpose of a committal hearing for indictable offenses in the Magistrates' Court?",
        "options": [
            "To allow the accused to appeal their conviction.",
            "To hear summary offenses and resolve them quickly.",
            "To determine if there is sufficient evidence to proceed to trial in a higher court.",
            "To impose the final sentence for the offense."
        ],
        "answer": "To determine if there is sufficient evidence to proceed to trial in a higher court.",
        "explanation": """Pre-trial hearings in the Magistrates' Court for indictable offenses to determine if there is sufficient evidence to send the accused for trial in a higher court.""",
        "learnmore": "https://galballyparker.com.au/what-are-pre-trial-procedures-and-how-do-they-work-in-practice/"
    }
]


# --- Main Window Launcher ---
def main_window():
    root = tk.Tk()
    app = lawQuizApp(root)
    app.start_quiz()
    root.mainloop()

# --- Start Screen ---
def start_screen():
    start = tk.Tk()
    start.title("Welcome")
    
    start.configure(bg="purple")

    label = tk.Label(start, text="Welcome to Criminal Law Study Quiz!", font=("Arial", 16, "bold"),
                     fg="lightgrey", bg="purple")
    label.pack(pady=40)

    start_button = tk.Button(start, text="Start Quiz", font=("Arial", 14),
                             highlightbackground=start["bg"],
                             command=lambda: [start.destroy(), main_window()])
    start_button.pack(pady=20)

    quit_button = tk.Button(start, text="Quit", font=("Arial", 14),
                             highlightbackground=start["bg"], command=start.destroy)
    quit_button.pack(pady=10)

    start.mainloop()

# --- lawQuizApp Class ---
class lawQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Criminal Law Victoria Quiz")
        

        self.selected_index = tk.IntVar(value=-1)
        self.questions = []
        self.q_index = 0
        self.score = 0
        self.explanations = []

        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.selected_index, value=i,
                                font=("Arial", 12), anchor="w", justify="left")
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)
        #next button
        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=10)
        #Cancel quiz button
        self.quit_button = tk.Button(root, text="Cancel quiz", command=self.quit_to_start, font=("Arial", 12))
        self.quit_button.pack(pady=5)
    # Start quiz function
    def start_quiz(self):
        self.questions = random.sample(questions, 5)
        self.q_index = 0
        self.score = 0
        self.explanations = []
        self.selected_index.set(-1)
        self.load_question()
    #Load Quiz function
    def load_question(self):
        q = self.questions[self.q_index]
        self.question_label.config(text=q["question"])
        self.selected_index.set(-1)
        for rb in self.radio_buttons:
            rb.deselect()
        for i, option in enumerate(q["options"]):
            self.radio_buttons[i].config(text=option, value=i)
     #Next Quiz function
    def next_question(self):
        if self.selected_index.get() == -1:
            messagebox.showwarning("Warning", "Please select an answer before continuing.")
            return

        q = self.questions[self.q_index]
        chosen = q["options"][self.selected_index.get()]
        correct = q["answer"]

        if chosen == correct:
            self.score += 1
            self.explanations.append(f"Q{self.q_index+1}: ✅ Correct - {q['explanation']}")
        else:
            self.explanations.append(f"Q{self.q_index+1}: ❌ Incorrect - {q['explanation']}")

        self.q_index += 1
        if self.q_index < len(self.questions):
            self.load_question()
        else:
            self.show_results()
    #Show results function
    def show_results(self):
        explanation_text = "\n\n".join(self.explanations)
        learnmore_links = []
        for i, q in enumerate(self.questions, start=1):
            if q.get("learnmore"):
                learnmore_links.append(f"Q{i}: {q['learnmore']}")

        if learnmore_links:
            explanation_text += "\n\n📚 Learn more:\n" + "\n".join(learnmore_links)

        result_window = tk.Toplevel(self.root)
        result_window.title("Quiz Completed")
        result_window.configure(bg="purple")

        result_label = tk.Label(result_window,
                                text=f"Your score: {self.score}/{len(self.questions)}\n\n{explanation_text}",
                                justify="left",
                                bg="purple",
                                fg="light grey",
                                font=("Arial", 12),
                                wraplength=380)
        result_label.pack(padx=20, pady=20)

        retry_button = tk.Button(result_window,
                                 text="Retry Quiz",
                                 font=("Arial", 14),
                                 bg="light grey",
                                 command=lambda: [result_window.destroy(), self.start_quiz()])
        retry_button.pack(pady=10)

        quit_button = tk.Button(result_window,
                                text="Quit",
                                font=("Arial", 14),
                                bg="light grey",
                                command=self.root.quit)
        quit_button.pack()

    #Quit to start function
    def quit_to_start(self):
            if messagebox.askyesno("Confirm", "Are you sure you want to return to the welcome screen?"):
                self.root.destroy()
                start_screen()
            
# --- Launch App ---
if __name__ == "__main__":
    start_screen()
