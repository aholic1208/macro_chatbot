#Doing nothing
task = 0

#kickstarter var oldline
oldline = ''

#Continuosly running app
while True:

    ###READ ME: Locate chatlog file (Please edit below to make it be directed to the chat logger file)
    fileHandle = open(r'C:\Users\HP\AppData\Roaming\MultiMC\instances\1.4.7 - CL.minecraft\chatlogs(Your chat log file name here)')

    #Read chatlog file
    lineList = fileHandle.readlines()

    #Read last line of chatlog file
    line = lineList[len(lineList)-1]

    #filtering out html codes from line
    filteredline = line.replace("</span>", "")
    filteredline = filteredline.replace("&lt;", "<")
    filteredline = filteredline.replace("&gt;", ">")
    filteredline = filteredline.replace('<span style="color: #0AA;">', "")
    filteredline = filteredline.replace('<span style="color: #AAA;">', "")
    filteredline = filteredline.replace('<code><span>', "")
    filteredline = filteredline.replace('</code><br>', "")
    filteredline = filteredline.replace('<span style="color: #FF5;">', "")
    filteredline = filteredline.replace('<span style="color: #FA0;">', "")

    #newline var
    newline = filteredline

    #test for changes
    if oldline == newline:
        task += 0
    elif oldline != newline:
        print(filteredline)
        oldline = newline