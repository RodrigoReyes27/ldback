from application.parser import IParser, ParsingResult
from PyPDF2 import PdfReader
from io import BytesIO

class PDFParser(IParser):
   def parse(self, file: BytesIO) -> ParsingResult:
        # Initialize a PDF file reader
        pdf = PdfReader(file)
        
        # Initialize the text and images list
        paragraphs = []
        images = []
        
        # Extract text from each page
        for page in range(len(pdf.pages)):
            page_text = pdf.pages[page].extract_text()

            lines = page_text.split('\n')

            
            paragraph = ""

            for line in lines:
                if line.strip() != "":
                    paragraph += " " + line.strip()
                elif paragraph != "":
                    paragraphs.append(paragraph.strip())
                    paragraph = ""
            if paragraph != "":
                paragraphs.append(paragraph.strip())
            
        # TODO: Extract images from the PDF file
        # This part is a bit more complex as it depends on the structure of your PDF file
        # You might need to use a library like PDFMiner or PyMuPDF if PyPDF2 doesn't work
        
        return ParsingResult(text=paragraphs, images=None)
