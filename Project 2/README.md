# Project-2: Speechify and QR Code Generator Applications 📰
This project aims to develop two practical desktop applications utilizing Python programming language.

## Speechify App
The [Text-to-Speech](https://github.com/Serkhani/SENG207/blob/d9c0a64db0c13fd0dcc494b2dbb651d0c11cff38/Project%202/speechify/dist/speechify.exe) application provides a user interface for converting text into spoken words. The user can enter text into an input text box and select the "Speak" button. The application will then utilize the pyttsx3 text-to-speech library to convert the text into audio.

The application allows the user to adjust the volume or speed of the spoken words. Additionally, an advanced feature of this application is to switch between a male or female voice. The application's user interface is designed using the PySimpleGui library.
![Speechify](https://github.com/Serkhani/SENG207/blob/007adb0bf72b07bc73243d8d3c3688b1251bb6c1/repo_resources/speechify_snip.JPG)

## QR Code Generator App
The [QR Code Generator](https://github.com/Serkhani/SENG207/blob/d9c0a64db0c13fd0dcc494b2dbb651d0c11cff38/Project%202/qrcodegen/dist/qrcodegen.exe) application provides a user interface for generating QR codes from any text input. The user can enter text into an input text box and select the "Create" button. The application will then utilize the qrcode library to generate a QR code image from the entered text.

The application allows the user to customize the size and color of the generated QR code image. Additionally, error handling is included in case the input text is invalid or if there are any issues with the QR code generation process. The application's user interface is designed using the PySimpleGui library.  
![QRCodeGen](https://github.com/Serkhani/SENG207/blob/f5b4368e97b2b47c527d8866f6b4b3bb67ff6e2c/repo_resources/qrcode_snip.JPG)

## Conversion to Executable Application
As part of the project submission, the Python code for both applications is converted into an executable application using the [PyInstaller](https://pyinstaller.org/en/stable/) library. The packaged executable can be distributed to others without requiring them to have Python or any specific libraries installed.

To use [PyInstaller](https://pyinstaller.org/en/stable/) to make these PySimpleGui applications executable, the following steps were taken:

* Installed [PyInstaller](https://pyinstaller.org/en/stable/) by running the command: ```pip install pyinstaller``` in the terminal or command prompt.
* Navigated to the directory containing the Python script and any additional resources or dependencies that the applications require.
* Ran the [PyInstaller](https://pyinstaller.org/en/stable/) command in the terminal or command prompt, using the command ```pyinstaller --onefile app.py``` where `app.py` is the name of the Python file.
* Waited for the packaging process to complete. [PyInstaller](https://pyinstaller.org/en/stable/) created a `dist` directory containing the packaged executable.
* Tested the executable by navigating to the `dist` directory and running the packaged executable. Both [PySimpleGui](https://www.pysimplegui.org/en/latest/) applications ran as expected.

## Disclaimer 🚨
Note that additional configuration options or dependencies may need to be included in the [PyInstaller](https://pyinstaller.org/en/stable/) command, depending on the specifics of the [PySimpleGui](https://www.pysimplegui.org/en/latest/) applications. The [PyInstaller](https://pyinstaller.org/en/stable/) documentation provides more information on how to customize the packaging process to suit specific needs.