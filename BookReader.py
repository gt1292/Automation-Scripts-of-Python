import pyttsx3
import PyPDF2

book = open('Law of Attraction.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage()
text = page.extract_text()
speaker.say(text)
speaker.runAndWait() 