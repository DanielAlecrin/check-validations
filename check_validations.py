import glob

directory = "/home/dalecrin/Documentos/Workspace/Agendamento/SL-AgendamentoCore/src/main/"
resourceDirectoryPortuguese = directory + "resources/i18n/validation/messages_pt.properties"
resourceDirectoryEnglish = directory + "resources/i18n/validation/messages_en.properties"
resourceDirectorySpanish = directory + "resources/i18n/validation/messages_es.properties"


validations = []
incorrectValidations = []
for filename in glob.iglob(directory + "**/*Event.java", recursive=True):

    f = open(filename, "r")
    if f.mode == "r":
        contents = f.read()
        # print(contents)

        for i in contents.splitlines():
            stringWithoutSpaces = i.strip()

            if "@" in stringWithoutSpaces and "message" in stringWithoutSpaces:
                stringWithoutSpaces = stringWithoutSpaces.replace("\"", "")
                stringWithoutSpaces = stringWithoutSpaces.split("{")
                stringWithoutSpaces = stringWithoutSpaces[1].split("}")
                # print(stringWithoutSpaces[0])

                validations.append(stringWithoutSpaces[0])

for filename in glob.iglob(directory + "**/*Dto.java", recursive=True):
    f = open(filename, "r")
    if f.mode == "r":
        contents = f.read()
        # print(contents)

        for i in contents.splitlines():
            stringWithoutSpaces = i.strip()

            if "@" in stringWithoutSpaces and "message" in stringWithoutSpaces:
                stringWithoutSpaces = stringWithoutSpaces.replace("\"", "")
                stringWithoutSpaces = stringWithoutSpaces.split("{")
                stringWithoutSpaces = stringWithoutSpaces[1].split("}")
                # print(stringWithoutSpaces[0])

                validations.append(stringWithoutSpaces[0])

for filename in glob.iglob(directory + "**/*DTO.java", recursive=True):
    f = open(filename, "r")
    if f.mode == "r":
        contents = f.read()
        # print(contents)

        for i in contents.splitlines():
            stringWithoutSpaces = i.strip()

            if "@" in stringWithoutSpaces and "message" in stringWithoutSpaces:
                stringWithoutSpaces = stringWithoutSpaces.replace("\"", "")
                stringWithoutSpaces = stringWithoutSpaces.split("{")
                stringWithoutSpaces = stringWithoutSpaces[1].split("}")
                # print(stringWithoutSpaces[0])

                validations.append(stringWithoutSpaces[0])


# for v in validations:
#     print(v)    
print("\n ###############")


f = open(resourceDirectoryPortuguese, "r")
if f.mode == "r":
    contents = f.read()
    lines = contents.splitlines()

    for valid in validations:
        isCorrect = False
        messageAndDetail = 0
        for line in lines:
            if valid in line:
                isCorrect = True
        
        if isCorrect == False:
            incorrectValidations.append(valid)

print("Incorrect validations em Portugues: "  + str(len(incorrectValidations)))
for incorrectValid in incorrectValidations:
    print(incorrectValid)

print("\n")

incorrectValidations = []
f = open(resourceDirectoryEnglish, "r")
if f.mode == "r":
    contents = f.read()
    lines = contents.splitlines()

    for valid in validations:
        isCorrect = False
        messageAndDetail = 0
        for line in lines:
            if valid in line:
                isCorrect = True
        
        if isCorrect == False:
            incorrectValidations.append(valid)

print("Incorrect validations em Ingles: "  + str(len(incorrectValidations)))
for incorrectValid in incorrectValidations:
    print(incorrectValid)

print("\n")

incorrectValidations = []
f = open(resourceDirectorySpanish, "r")
if f.mode == "r":
    contents = f.read()
    lines = contents.splitlines()

    for valid in validations:
        isCorrect = False
        messageAndDetail = 0
        for line in lines:
            if valid in line:
                isCorrect = True
        
        if isCorrect == False:
            incorrectValidations.append(valid)

print("Incorrect validations em Espanhol: "  + str(len(incorrectValidations)))
for incorrectValid in incorrectValidations:
    print(incorrectValid)

print("\n")