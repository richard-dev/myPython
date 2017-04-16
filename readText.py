import urllib.request

def readText():
    file = open("/users/richard/downloads/movie_quotes.txt")
    fileContents = file.read()
    print(fileContents)
    file.close()
    checkProfanity(fileContents)

def checkProfanity(textToCheck):
    query = urllib.parse.urlencode({'q': textToCheck})
    print("\n\n" + query + "\n\n")
    conn = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+query)
    output = conn.read().decode("utf-8")
    print("\n" + output + "\n\n")
    conn.close()

    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan document properly.")

readText()