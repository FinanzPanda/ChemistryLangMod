import os

folder ="C:/Users/Karl-Theodor/Documents/Github/ChemistryLangMod/PythonDataGen"
filepath= folder+"/recipes/e"

filepathChemName= folder + "/chemNameFoleder"
OutputrecepiesFolder= folder + "/outputRecepies"

TestRecips = folder + "/testRecips"

Limit= 10000
Count=0

ItemFInder= "item"
tagFInder= "tag"

NewNames =[]


# -------- func ---------

def ItemNameFinder(Line: str):
    ItemList = Line.split(":")[2][:-1]
    return ItemList

def LangSplitter(ItemName: str):
    filepathItemLang = filepathChemName+"/"+ItemName+".txt"
    filepathItemRecepie = OutputrecepiesFolder +"/" + ItemName+".txt"
    try:
        file = open(filepathItemLang, "r", encoding="utf-8")
        LangName= file.readline()
        file.close
        RetunValue = LangName.split(":")[1][2:-2]
        return RetunValue
    except:
        try:
            file = open(filepathItemRecepie, "r", encoding="utf-8")
            LangName= file.readline()
            file.close
            RetunValue = LangName.split(":")[1][2:-2]
            return RetunValue
        except:
            print("no such file")
            return None

def WriteItemToDictionary(Item:str):
    ItemNameParts = Item.split(":")
    path = OutputrecepiesFolder + "/"+ItemNameParts[0] + ".txt"
    fileTestPath = TestRecips + "/"+ItemNameParts[0] + ".txt"
    
    NewLang = ItemNameParts[1]
    try:
        file = open(path, "r", encoding="utf-8")
        Content = file.readline()
        file.close()

        LangParts = Content.split(":")
        
        NewLangFileContent = LangParts[0] + ": \"" + NewLang +"\","
    
        file = open(path, "w", encoding="utf-8")
        file.write(NewLangFileContent)
        file.close()
        
    except:
        DummyLang="\"block.minecraft."+ItemNameParts[0]+"\": \"" + NewLang + "\","
        file = open(path, "w", encoding="utf-8")
        file.write(DummyLang)
        file.close()



# -------- loop ---------

for file in os.scandir(filepath):
    if not file.is_file():
        continue

    if Count > Limit:
        break

    with open (file.path, "r") as recipe:
        Content= [line.strip() for line in recipe.readlines()]

        NewName=""

        for line in Content:
            if not ItemFInder in line:
                continue
            ItemName= ItemNameFinder(line)
            ComponentName= LangSplitter(ItemName)
            if ComponentName == None: continue

            if NewName == "": NewName+= ComponentName
            else:  NewName+= " + "+ ComponentName

        if NewName =="": continue

        NewNames.append(file.name[:-5] + ":" + NewName)
            

    Count+=1



for Item in NewNames:
    WriteItemToDictionary(Item)