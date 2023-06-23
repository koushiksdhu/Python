# We have a list of names in the names.txt file. We have to insert that names into a letter.txt.
PLACEHOLDER = "[Name]"

with open("./Invitation/name_list/names.txt") as file:
    names = file.readlines()

for name in names:          # Iterating through the list, named as, names,
    n = name.strip()        # Removes nextline (\n) escape sequence character.
    with open(f"./Invitation/invitation_cards/{n} Invitation.txt", "w+") as file_write:
        with open("./Invitation/letter_format/letter.txt") as file_read:
            data = file_read.read()
            data = data.replace(PLACEHOLDER, n)
            file_write.write(data)
            
#   Current folder is always the root folder that is opened in the IDE. If you use relative path than your root folder opened in IDE is the current folder i.e., [ ./ ]

 

        

