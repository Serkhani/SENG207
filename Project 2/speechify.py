from PySimpleGUI import Window, Text, Input, Button, Radio, popup, WIN_CLOSED
import pyttsx3


class MainWindow(Window):
    def __init__(self) -> None:
        # Define the window's contents
        self.layout = [
            [Input(), Button('Speak')],     # Part 2 - The Layout
            [Text("Select Voice Type"), Radio("Male", "voice", True,), Radio("Female", "voice")]]
        super().__init__('Speechify', self.layout)
        # initialize the engine
        self.engine = pyttsx3.init()
        # get and save the voices
        self.voices = self.engine.getProperty('voices')

    # check if the male radio is activated
    def voiceCheck(self, val):
        if val:
            self.engine.setProperty('voice', self.voices[1].id)
        else:
            self.engine.setProperty('voice', self.voices[0].id)
    # speak the contents of the textfield
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    


if __name__ == '__main__':
    # Create the window
    window = MainWindow()
    while True:
        # Interact with the Window
        event, values = window.read()
        if event == WIN_CLOSED:
            # Finish up by removing from the screen
            window.close()
            # break from the loop and end the program
            break
        elif values[0]:
            # check if the user has changed the gender of the speaker
            window.voiceCheck(values[1])
            # Do something with the information gathered
            window.speak(values[0])
        else: 
            # popup to notify the user of an empty textfield
            popup("Textfield must be filled", "Error") 
            
        

    
