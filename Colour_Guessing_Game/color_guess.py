import random
import tkinter as tk
import time
root = tk.Tk()
root.configure(bg="#555555")
root.wm_minsize(700,550)
root.wm_maxsize(700,550)
root.wm_title("Color Guessing")
class game():
    def __init__(self):
        self.sec = 20
        self.score = 0
        self.colors = ['Red' , 'Green' , 'Blue' , 'Yellow' , 'Orange']
        self. pc_choice =self.colors[random.randint(3,4)]
        self.pc_text = self.colors[random.randint(0,2)]
        self.main_frame = tk.Frame(root)
        self.main_frame.config(bg="#555555")
        self.colors_label = tk.Label(self.main_frame,bg="#333333",fg="white",\
                            text="COLORS  :  Red , Green , Blue , Yellow , Orange",\
                            height = 2,\
                            font = ('Courier',15,'bold'))
        self.colors_label.pack(pady = 10,fill=tk.X)
        self.time_label = tk.Label(self.main_frame,text = "Time remaining : 20",font=('Times',15))
        self.time_label.pack(pady=18)
        self.guesslabel = tk.Label(self.main_frame,bg="#555555",fg = self.pc_choice,\
                               text=self.pc_text,\
                               font = ('Times',30,'bold'),\
                               width =15)
        self.guesslabel.pack(pady=15)
        self.score_label = tk.Label(self.main_frame,fg="white",bg="#555555",\
                                text = "Your Score : 0",\
                                font=('Times',15,'italic'))
        self.score_label.pack(pady=25)
        self.choice_label = tk.Label(self.main_frame,fg="white",bg="#555555",\
                                text = "Enter your choice below :",
                                font=('Times',15,'bold'))
        self.choice_label.pack(pady=5)
        self.user_choice = tk.Entry(self.main_frame,fg="black",bg="white",width=20,font=('Times',25,'bold'))
        self.user_choice.bind("<Return>",self.score_update)
        self.user_choice.focus()
        self.user_choice.pack()
        self.exit_button = tk.Button(self.main_frame,text="Exit",\
                                 width=10,\
                                 bg="#aaaaaa",\
                                 fg = "black",\
                                 font = ('Times',15,'bold'))
        self.exit_button.config(relief="raised",)
        self.exit_button.pack(pady=50)
        self.exit_button.bind("<ButtonRelease-1>",self.destroy)
        self.play_again = tk.Button(self.main_frame,text="Play Again",\
                                 width=10,\
                                 bg="#aaaaaa",\
                                 fg = "black",\
                                 font = ('Times',15,'bold'))
        self.play_again.bind("<ButtonRelease-1>",self.repeat)
        self.main_frame.pack()
        
    def time_remain(self):  
        global sec
        self.time_label.config(text=f"Time remaining : {self.sec} sec.")
        #print(self.sec)
        self.sec -=1
        if self.sec == -1:
            self.time_label.destroy()
            self.guesslabel.destroy()
            #self.score_label.destroy()
            self.choice_label.destroy()
            self.user_choice.destroy()
            self.exit_button.destroy()
            self.exit_button = tk.Button(self.main_frame,text="Exit",\
                                 width=10,\
                                 bg="#aaaaaa",\
                                 fg = "black",\
                                 font = ('Times',15,'bold'))
            self.exit_button.config(relief="raised",)
            self.exit_button.bind("<ButtonRelease-1>",self.destroy)
            self.play_again.pack(pady=20)
            self.exit_button.pack()
        else:
            time.sleep(1)
            root.after(1000,self.time_remain)
        
    def destroy(self,e):
        root.destroy()
    
    def score_update(self,e):
        if self.pc_choice.lower() == (self.user_choice.get()).lower():
            self.score += 1
            #print(score)
            self.score_label.config(text=f"Your Score : {self.score}")
            self.user_choice.delete(0, 'end')
            self.next_guess()
        else:
            self.user_choice.delete(0, 'end')
            self.next_guess()
        
    def next_guess(self):
        self.pc_choice = self.colors[random.randint(0,4)]
        self.pc_text = self.colors[random.randint(0,4)]
        #print(self.pc_choice,self.pc_text,1)
        while(self.pc_text == self.pc_choice):
            #print("In while")
            #print(self.pc_choice , self.colors[random.randint(0,4)],2)
            self.pc_choice = self.colors[random.randint(0,4)]
            self.pc_text == self.colors[random.randint(0,4)]
        #print("After While")
        #print(self.pc_choice , self.pc_text,3)
        self.guesslabel.config(fg = self.pc_choice , text = self.pc_text)
    
    def repeat(self,e):
        self.main_frame.destroy()
        self.__del__()
        obj = game()
        obj.time_remain()
        
        
    def __del__(self):
        pass

def start(e):
    game_name.destroy()
    inst_label.destroy()
    start_button.destroy()
    obj = game()
    obj.time_remain()

instructions = """** HOW TO PLAY **

1.Quickly distinguish between the color 
name and the actual color 
present in the word shown.

2.If you guessed the right color,you will
 get 1 point.

3.Colors : Red,Green,Blue,Yellow,Orange  

4.Time Limit : 20 sec.
"""
game_name = tk.Label(root,\
                    text="Color Guessing",\
                    font=('courier',25,'italic','bold'),\
                    fg="#eeeeee",bg="#333333",height=2)
game_name.pack(fill=tk.X)

inst_label = tk.Label(root,\
                    text=instructions,\
                    font=('courier',15,'italic'),\
                    fg="#000000",bg="#999999",\
                    height = 14)
inst_label.pack(padx=5,pady=30,fill=tk.X)

start_button = tk.Button(root,text="Start",\
                         width=15,\
                         bg="#aaaaaa",\
                         fg = "black",\
                         font = ('Times',15,'bold'))
start_button.config(relief="raised",)
start_button.pack(pady=15)
start_button.bind("<ButtonRelease-1>",start)
root.mainloop()