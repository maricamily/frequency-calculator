from tkinter import * 

class Application: 
    def __init__(self, master=None):
        self.firstContainer = Frame(master)
        self.firstContainer.pack()
        self.standardFont = ("Comic Sans", "10")
        self.msg = Label(self.firstContainer, text="Contador de faltas") # add the text to the top of the application
        self.msg.pack ()

        self.segundoContainer = Frame(master)
        self.segundoContainer.pack ()
        self.choice80 = Button(self.segundoContainer, text="80", width=10, command=self.button80) # creates a button for 80 of course load
        self.choice80.pack ()

        self.thirdContainer = Frame(master)
        self.thirdContainer.pack ()
        self.choice120 = Button(self.thirdContainer, text="120", width=10, command=self.button120) # creates a button for 120 of course load
        self.choice120.pack (pady=10)

        self.fourthContainer = Frame(master)
        self.labelAbsences = Label(self.fourthContainer, text="pai, devo faltar? (digite o n de faltas)")
        self.labelAbsences["font"] = self.standardFont
        self.absences = Entry(self.fourthContainer, width=30)
        self.absences["font"] = self.standardFont # here is the creation of the input so the user can tell how much absences he had, but it only appears if you click the button

    def inputAbsences(self):
        self.fourthContainer.pack(pady=10)
        self.labelAbsences.pack ()
        self.absences.pack () #makes the input box visible

    def button80(self):
        if self.msg["text"] == "Contador de faltas":
            self.inputAbsences ()
        else:
            self.msg["text"] = "botao 80" #here is the logic for course load of 80

    def button120(self):
        if self.msg["text"] == "Contador de faltas":
            self.inputAbsences ()
        else:
            self.msg["text"] = "botao 120" #here is the logic for course load of 120

root = Tk()
Application(root)
root.mainloop() #initiates the application