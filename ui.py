import tkinter as tk
import customtkinter
from tkinter import messagebox
from PIL import Image
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from question_data import categories_list, categories, categories_dict
import requests
#import matplotlib.pyplot as plt

API_URL = 'https://opentdb.com/api.php'
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



class Trivia_Ui:
    def __init__(self,trivia_brain,database_manager):
        self.trivia_brain = trivia_brain
        self.database_manager = database_manager
        self.graph_exists = False
        self.root = customtkinter.CTk()
        self.root.geometry = ("50000x50000")
        self.welcome_screen()
        self.root.mainloop()
        
        

    # Method for Creating the Opening Screen of the APP
    def welcome_screen(self):
        self.root.title("Trivia Training Module")
        self.root.config(padx=20,pady=20)
        

        self.canvas = tk.Canvas(width=300, height=250, bg = "#1a1a1a")
        self.canvas.grid(row = 2, column = 0, columnspan=2, pady=50)

        self.welcome = tk.Canvas(width= 350, height = 50, bg = "#1a1a1a",borderwidth=0, highlightthickness=0)
        self.welcome_text = self.welcome.create_text(175,25, text = 'Welcome To The Trivia Training Module', fill="#FFFFFF", font = ('News Gothic Light',12),width =300)
        self.welcome.grid(row = 1, column = 0, columnspan = 2, pady = 50)

        self.optionmenu = customtkinter.CTkOptionMenu(self.root, values=["General Knowledge", "Animals","Arts", "Politics", "History"], command=self.optionmenu_callback)
        self.optionmenu.set("Select An Option")
        self.optionmenu.grid(row = 2, column = 1,padx = 100)

        self.begin = customtkinter.CTkButton(master = self.root , text = "Begin!", command = self.trivia_screen)
        self.begin.grid(row = 3, column=1)

    def optionmenu_callback(self,choice):
        print("optionmenu dropdown clicked:", choice)
        self.category_selected = choice

    def trivia_screen(self):
        #try:
        print(self.category_selected)
        selected_text=f'You Have Selected : {self.category_selected}\n Please Wait For First Question'
        self.welcome.destroy()
        self.optionmenu.destroy()
        self.begin.destroy()
        #self.graph.destroy()
        
    #Creating new labels for updated window screen
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=selected_text,
            fill='white',
            font=("News Gothic Light", 20, "italic")
        )
        
        #Creating buttons for answering true or false
        self.true_image = customtkinter.CTkImage(dark_image=Image.open("images/true.png"))
        self.true_button = customtkinter.CTkButton(master = self.root,text = "",image=self.true_image, command=self.true_pressed,fg_color="#1a1a1a",width = 30)
        self.true_button.grid(row=3, column=0)
        
        
        self.false_image = customtkinter.CTkImage(dark_image=Image.open("images/false.png"))
        self.false_button = customtkinter.CTkButton(master = self.root,text = "", image=self.false_image, command=self.false_pressed,fg_color="#1a1a1a",width = 30)
        self.false_button.grid(row=3, column=1)

        #Creating labels for displaying question number and current score
        self.score_label = customtkinter.CTkLabel(master = self.root,text=f"Score: {self.trivia_brain.score}")
        self.score_label.grid(row=0, column=1)


        self.question_number_label = customtkinter.CTkLabel(master = self.root,text = f"Question Number: {self.trivia_brain.question_number}")
        self.question_number_label.grid(row=0, column=0)

        print("here")
        #Create the questions for displaying
        self.question_category()


        #After a couple of seconds, display the first question
        self.root.after(2000,self.get_next_question)

    # If there is no selected category, display an error box
        #except:
        #messagebox.showerror("Error", "No Category Selected!")

    # Button Arguments
    def true_pressed(self):
        user_answer = 'True'
        is_correct = self.trivia_brain.check_answer(user_answer)
        #Check the user answer against question
        self.right_wrong(is_correct)

    #Method for grabbing the questions for the category from API
    def question_category(self):
        # Creating Question Data From Selected Category
        #category_id = categories_list.index(self.category_selected) + 9
        category_id = categories_dict[self.category_selected]
        print(f"Category ID : {category_id}")
        params = {
            'category': category_id,
            'amount': 2,
            'type': 'boolean'
        }

        response = requests.get(url=API_URL, params=params)
        question_data = response.json()
        question_data = question_data['results']
        #self.question_data = question_data

        #Pass the question data to the trivia brain for manipulation
        self.trivia_brain.create_questions(question_data)




    def false_pressed(self):
        user_answer = 'False'
        is_correct = self.trivia_brain.check_answer(user_answer)
        #Check the user answer against question
        self.right_wrong(is_correct)

    def get_next_question(self):
        self.canvas.config(bg="#1a1a1a")

        #Update scores and question numbers
        self.score_label.configure(text=f'Score: {self.trivia_brain.score}')
        self.question_number_label.configure(text = f"Question Number: {self.trivia_brain.question_number}")

        #If there are more questions, display one, if not end the game
        question = self.trivia_brain.next_question()
        if question != False:
            self.canvas.itemconfig(self.question_text,text = question)
        else:
            self.canvas.itemconfig(self.question_text, text = f'Game Over: Your score was {self.trivia_brain.score}')
            # Commit Score To Correct Database Label
            print(f"Category Selected : {self.category_selected}")
            self.database_manager.add_values(self.category_selected,self.trivia_brain.score)
            
            self.true_button.destroy()
            self.false_button.destroy()

            self.graph = customtkinter.CTkButton(text = "Results", command = self.graph_results)
            self.graph.grid(row = 3, column =2)


            self.play_again_button = customtkinter.CTkButton(text = 'Play Again!', command = self.play_again)
            self.play_again_button.grid(row=3,column=1)

    def right_wrong(self,is_correct):
        if is_correct == True:
            self.canvas.config(bg='green')
            self.trivia_brain.score +=1

        else:
            self.canvas.config(bg='red')
        self.root.after(1000, self.get_next_question)
    
        

    

    

        
            






        




        
        
        
        
