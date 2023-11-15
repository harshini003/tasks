#task 3 
#level 3
# importing the modules 
import PyPDF2 
import pyttsx3 
path = open("h:\cognifyz\level-3\automation repe\file.pdf" , 'rb')
pdfReader = PyPDF2.PdfFileReader(path) 
from_page = pdfReader.getPage(24) 
text = from_page.extractText() 
speak = pyttsx3.init() 
speak.say(text) 
speak.runAndWait()
