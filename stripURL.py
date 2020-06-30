file = open('urls_pdf.txt', mode = 'r')
lines = file.readlines()
file.close()
my_dict = {}
my_list = []
tagged = []
untagged = []
i = 0
found = 0
for line in lines:
    i = i + 1
    boundary = "URL References:"
    if boundary in line:
        found = 1
    if -1 < line.find("http"):
        link = line[2:].rstrip()
        if link.find("utm_")>0:
            tagged.append(link)
        else:
            untagged.append(link)
print("Tagged")
print(tagged)
print("Untagged")
print(untagged)
