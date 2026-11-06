import os

folder ="C:/Users/Karl-Theodor/Documents/Github/ChemistryLangMod/PythonDataGen"
filepathLang= folder + "/lang/ch_ch.json"
filepathRecip= folder + "/recipes/e"

filepathChemName= folder + "/chemNameFoleder"
folderPathCraftBle= folder + "/outputRecepies"

OutputNOTCraftable=folder+"/NOTCraftble.txt"
OutputCraftable=folder+"/Craftble.txt"


Step= 100
Count=0

ItemFInder= "item"
tagFInder= "tag"

langNames=[]
Recepies=[]

NotCraftable=[]

Craftable=[]

# func

def RecipiesCheckItem(Item, RecepieList):
    for Recipe in RecepieList:
        if Recipe == Item: return True
    return False

def ItemNameSpliter(Item):
    ItemList = Item.split(".")         
    if not len(ItemList)==3:
        return None
    Name= ItemList[2].split(":")[0][:-1]
    return Name

def WriteNoCraftsToDictionary(ItemList: list, path:str):
    for Item in ItemList:
        Name = ItemNameSpliter(Item)
        print(Item+" Output: "+ Name)
        if Name != None:
            FilePath = path + "/"+ Name+".txt"
        file = open(FilePath,"w", encoding="utf-8")
        file.write(Item)
        file.close


# File reader

with open (filepathLang, "r", encoding="utf-8") as file:
    langNames= [line.strip() for line in file.readlines()]

for file in os.scandir(filepathRecip):
    
    if not file.is_file():
        continue

    Recepies.append(file.name.split(".")[0])


# Analyse Data

for Name in langNames:
    if Count%Step == 0:
        print(Count)

    if not ":" in Name:
        if Name == langNames[-1]:
            break
        continue
    else:

        ItemList = Name.split(".")
        
        if not len(ItemList)==3:
            continue

        Item= ItemList[2].split(":")[0][:-1]
        if RecipiesCheckItem(Item, Recepies): 
            Craftable.append(Name)
            continue

        NotCraftable.append(Name)


    Count+=1

#Save Data

INPUT=input("1/2/3: ")

if INPUT=="1":
    with open(OutputNOTCraftable, "w", encoding="utf-8") as file:
        file.writelines([item +"\n" for item in NotCraftable])

    with open(OutputCraftable, "w", encoding="utf-8") as file:
        file.writelines([item +"\n" for item in Craftable])

elif INPUT=="2":
    WriteNoCraftsToDictionary(NotCraftable, filepathChemName)

elif INPUT=="3":
    WriteNoCraftsToDictionary(Craftable, folderPathCraftBle)