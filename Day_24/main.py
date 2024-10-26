#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Letters/starting_letter.txt",mode="r") as letter:
    starting_letter = letter.read()

with open("Input/Names/invited_names.txt",mode="r") as invites:
    invited_names = invites.readlines()


with open("Output/ReadyToSend/example.txt",mode="w") as Ready:
    for invited_name in invited_names:
        Ready.write(starting_letter.replace("[name]",invited_name.strip()))
        Ready.write("\n")