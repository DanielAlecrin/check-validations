import glob

directory = "/home/dalecrin/Documentos/Workspace/Agendamento/SL-AgendamentoCore/src/main/"
resourceDirectoryPortuguese = directory + "resources/i18n/validation/messages_pt.properties"
resourceDirectoryEnglish = directory + "resources/i18n/validation/messages_en.properties"
resourceDirectorySpanish = directory + "resources/i18n/validation/messages_es.properties"


def find_validations(resourceDirectory):
    validations = []

    for filename in glob.iglob(resourceDirectory, recursive=True):

        f = open(filename, "r")
        if f.mode == "r":
            contents = f.read()

            for i in contents.splitlines():
                stringWithoutSpaces = i.strip()

                if "@" in stringWithoutSpaces and "message" in stringWithoutSpaces:
                    stringWithoutSpaces = stringWithoutSpaces.replace("\"", "")
                    stringWithoutSpaces = stringWithoutSpaces.split("{")
                    stringWithoutSpaces = stringWithoutSpaces[1].split("}")

                    validations.append(stringWithoutSpaces[0])
    
    return validations

def inspect_validations_literals(resourceDirectory):
    incorrectValidations = []
    
    f = open(resourceDirectory, "r")
    if f.mode == "r":
        contents = f.read()
        lines = contents.splitlines()

        for valid in all_validations:
            isCorrect = False
            for line in lines:
                if valid in line:
                    isCorrect = True
                    break
            
            if isCorrect == False:
                incorrectValidations.append(valid)
    
    return incorrectValidations

all_validations = []

all_validations.extend(find_validations(directory + "**/*Event.java"))
all_validations.extend(find_validations(directory + "**/*Dto.java"))
all_validations.extend(find_validations(directory + "**/*DTO.java"))

print("#####################\n")
print("#####################\n")
print("ABAIXO ESTÃO AS VALIDATIONS QUE ESTÃO SEM AS LITERAIS NOS ARQUIVOS\n")
print("#####################\n")
print("#####################\n")

## Português
wrong_validations_pt = inspect_validations_literals(resourceDirectoryPortuguese)

print("Validations incorretas em Portugues: "  + str(len(wrong_validations_pt)))
for wrongVld in wrong_validations_pt:
    print(wrongVld)

print("\n")

## Espanhol
wrong_validations_es = inspect_validations_literals(resourceDirectorySpanish)

print("Validations incorretas em Espanhol: "  + str(len(wrong_validations_es)))
for wrongVld in wrong_validations_es:
    print(wrongVld)

print("\n")

## Ingles
wrong_validations_en = inspect_validations_literals(resourceDirectoryEnglish)

print("Validations incorretas em Ingles: "  + str(len(wrong_validations_en)))
for wrongVld in wrong_validations_en:
    print(wrongVld)

print("\n")