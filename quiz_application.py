import tkinter as tk
from tkinter import messagebox
import random
import webbrowser

# Sample quiz questions for study (Criminal Law Victoria)
# Dictionary format:
# - question: Quiz question
# - options: Possible answers
# - answer: Correct answer
# - explanation: Brief explanation of the answer
# - learnmore: Weblink for more detailed information about the answer
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
        "explanation": "Pre-trial hearings in the Magistrates' Court for indictable offenses determine whether there is sufficient evidence to send the accused for trial in a higher court.",
        "learnmore": "https://galballyparker.com.au/what-are-pre-trial-procedures-and-how-do-they-work-in-practice/"
    }
]


def start_screen():
    
    root = tk.Tk()
    root.title("Criminal Law Study Quiz")
    root.configure(bg="purple")

    # Color constants
    BG_COLOR = "purple"
    FG_COLOR = "lightgrey"
    BTN_BG = "lightgrey"

    def show_welcome():
        
        # Clear any existing 
        for w in root.winfo_children():
            w.destroy()

        label = tk.Label(root,
                         text="Welcome to Criminal Law Study Quiz!",
                         font=("Arial", 16, "bold"),
                         fg=FG_COLOR,
                         bg=BG_COLOR)
        label.pack(pady=40)

        def launch_quiz():
            # Remove welcome and start quiz
            for w in root.winfo_children():
                w.destroy()
            app = lawQuizApp(root, back_callback=show_welcome)
            app.start_quiz()

        start_button = tk.Button(root,
                                 text="Start Quiz",
                                 font=("Arial", 14),
                                 highlightbackground=BG_COLOR,
                                 bg=BTN_BG,
                                 command=launch_quiz)
        start_button.pack(pady=20)

        quit_button = tk.Button(root,
                                text="Quit",
                                font=("Arial", 14),
                                highlightbackground=BG_COLOR,
                                bg=BTN_BG,
                                command=root.destroy)
        quit_button.pack(pady=10)

    show_welcome()
    root.mainloop()


class lawQuizApp:
    
    #Main quiz application UI.
    
    def __init__(self, root, back_callback):
        self.root = root
        self.back_callback = back_callback
        self.root.title("Criminal Law Victoria Quiz")

        # State
        self.selected_option = tk.IntVar(value=-1)
        self.questions = []
        self.q_index = 0
        self.score = 0
        self.explanations = []

        # Styling
        self.BG_COLOR = "purple"
        self.FG_COLOR = "lightgrey"
        self.BTN_BG = "lightgrey"

        # Build UI
        self.root.configure(bg=self.BG_COLOR)
        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14), bg=self.BG_COLOR, fg=self.FG_COLOR)
        self.question_label.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root,
                                text="",
                                variable=self.selected_option,
                                value=i,
                                font=("Arial", 12),
                                anchor="w",
                                justify="left",
                                bg=self.BG_COLOR,
                                fg=self.FG_COLOR,
                                selectcolor=self.BG_COLOR,
                                activebackground=self.BG_COLOR)
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 12), bg=self.BTN_BG,highlightbackground=self.BG_COLOR)
        self.next_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Cancel quiz", command=self.quit_to_start, font=("Arial", 12), bg=self.BTN_BG,highlightbackground=self.BG_COLOR)
        self.quit_button.pack(pady=5)

    def start_quiz(self, length=5):
       #Start or restart the quiz. 
        
        quiz_len = min(length, len(questions))
        # Choose random questions
        self.original_questions = random.sample(questions, k=quiz_len)
        self.questions = self.original_questions.copy()
        self.q_index = 0
        self.score = 0
        self.explanations = []
        self.selected_option.set(-1)
        self.load_question()

    def load_question(self):
        #Load question into the UI."""
        q = self.questions[self.q_index]
        self.question_label.config(text=q["question"])
        self.selected_option.set(-1)
        for rb in self.radio_buttons:
            rb.deselect()
            rb.config(text="")  # clear old text
        for i, option in enumerate(q["options"]):
            if i < len(self.radio_buttons):
                self.radio_buttons[i].config(text=option, value=i)

    def next_question(self):
        """Handle Next button: validate selection, record score and explanation, advance or show results."""
        if self.selected_option.get() == -1:
            messagebox.showwarning("Warning", "Please select an answer before continuing.")
            return

        q = self.questions[self.q_index]
        chosen = q["options"][self.selected_option.get()]
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
    
    def retry_same_quiz(self):
        self.questions = self.original_questions.copy()
        self.q_index = 0
        self.score = 0
        self.explanations = []
        self.selected_index.set(-1)
        self.load_question()
        
    def show_results(self):
        #Results Window
        explanation_text = "\n\n".join(self.explanations)
        learnmore_links = []
        for i, q in enumerate(self.questions, start=1):
            if q.get("learnmore"):
                learnmore_links.append((f"Q{i}", q["learnmore"]))

        result_window = tk.Toplevel(self.root)
        result_window.title("Quiz Completed")
        result_window.configure(bg=self.BG_COLOR)
        #Results label
        result_label = tk.Label(result_window,
                                text=f"Your score: {self.score}/{len(self.questions)}\n\n{explanation_text}",
                                justify="left",
                                bg=self.BG_COLOR,
                                fg=self.FG_COLOR,
                                font=("Arial", 12),
                                wraplength=380)
        result_label.pack(padx=20, pady=10)
        #Learn more links
        if learnmore_links:
            lm_frame = tk.Frame(result_window, bg=self.BG_COLOR)
            lm_frame.pack(padx=20, pady=(0, 10), anchor="w")
            header = tk.Label(lm_frame, text="📚 Learn more:", bg=self.BG_COLOR, fg=self.FG_COLOR, font=("Arial", 12, "bold"))
            header.pack(anchor="w")
            for label_text, url in learnmore_links:
                link = tk.Label(lm_frame, text=f"{label_text}: {url}", fg="Light Cyan", bg=self.BG_COLOR, cursor="hand2", wraplength=360, justify="left")
                # bind the click to open the URL
                link.bind("<Button-1>", lambda e, u=url: webbrowser.open(u))
                link.pack(anchor="w", pady=2)
        #Button frame for the retry options
        btn_frame = tk.Frame(result_window, bg=self.BG_COLOR)
        btn_frame.pack(pady=10)

        retry_same_button = tk.Button(btn_frame,
                                 text="Retry Quiz",
                                 font=("Arial", 14),
                                 bg=self.BTN_BG,highlightbackground=self.BG_COLOR,
                                 command=lambda: [result_window.destroy(), self.retry_same_quiz()])
        retry_same_button.grid(row=0, column=0, padx=10)
        
        # Retry with new questions
        retry_new_button = tk.Button(result_window,
                             text="New Quiz",
                             font=("Arial", 14),
                             bg=self.BTN_BG,Highlightbackground=self.BG_COLOR,
                             command=lambda: [result_window.destroy(), self.start_quiz()])
        retry_new_button.grid(row=0, column=1, padx=10)

        quit_button = tk.Button(btn_frame,
                                text="Quit",
                                font=("Arial", 14),
                                bg=self.BTN_BG,highlightbackground=self.BG_COLOR,
                                command=self.root.quit)
        quit_button.pack(padx=10)
    
    def retry_same_quiz(self):
        self.root.destroy()  # Close current quiz window
        root = tk.Tk()
        app = lawQuizApp(root)
        app.questions = self.original_questions.copy()  # Reuse same questions
        app.start_quiz()
        root.mainloop()
        
    def start_quiz(self):
        self.root.destroy()  # Close current quiz window
        root = tk.Tk()
        app = lawQuizApp(root)
        app.start_quiz()  # This will randomize new questions
        root.mainloop()


    def quit_to_start(self):
        """Return to the welcome screen without destroying the single root window."""
        if messagebox.askyesno("Confirm", "Are you sure you want to return to the welcome screen?"):
            # Remove all widgets attached to root and call the provided back callback to re-show the welcome UI
            for w in self.root.winfo_children():
                w.destroy()
            self.back_callback()


if __name__ == "__main__":
    start_screen()
