import csv
from pptx import Presentation
from pptx.util import Inches

class FlashcardPPT:
    def __init__(self):
        self.presentation = Presentation()

    def add_flashcard(self, statement, definition):
        slide = self.presentation.slides.add_slide(self.presentation.slide_layouts[5])  # Use a blank slide layout

        # Add statement text
        statement_textbox = slide.shapes.add_textbox(left=Inches(1), top=Inches(1), width=Inches(4), height=Inches(1))
        statement_frame = statement_textbox.text_frame
        statement_frame.text = "Statement: {}".format(statement)
        
        slide = self.presentation.slides.add_slide(self.presentation.slide_layouts[5])  # Use a blank slide layout

        # Add definition text
        definition_textbox = slide.shapes.add_textbox(left=Inches(1), top=Inches(3), width=Inches(4), height=Inches(2))
        definition_frame = definition_textbox.text_frame
        definition_frame.text = "Definition: {}".format(definition)

def create_flashcards(input_csv, output_pptx):
    # Read data from CSV
    with open(input_csv, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Create PowerPoint presentation
    ppt = FlashcardPPT()

    # Loop through data and add flash cards to PowerPoint
    for entry in data:
        statement = entry['ï»¿statement']
        definition = entry['definition']
        ppt.add_flashcard(statement, definition)

    # Save the PowerPoint presentation to a file
    ppt.presentation.save(output_pptx)

if __name__ == "__main__":
    input_csv = "flashcards.csv"
    output_pptx = "flashcards.pptx"

    create_flashcards(input_csv, output_pptx)
    print(f"Flashcards generated and saved to {output_pptx}")
