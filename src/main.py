from pptx import Presentation
import os
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def translate_text(text, output_language):
    return text + output_language

def translate_ppt(input_ppt, output_ppt, output_language):
    pass

# TODO: 1. copy each slide to new ppt 
# TODO: 2. extract text run with properties 
# TODO: 3. translate them 
# TODO: 4. replace previous run with translated

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    input_ppt = os.path.join(dir_path, '../inputs/test.pptx') 
    output_language = 'en'
    output_ppt = os.path.join(dir_path, '../outputs/', os.path.splitext(input_ppt)[0] + '_translate.pptx') 
    
    translate_ppt(input_ppt, output_ppt, output_language)
    print("Translation process completed successfully.")

if __name__ == "__main__":
    main()

