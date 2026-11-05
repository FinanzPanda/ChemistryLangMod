import os

folder ="C:/Users/Karl-Theodor/Documents/Github/ChemistryLangMod/PythonDataGen"
filepath= folder+"/recipes/e"

Limit= 10
Count=0

ItemFInder= "item"
tagFInder= "tag"

for file in os.scandir(filepath):
    if not file.is_file():
        continue

    if Count > Limit:
        break

    with open (file.path, "r") as recipe:
        Content= [line.strip() for line in recipe.readlines()]
        for line in Content:
            if ItemFInder in line:
                print(line)

    Count+=1