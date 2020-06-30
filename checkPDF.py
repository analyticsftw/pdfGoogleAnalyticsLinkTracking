# Inspiration https://www.geeksforgeeks.org/working-with-pdf-files-in-python/

# Import modules
import pdfquery


def main():
    pdf = pdfquery.PDFQuery("basic.pdf")
    pdf.load()
    print(pdf)

if __name__ == "__main__":
    # calling the main function
    main()
