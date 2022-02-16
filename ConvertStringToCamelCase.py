
def to_camel_case(text):
    if text == "":
        return text  
    else:
        firstLetter = text[0]
        for x in range(len(text)):
            if not text[x].isalpha():
                text = text.replace(text[x]," ")
        newText = text
        newText = newText.title()
        for x in range(len(newText)):
                if not newText[x].isalpha():
                    newerText = newText.replace(newText[x],"")
            
        newerText = newerText.replace(newerText[0],firstLetter)
        print (newerText)

to_camel_case("Convert string to camel case")


