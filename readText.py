import urllib.request

def readText():
    file = open("/users/richard/downloads/movie_quotes.txt")
    fileContents = file.read()
    print(fileContents)
    file.close()
    checkProfanity(fileContents)

def checkProfanity(textToCheck):
    query = urllib.parse.urlencode({'q': textToCheck})
    conn = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+query)
    output = conn.read()
    print(output)
    conn.close()

readText()
