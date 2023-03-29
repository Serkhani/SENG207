from PySimpleGUI import Window, Input, Button, Column, Image, popup, WIN_CLOSED, Combo, Text
import io, qrcode


class MainWindow(Window):
    def __init__(self) -> None:
        # Define the window's contents
        self.layout = [
            [Input()],     # Part 2 - The Layout
            [Button('Create')],
            [Column([[Image(key='-QR-')]], size=(300, 300), justification='center')],
            [Text('fill color: '), Combo(['Black', 'White', 'Red', 'Green', 'Blue'], key='-FILL-', default_value='Black')],
            [Text('back color: '), Combo(['White', 'Black', 'Red', 'Green', 'Blue'], key='-BACK-', default_value='White')],
    
        ]
        # initialize the Window class
        super().__init__('QR Code Generator', self.layout)
    
    def genCode(self, data, fill_color, back_color):
        "generates the qr code"
        qr = qrcode.QRCode(version=1, box_size=7, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        self.img = qr.make_image(fill_color=fill_color, back_color=back_color)
        self.showCode()

    def showCode(self):
        "shows the qr code that has been generated"      
        with io.BytesIO() as buffer:
        # Save the image data to a bytes buffer
            self.img.save(buffer, format='PNG')
            img_bytes = buffer.getvalue()
            self['-QR-'].update(data=img_bytes)
    
    def removeCode(self):
        "removes the qr code from the container"
        self['-QR-'].update(data=b'')


if __name__ == '__main__':
    # Create the window
    window = MainWindow()
    while True:
        # Interact with the Window
        event, values = window.read()
        if event == WIN_CLOSED or event == 'Exit':
            # Finish up by removing from the screen
            window.close()
            # break from the loop and end the program
            break
        elif values[0]:
            # generate the qr code
            window.genCode(values[0], values['-FILL-'], values['-BACK-'])
        else: 
            # popup to notify the user of an empty textfield
            popup("Error", "Textfield cannot be empty") 
            window.removeCode()