import tkinter as tk
import random
from tkinter import messagebox

user_score = 0
computer_score = 0
def play_game(user_choice):
    global user_score, computer_score
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1
    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}\n\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Score - You: 0 | Computer: 0")
def exit_game():
    window.quit()
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("500x450")
window.configure(bg="#f8f9fa")  
instructions = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 16, "bold"), bg="#f8f9fa", fg="#333")
instructions.pack(pady=20)

result_label = tk.Label(window, text="Make your move!", font=("Helvetica", 14), bg="#ffffff", fg="#333", width=40, height=5, relief="solid", bd=1)
result_label.pack(pady=20)

score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12, "italic"), bg="#f8f9fa", fg="#444")
score_label.pack(pady=10)

button_frame = tk.Frame(window, bg="#f8f9fa")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game("Rock"), width=10, font=("Helvetica", 12), bg="#6c757d", fg="white", activebackground="#5a6268", activeforeground="white")
rock_button.grid(row=0, column=0, padx=15)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("Paper"), width=10, font=("Helvetica", 12), bg="blue", fg="white", activebackground="#0056b3", activeforeground="white")
paper_button.grid(row=0, column=1, padx=15)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game("Scissors"), width=10, font=("Helvetica", 12), bg="#dc3545", fg="white", activebackground="#c82333", activeforeground="white")
scissors_button.grid(row=0, column=2, padx=15)


play_again_button = tk.Button(window, text="Play Again", command=reset_game, width=15, font=("Helvetica", 12), bg="light green", fg="black", activebackground="#e0a800", activeforeground="black")
play_again_button.pack(pady=10)

exit_button = tk.Button(window, text="Exit", command=exit_game, width=15, font=("Helvetica", 12), bg="yellow", fg="black", activebackground="#5a6268", activeforeground="black")
exit_button.pack(pady=5)

window.mainloop()
