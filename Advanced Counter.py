import time
counts = 0
def counter(button):
    global counts
    count = input(f"When You Want To Count Please Type {button}: ")
    if (count == button):
        counts += 1
        counter(choosing)
    elif(count == "end"):
        print(f"You're Count's Were {counts}")
        time.sleep(1)
        going = input("Do You Want To Exit Or Repeat? (1 For Repeating And 2 For Exiting): ")
        if(going == "1"):
            counter(choosing)
        elif going == "2":
            quit()
    else:
        print(f"Plese Type {button} To Count, You're Score Was: {counts} And Now The Program Is Restarting")
        counter(choosing)
choosing = input("Enter The Word Or Button To Count With: ")
counter(choosing)
