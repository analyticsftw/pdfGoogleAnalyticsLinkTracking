# Processes a PDF file, extracts hyperlinks and look for presence/absence of URL tracking parameters
# Julien Coquet, June 2020

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def run(cmdline):
    subprocess.run([cmdline],  check=True, cwd="./", shell=True)


def main():
    # Install missing modules
    install("pdfx")
    install("pdfminer2")

    # define source PDF file and
    sourceFile = "basic.pdf"
    outputFile = "urls_pdf.txt"

    # Runs pdfx as shell, extracts link URLs found in the source PDF file
    # and stores the output to a text file
    run("pdfx " + sourceFile + " -v > " + outputFile)

    # Open the output textfile
    file = open('urls_pdf.txt', mode='r')
    lines = file.readlines()
    file.close()

    tagged = []
    untagged = []
    i = 0

    # Go through lines in file until we reach the URL References section
    for line in lines:
        i = i + 1
        boundary = "URL References:"
        if boundary in line:
            found = i
        # Trim URLs and separate in different lists according to presence of UTM tags
        if -1 < line.find("http"):
            link = line[2:].rstrip()
            if link.find("utm_") > 0:
                tagged.append(link)
            else:
                untagged.append(link)

    # Output results
    print("Tagged: %s/%s" % (str(len(tagged)), i - found)  )
    print(tagged)
    print("Untagged: %s/%s" % (str(len(untagged)), i - found)  )
    print(untagged)


if __name__ == "__main__":
    # calling the main function
    main()
