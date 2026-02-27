class TextOperation:
    def __init__(self, operationType, char=None):
        self.operationType = operationType
        self.char = char

class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []
    

    def add_char(self, char):
        self.text += char
        self.history.append(TextOperation("add",char))
        
        self.display()
    
    def delete(self):
        if not self.text:
            print("Nothing to delete")
            return
        
        removed = self.text[-1]
        self.text = self.text[:-1]
        self.history.append(TextOperation("delete", removed))
        self.display()

    def undo(self):
        if not self.history:
            print("Nothing to undo")
            return
        lastOperation = self.history.pop()

        # if the last operation == add
        if lastOperation.operationType == "add":
            # do the opposite
            self.text = self.text[:-1]


        
        elif lastOperation.operationType == "delete":
            self.text += lastOperation.char
        self.display()


    def display(self):
        print(f"Current text: '{self.text}'")

    

def run_editor():
    editor = TextEditor()
    print("\t~~~~~Welcome this is a simple text editor!~~~~~~~")
    print("\n\t***********Use these command:*************")
    print("\t \"add , <char>\" \t -> \t adds wanted character")
    print("\t \"delete\" \t -> \t deletes last character")
    print("\t \"undo\" \t -> \t undoes last command")
    print("\t\"quit\" \t -> \t to exit the program")


    running = True

    while running:
        command = input("\nEnter a char: ").lower().strip()
        if command.startswith("add"):
            char = command.split(" ")[1]
            if len(char) == 1:
                editor.add_char(char)
            else:
                print("Please only enter one character")
        
        elif command == "delete":
            editor.delete()
            
        elif command == "undo":
            editor.undo()

        elif command == "display":
            editor.display()
        
        elif command == "quit" or command == "exit" :
            print("Exiting...")
            running = False
        
        else:
            print ("unkown command")

if __name__ == "__main__":
    run_editor()