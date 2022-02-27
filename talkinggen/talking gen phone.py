import random
import winsound
import os
fileat = os.path.dirname(os.path.abspath(__file__)) + str("\g")
def benanswer():
    randomvar = random.randint(1, 5)
    if randomvar == 1:
        print("Ben - ho ho ho")
        winsound.PlaySound(fileat + "enhohoho", winsound.SND_FILENAME)
        benstart()
    if randomvar == 2:
        print("Ben - yes")
        winsound.PlaySound(fileat + "enyes", winsound.SND_FILENAME)
        benstart()
    if randomvar == 3:
        print("Ben - no")
        winsound.PlaySound(fileat + "enno", winsound.SND_FILENAME)
        benstart()
    if randomvar == 4:
        print("Ben - eugh")
        winsound.PlaySound(fileat + "enaugg", winsound.SND_FILENAME)
        benstart()
    if randomvar == 5:
        print("Ben cut the line!")
        winsound.PlaySound(fileat + "encutline", winsound.SND_FILENAME)
        askstart()
def benstart():
    input("Ask ben a question: ")
    benanswer()
def askstart():
    if input("What do you want to do (phone or close) ") == "phone":
        winsound.PlaySound(fileat + "enstart", winsound.SND_FILENAME)
        print("Ben")
        benstart()
    else:
        quit()
askstart()