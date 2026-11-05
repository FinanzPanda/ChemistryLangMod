import os

folder ="C:/Users/Karl-Theodor/Documents/Github/ChemistryLangMod/PythonDataGen"
filepathLang= folder + "/lang/ch_ch.json"
filepathRecip= folder + "/recipes/e"


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

with open(OutputNOTCraftable, "w", encoding="utf-8") as file:
    file.writelines([item +"\n" for item in NotCraftable])

with open(OutputCraftable, "w", encoding="utf-8") as file:
    file.writelines([item +"\n" for item in Craftable])
