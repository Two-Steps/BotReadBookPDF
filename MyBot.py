import pyttsx3
from PyPDF2 import PdfFileReader

def speech(texts):
    ttsx = pyttsx3.init()
    ttsx.setProperty('rate', 150)
    voices = ttsx.getProperty('voices')
    ttsx.setProperty('voice', voices[1].id)
    ttsx.say(texts)
    ttsx.runAndWait()

def books(page_remember = 0):
    book = open("SE.pdf", 'rb')
    reader = PdfFileReader(book)
    number_of_pages = reader.numPages
    for page in range(page_remember,number_of_pages):
        try:
            f = open('note.txt','x')
            f.write(str(page + 1))
            f.close()
        except FileExistsError:
            # print('file note.txt is exist')
            f = open('note.txt','w')
            f.write(str(page + 1))
            f.close()
        page = reader.getPage(page)
        texts = page.extractText()
        speech(texts)
def remember_page():
    pr = -1
    try:
        r = open('note.txt','r')
        pr = int(r.read(1))
        # print(pr)
        r.close()
    except:
        pr = 0
    # print(pr) test file note.txt exist
    return pr
def main():
    speech('Welcome boss')
    t = remember_page()
    if t>0:
        print(f'You readed in page {t}, press "y" if you want to continue press "n" to read again')
        speech(f'You readed in page {str(t)}, press "y" if you want to continue press "n" to read again')
        type_read = str(input('enter your key in here: ')).lower()
        if 'y' in type_read:
            books(t)
        elif 'n' in type_read:
            books(0)
        else: 
            speech('you no choose any option so I shut down program, bye sir')
            quit()
    else:
        books(0)

if __name__ == "__main__":
    main()
