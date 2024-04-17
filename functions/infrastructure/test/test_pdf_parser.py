import unittest
from io import BytesIO
from functions.application.parser.iparser import ParsingResult, DocumentImage
from functions.infrastructure.parser.pdf_parser import PDFParser

class PdfParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = PDFParser()

    def test_parse(self):
        file = BytesIO(b"%PDF-1.0\n\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n\n3 0 obj\n<< /Type /Page /Parent 2 0 R /Resources << >> /MediaBox [0 0 200 200] >>\nendobj\n\nxref\n0 4\n0000000000 65535 f \n0000000010 00000 n \n0000000053 00000 n \n0000000118 00000 n \ntrailer\n<< /Size 4 /Root 1 0 R >>\nstartxref\n147\n%%EOF")

        result = self.parser.parse(file)

        self.assertIsInstance(result, ParsingResult)
        self.assertIsInstance(result.text, str)
        self.assertIsInstance(result.images, tuple)

if __name__ == "__main__":
    unittest.main()