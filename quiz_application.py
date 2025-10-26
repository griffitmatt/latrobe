import tkinter as tk
from tkinter import messagebox
import random
import webbrowser
import time

#Matt Griffiths 20226373

# Sample quiz questions for study (Criminal Law Victoria)
# Dictionary format:
# - question: Quiz question
# - options: Possible answers
# - correct_index: use index of the correct answer in options
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
        "correct_index": 1,
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
        "correct_index": 1,
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
        "correct_index": 2,
        "explanation": "Summary offences are generally heard in the Magistrates' Court.",
        "learnmore": "https://www.mcv.vic.gov.au/criminal-matters/criminal-offences/summary-offences"
    },
    {
        "question": "Which piece of legislation primarily guides sentencing in Victoria?",
        "options": [
            "The Crimes Act 1958 (Vic)",
            "The Evidence Act 2008 (Vic)",
            "The Sentencing Act 1991 (Vic)",
            "The Bail Act 1977 (Vic)"
        ],
        "correct_index": 2,
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
        "correct_index": 2,
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
        "correct_index": 2,
        "explanation": "The Court of Appeal reviews decisions from the County and Supreme Courts.",
        "learnmore": "https://www.supremecourt.vic.gov.au/areas/court-of-appeal/"
    },
    {
        "question": "What is the purpose of a committal hearing for indictable offenses in the Magistrates' Court?",
        "options": [
            "To allow the accused to appeal their conviction.",
            "To hear summary offenses and resolve them quickly.",
            "To determine if there is sufficient evidence to proceed to trial in a higher court.",
            "To impose the final sentence for the offense."
        ],
        "correct_index": 2,
        "explanation": "Pre-trial hearings in the Magistrates' Court for indictable offenses determine whether there is sufficient evidence to send the accused for trial in a higher court.",
        "learnmore": "https://galballyparker.com.au/what-are-pre-trial-procedures-and-how-do-they-work-in-practice/"
    },
    {
        "question": "What is the primary difference between the 'but for' test and the legal causation test in proving actus reus?",
        "options": [
            "The 'but for' test focuses on mental state, while legal causation focuses on physical actions.",
            "The 'but for' test applies to omissions, while legal causation applies to acts.",
            "The 'but for' test establishes factual link, while legal causation considers operating and substantial cause.",
            "The 'but for' test establishes foreseeability, while legal causation establishes direct intent."
        ],
        "correct_index": 2,
        "explanation": (
            "The 'but for' test determines factual causation by asking if the harm would have occurred without the defendant's action; "
            "legal causation (cause in fact) considers whether the defendant's act was an operating and substantial cause of the harm. "
            "Legal causation requires the harm to be a foreseeable result of the act, not a remote or insignificant one."
        ),
        "learnmore": "https://www.fedcourt.gov.au/digital-law-library/judges-speeches/speeches-former-judges/justice-edelman/edelman-j-20150907"
    }
]

#constants
#Window Title 
APP_TITLE = "Criminal Law Study App"
#Colours
BG_COLOR = "purple"
FG_COLOR = "lightgrey"
BTN_BG = "lightgrey"


def start_screen():
    
    root = tk.Tk()
    root.title(APP_TITLE)
    root.configure(bg="purple")

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
            app = lawQuizApp(root, back_callback=show_welcome, bg_color=BG_COLOR, fg_color=FG_COLOR, btn_bg=BTN_BG)
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
    
    def __init__(self, root, back_callback, bg_color, fg_color, btn_bg):
        self.root = root
        self.back_callback = back_callback
        

        # State
        # use explicit master for the IntVar
        self.selected_option = tk.IntVar(self.root, value=-1)
        self.questions = []
        self.q_index = 0
        self.score = 0
        self.explanations = []

        #Colour style
        self.BG_COLOR = bg_color
        self.FG_COLOR = fg_color
        self.BTN_BG = btn_bg

        # Build UI
        self.root.configure(bg=self.BG_COLOR)
        # Put all widgets inside a content frame so it's easier to clear/replace views
        self.content_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        self.content_frame.pack(fill="both", expand=True)

        self.question_label = tk.Label(self.content_frame, text="", wraplength=400, font=("Arial", 14), bg=self.BG_COLOR, fg=self.FG_COLOR)
        self.question_label.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.content_frame,
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

        self.next_button = tk.Button(self.content_frame, text="Next", command=self.next_question, font=("Arial", 12), bg=self.BTN_BG, highlightbackground=self.BG_COLOR)
        self.next_button.pack(pady=10)

        self.quit_button = tk.Button(self.content_frame, text="Cancel quiz", command=self.quit_to_start, font=("Arial", 12), bg=self.BTN_BG, highlightbackground=self.BG_COLOR)
        self.quit_button.pack(pady=5)
        
 
          
        

    def start_quiz(self, length=5):
       #Start or restart the quiz. 
        #Ensure quiz will still run if there are less than 5 questions
        quiz_len = min(length, len(questions))
        # Choose random questions
        self.original_questions = random.sample(questions, k=quiz_len)
        self.questions = self.original_questions.copy()
        self.q_index = 0
        self.score = 0
        self.explanations = []
        self.selected_option.set(-1)
        
                
        self.show_quiz_view()
        # Set timer countdown in seconds. Currentlly 5 minutes
        self.countdown(300)

    def show_quiz_view(self):
        # Reset content_frame to show fresh quiz content
        for w in self.content_frame.winfo_children():
            w.destroy()

        #timer label
        self.status = tk.Label(
        self.content_frame,
        text="",
        bg=self.BG_COLOR,
        fg=self.FG_COLOR,
        font=("Times", 16, "bold underline")
         )
        self.status.pack(pady=10)


        self.question_label = tk.Label(self.content_frame, text="", wraplength=400, font=("Arial", 14), bg=self.BG_COLOR, fg=self.FG_COLOR)
        self.question_label.pack(pady=20)

        self.radio_buttons = []
        
        
        for i in range(4):
            rb = tk.Radiobutton(self.content_frame,
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

        self.next_button = tk.Button(self.content_frame, text="Next", command=self.next_question, font=("Arial", 12), bg=self.BTN_BG, highlightbackground=self.BG_COLOR)
        self.next_button.pack(pady=10)

        self.quit_button = tk.Button(self.content_frame, text="Cancel quiz", command=self.quit_to_start, font=("Arial", 12), bg=self.BTN_BG, highlightbackground=self.BG_COLOR)
        self.quit_button.pack(pady=5)
        
       
        # Load the first (current) question.
        self.load_question()
        
    def load_question(self):
        #Load question into the UI.
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
       # Next Question, populate possible answers, record answer and explanation.
        if self.selected_option.get() == -1:
            messagebox.showwarning("Warning", "Please select an answer before continuing.")
            return

        q = self.questions[self.q_index]
        chosen_index = self.selected_option.get()
        correct_index = q.get("correct_index", None)

        if correct_index is None:
            # Fallback: if dataset still uses 'answer' text, attempt to compare strings
            chosen_text = q["options"][chosen_index]
            correct_text = q.get("answer", "")
            if chosen_text == correct_text:
                self.score += 1
                self.explanations.append(f"Q{self.q_index+1}: ✅ Correct - {q['explanation']}")
            else:
                self.explanations.append(f"Q{self.q_index+1}: ❌ Incorrect - {q['explanation']} (Correct: {correct_text})")
        else:
            if chosen_index == correct_index:
                self.score += 1
                self.explanations.append(f"Q{self.q_index+1}: ✅ Correct - {q['explanation']}")
            else:
                correct_text = q["options"][correct_index]
                self.explanations.append(f"Q{self.q_index+1}: ❌ Incorrect - {q['explanation']} (Correct: {correct_text})")

        self.q_index += 1
        if self.q_index < len(self.questions):
            self.load_question()
        else:
            self.show_results()
    
    def reset_to_original_questions(self):
        #Reuse original questions instead of generating new set of questions
        self.questions = self.original_questions.copy()
        self.q_index = 0
        self.score = 0
        self.explanations = []
        self.selected_option.set(-1)
        self.show_quiz_view()

    def show_results(self):
         # Clear the window show results
        for w in self.content_frame.winfo_children():
            w.destroy()

        explanation_text = "\n\n".join(self.explanations)
        learnmore_links = []
        # Use original_questions to map consistently to displayed Q numbers
        for i, q in enumerate(self.original_questions, start=1):
            if q.get("learnmore"):
                learnmore_links.append((f"Q{i}", q["learnmore"]))

        # Results label
        result_label = tk.Label(self.content_frame,
                                text=f"Your score: {self.score}/{len(self.questions)}",
                                justify="left",
                                bg=self.BG_COLOR,
                                fg=self.FG_COLOR,
                                font=("Arial", 14))
        result_label.pack(padx=20, pady=(10, 5), anchor="w")

        explanations_label = tk.Label(self.content_frame,
                                     text=explanation_text,
                                     justify="left",
                                     bg=self.BG_COLOR,
                                     fg=self.FG_COLOR,
                                     font=("Arial", 12),
                                     wraplength=600)
        explanations_label.pack(padx=20, pady=(0, 10), anchor="w")

        # Learn more links (if any)
        if learnmore_links:
            lm_frame = tk.Frame(self.content_frame, bg=self.BG_COLOR)
            lm_frame.pack(padx=20, pady=(0, 10), anchor="w")
            header = tk.Label(lm_frame, text="Learn more:", bg=self.BG_COLOR, fg=self.FG_COLOR, font=("Arial", 12, "bold"))
            header.pack(anchor="w")
            for label_text, url in learnmore_links:
                link = tk.Label(lm_frame, text=f"{label_text}: {url}", fg="light cyan", bg=self.BG_COLOR, cursor="hand2", wraplength=560, justify="left")
                # bind the click to open the URL
                link.bind("<Button-1>", lambda e, u=url: webbrowser.open(u))
                link.pack(anchor="w", pady=2)

        # Button frame for options
        btn_frame = tk.Frame(self.content_frame, bg=self.BG_COLOR)
        btn_frame.pack(pady=10)

        retry_same_button = tk.Button(btn_frame,
                                 text="Retry Quiz",
                                 font=("Arial", 14),
                                 bg=self.BTN_BG, highlightbackground=self.BG_COLOR,
                                 command=self.reset_to_original_questions)
        retry_same_button.pack(side="left", padx=10)
        
        # Retry with new questions
        retry_new_button = tk.Button(btn_frame,
                             text="New Quiz",
                             font=("Arial", 14),
                             bg=self.BTN_BG, highlightbackground=self.BG_COLOR,
                             command=lambda: self.start_quiz())
        retry_new_button.pack(side="left", padx=10)
        
        # Button to exit the application
        quit_button = tk.Button(btn_frame,
                                text="Quit",
                                font=("Arial", 14),
                                bg=self.BTN_BG, highlightbackground=self.BG_COLOR,
                                command=self.root.quit)
        quit_button.pack(side="left", padx=10)
    
    def countdown(self, time, msg='Time Left : '):
        
        #timer minutes and seconds 
        if time > 0:
            minutes = time // 60
            seconds = time % 60
            self.status.config(
             text=f"{msg}{minutes:02d}:{seconds:02d}",
             font=("Arial", 16, "bold underline")
             )
            self.root.after(1000, self.countdown, time - 1, msg)
        else:
            self.status.config(text="Time's up!")
            self.show_results()
            
    def quit_to_start(self):
        # Prompt user to confirm return to welcome screen
        if messagebox.askyesno("Confirm", "Are you sure you want to return to the welcome screen?"):
            # Remove all windows
            for w in self.root.winfo_children():
                w.destroy()
            self.back_callback()

# This is important if you want the start screen to start.
if __name__ == "__main__":
    start_screen()