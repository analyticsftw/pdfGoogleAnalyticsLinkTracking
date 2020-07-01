# pdfGoogleAnalyticsLinkTracking
 A set of scripts to extract hyperlinks in a PDF file and check for the presence of URL tracking tags, such as UTM parameters for Google Analytics

Make sure to install all dependencies (pdfx, pdfminer) and run pdf_workflow.py

This script can easily be adapted to handle multiple PDF files.

Do pay attention that in this method we run pdfx as a shell command - you may need to use another method to execute this link search.

Also, the output is still very much in list form but you can easily modify the script to suit your needs.
