import sys
import os
from time import sleep

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract as pyt

class Image_Processing:

    def __init__(self, *args):

        ''' This uses pytesseract to transform png to text.
            In order to transform pdfs to images use 'pfd2imagelibrary'
        '''

        self.user = os.path.expanduser('~')
        sleep(3)
        print('The general path is : {}'.format(self.user))
        self.cwd =  os.path.join(self.user, *args) # no necesity to put raw strings here

        sleep(3)
        print('The working path will be : {}'.format(self.cwd))
        sleep(3)
    def define_path(self):

        '''Setting the path to the parent directory.
            Note that this will only work if files are placed in the users folder
            from main disk unit.
        '''

        sys.path.append(self.cwd)
        os.chdir(self.cwd)
        print ('The current working directory is : {}'.format(os.getcwd()))

    def image_to_text(self,image_path, text_path, language = 'eng'):

        ''' This is the method that transform the image into text
            and saves it to disk. it is important to note that the
            text_path and image_path are relative paths starting
            from the predefines current working directory
        '''

        self.img = Image.open(image_path)
        self.text = pyt.image_to_string(self.img, lang =language)

        with open (os.path.join(self.cwd, text_path), 'w') as text_file:
            text_file.write(self.text)

    def read_image_to_text(self, text_abs_path):

        with open(os.path.join(os.getcwd(),text_abs_path), 'rt') as f:
            self.text = f.read()
        print(self.text)

if __name__ == '__main__':
    Png = Image_Processing('Desktop', 'TA_Mac', 'Img_pross') # an imput could be added here :)
    Png.define_path()
    Png.image_to_text(r'Data/out_pic','Data/textocr.txt')
    Png.read_image_to_text('Data/textocr.txt')
