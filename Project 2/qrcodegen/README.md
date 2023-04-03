# QR Code Generator App 📰
This is a simple application that generates QR codes from any text input. The app's interface is designed with the user in mind and is easy to use.

![QRCodeGen](https://github.com/Serkhani/SENG207/blob/f5b4368e97b2b47c527d8866f6b4b3bb67ff6e2c/repo_resources/qrcode_snip.JPG)

### Installation 🖥️
To run the application, you will need to have Python 3.x installed on your computer. You can download it from the official [Python website](https://www.python.org/downloads/)

### Additionally, you will need to install the following libraries:
>* PySimpleGUI
>* qrcode  

You can install these libraries using pip. Open your command prompt or terminal and type the following commands:
``` powershell
pip install -r requirements
```
### Usage
To use the application, simply run the [executable](https://github.com/Serkhani/SENG207/blob/d9c0a64db0c13fd0dcc494b2dbb651d0c11cff38/Project%202/qrcodegen/dist/qrcodegen.exe) file  or run [qrcodegen.py](https://github.com/Serkhani/SENG207/blob/d9c0a64db0c13fd0dcc494b2dbb651d0c11cff38/Project%202/qrcodegen/qrcodegen.py) file in your terminal using the following command:

``` shell
python qrcodegen.py
```
This will open the app's interface, where you can type any text you want to generate a QR code for. 
> * Once you have entered the text, click the <button> Create</button>
to generate the QR code. The QR code will appear in the container below it.
> * You can customize the size and color of the generated QR code by selecting the fill color and back color from the dropdown menus.

### Disclaimer 🚨  
If you enter an empty textfield and click the "Create" button, a popup will appear to notify you that the textfield cannot be empty.

### Features
* Generate QR codes from any text input
* Customize the size and color of the generated QR code
* Error handling for empty textfields
* Easy-to-use interface