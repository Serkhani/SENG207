# Text to Speech App 📰
### Introduction 🚩
The Text to Speech App is a Python application that allows users to convert any text entered into an input box into spoken words. The application utilizes the pyttsx3 library for text-to-speech conversion and the PySimpleGui library for designing the user interface.

The application's primary goal is to provide an audio-based interface for individuals with visual impairments or anyone who prefers to listen rather than read text.


### Installation 🖥️
To run the application, you will need to have Python 3.x installed on your computer. You can download it from the official [Python website](https://www.python.org/downloads/)

### Additionally, you will need to install the following libraries:
>* PySimpleGUI
>* pyttsx3  

You can install these libraries using pip. Open your command prompt or terminal and type the following commands:
``` powershell
pip install -r requirements
```
### Usage
To use the application, simply run the [executable](https://github.com/Serkhani/SENG207/blob/d9c0a64db0c13fd0dcc494b2dbb651d0c11cff38/Project%202/speechify/dist/speechify.exe) file  or run [speechify.py](https://github.com/Serkhani/SENG207/blob/d9c0a64db0c13fd0dcc494b2dbb651d0c11cff38/Project%202/speechify/speechify.py) file in your terminal using the following command:

``` shell
python speechify.py
```
This will open the app's interface, where you can type any text you want to generate a QR code for. 
> * Once the application is running
> * Enter any text into the input box
> * Click the <button>Speak</button>
> * The application will convert the text to speech.
Also  
> * To switch to a female voice, click on the Female radio button and same for male.

### Disclaimer 🚨  
If you click the <button>Speak</button> while textfield is empty a popup will appear to notify you that the textfield cannot be empty.
### Features
* Allows users to enter text into an input text box and convert it into spoken words by clicking the "Speak" button.
* Provides the ability to adjust the volume and speed of the spoken words.
* Allows users to switch between a male and female voice.
* Provides an error message if the input text box is empty.