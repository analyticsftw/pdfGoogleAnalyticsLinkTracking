# Processes a PDF file, extracts hyperlinks and look for presence/absence of URL tracking parameters
# Julien Coquet, June 2020

import os, subprocess, sys
import os.path

# Required packages
import pdfx, pdfminer2


def run(cmdline):
    subprocess.run([cmdline],  check=True, cwd="./", shell=True)


def main():
    # check for filename argument
    nargs = len(sys.argv)
    if nargs < 2:
        print ("Argument missing: filename.\nTry again with: python3 pdf_workflow.py yourfile.pdf")
        exit()
    


    # define source PDF file and
    sourceFile = sys.argv[1]
    if not os.path.isfile(sourceFile):
        print ('File ' + sourceFile + ' is missing.')
        exit()
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
