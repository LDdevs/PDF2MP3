import pyttsx3
import PyPDF2

# Insert name of your PDF
with open('Syllabus_Lisa Downie.pdf', 'rb') as file:
    pdfreader = PyPDF2.PdfReader(file)
    speaker = pyttsx3.init()

    text = ""
    for page_num in range(len(pdfreader.pages)):
        text += pdfreader.pages[page_num].extract_text()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)

    # Name the MP3 file whatever you like
    speaker.save_to_file(clean_text, 'syllabus.mp3')
    speaker.runAndWait()

speaker.stop()