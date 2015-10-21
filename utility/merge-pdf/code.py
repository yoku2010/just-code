#!/usr/bin/python

# =============================
# Need to Install pypdf package
# =============================
# $ sudo pip install pypdf
#

from pyPdf import PdfFileWriter, PdfFileReader
 
def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]
 
output = PdfFileWriter()
append_pdf(PdfFileReader(file("pdf-sample-1.pdf","rb")),output)
append_pdf(PdfFileReader(file("pdf-sample-2.pdf","rb")),output)

output.write(file("pdf-sample-3.pdf","wb"))
