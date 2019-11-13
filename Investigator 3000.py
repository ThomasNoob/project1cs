#Opens window: 
#Displays rules of the game for investigation
#Simple shapes on the grid represents furniture and objects
#Uses get mouse when user clicks on an object,
#When a user clicks on an object new window will display showing a description and evidence number. This is what the user needs to remember 
#When user believes he has found all the evidence he must enter the correct object to the correct evidence number. If all is done correctly player moves on to the investigation round 
#Player is met with 3 suspects, he can question them on evidence and what they did during the crime, player only has so much “time” is only allowed to ask 3 questions per suspect.
#At the end the player may enter the name of the suspect he thinks did the crime
#If he is correct. He wins (display window of whether you won or lost)

#Suspects: Bobby big nose, slippery Sam, beautiful Paul 
#Display “what should I ask about?” Evidence numbers or events and relationship to the suspect, or they can intimidate, charm, or leverage.

#5 pieces of evidence 


print("\n Evidence must be filed. please enter evidence codex name.")
e1 = input("\n Evidence #1")
if e1 == ("knife"):
    e2 = input("\n Evidence #2")
    if e2 == ("picture"):
        e3 = input("\n Evidence #3")
        if e3 == ("hair"):
            e4 = input("\n Evidence #4")
            if e4 == ("note"):
                e5 = input("\n Evidence #5")
                if e5 == ("card"):
                    print("\n Private Jenkins: Got all the evidence filed? I hope you wrote it down, we got some suspects for questioning. We...cant bring them in on any charges so its likely theyll walk out after 3 questions. Thats their right though")

print("\n Private Jenkins: Detective, our first suspect is “Bobby Big nose” Hes kinda the big shot around here, being a beta-crime lord and all. But don’t let that fool you boss: he’s a hard ass. You probably won’t get much out of him. Suspect is white, 5’6, dark brown hair, brown eyes, male, age 39. \n \n You see a short round man in a black tuxedo walk in, well, his nose feels like it passes through the door 2 minutes before the rest of him. He groans as he sits down in the seat and crosses his legs on the table before lighting a smoke. He doesn’t say anything.")
def Bobby():
    bobint = input("\n Enter an evidence number or press \n a. Charm him \n b. Intimidate him \n c. Use  financial or criminal Leverage against him")

Bobby()


print("\n Private Jenkins: Detective, our second suspect is Slippery Sam. Creepy guy. He’s a small time thief but rumor has it he’s gotten into um... taking bodies too. We can’t get a read on the guy but we caught him near the seen. Too much of a coincidence to not bring him in. Just last week we brought him in on a similar charge but he walked. Suspect is white, 6’3, bright blond hair, blue eyes, male, age 25. \n \n You see a tall lanky man in a deep red turtle neck slowly walk in, a crooked smile on his face. He sits down quietly and places his long fingers on the table before leaning in slightly and extending his hand. This whole time he hasn’t blinked once. \n \n Slippery Sam: Good sir.... it’s a pleasure to meet you, id like to cooperate in any way I can...")
def Sam():
    samint = input("\n Enter an evidence number or press \n a. Charm him \n b. Intimidate him \n c. Use  financial or criminal Leverage against him")
Sam()

print("\n Private Jenkins: Uh... um... sir, we have a third suspect. We found him close by to the scene watching the police, he might’ve been waking his dog but he could be an invaluable witness. Uhhh we tried getting his name on the witness form but he signed as “Beautiful Paul” Don’t get too distracted sir. Suspect is white, 6 ft exactly, ginger hair, green eyes, male, age 22. \n \n A tanned, in-shape young man walks through the door- curly orange hair swaying as he walked. You notice his hair looks dyed, recently in fact. He’s wearing a black wife beater and jeans. He sits down and flicks his sun glasses off before nodding at you. \n \n Beautiful Paul: Sup’ king? What can Beautiful Paul~ do for you today?")
def paul():
    paulint = input("\n Enter an evidence number or press \n a. Charm him \n b. Intimidate him \n c. Use  financial or criminal Leverage against him")
paul()
