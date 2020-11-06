import pyttsx3
import PyPDF2

book = open('win.pdf', 'rb')

reader = PyPDF2.PdfFileReader(book)

pages = reader.numPages

print(pages)

speaker = pyttsx3.init()

for num in range(12, pages):
    page = reader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
