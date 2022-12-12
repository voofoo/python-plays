print("  ")
print("=/============================\=")
print("/______-+ Am I Satoshi +-______\\")
print("================================")

#Verify if one might be Satoshi
print("So, you want to find out if \nyou or someone you know might \nbe Satoshi ?")
print("")
print("Ok, let's roll. First things first though. \nTell me some things about you.")
print("")
has_brain = str(input("Use Y for Yes, N for No. Ok ? "))
print("")
if (has_brain == "Y"):
    print("ok, you're breathing, here we go...")
if (has_brain == " "):
    print("I'm an algorithm, not a psychic. \n...")
else:
    if (has_brain == "N"):
        print("Not very cooperative\n...")
knows_PGP = str(input("\nCan you use PGP ? "))
if (has_brain == "Y") + (knows_PGP == "Y"):
    print("\nLooking good there.. ")
else:
    if (has_brain == "Y") + (knows_PGP == "N"):
        print("\nWHY U NO PGP \O/.")
    if (has_brain == "N") + (knows_PGP == "N"):
        print("\nYou really need a pulse and a brain to be a candidate..")
    if (has_brain == "N") + (knows_PGP == "Y"):
        print("\nYou're making no sense, are you Craig Wright ?..")
                 
                

