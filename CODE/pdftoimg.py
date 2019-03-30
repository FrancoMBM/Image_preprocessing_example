
# first: brew install freetype imagemagick, brew install ghostscript
# brew install popler after installing xcode on macOS
import os
import sys
from pdf2image import convert_from_path

class Convert:

    def set_path(self, path_to_data_folder):

        ''' Setting the path to the desired data folder '''

        os.chdir(path_to_data_folder)
        self.working_path = os.getcwd()

        return self.working_path



    def convert(self, pdf_name, pixels, image, image_ext):

        '''This method transforms a pdf into an image'''
        try:

            pages = convert_from_path(os.path.join(self.working_path, pdf_name), pixels)

            for page in pages:
                page.save(os.path.join(self.working_path, image), image_ext)
        except:

            print('There is no pdf file. Please Provide one')

if __name__ == '__main__':

    #conv = convert()
    cwd = os.getcwd()
    #print(cwd)

    conv = Convert()
    conv.set_path('/Users/franco/Desktop/TA_Mac/Img_pross/Data')
    conv.convert('sample1.pdf', 700, 'out_pic', 'PNG')
