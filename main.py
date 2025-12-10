choice = input("Do you do your homework? yes or no: ").lower()

if choice == "yes":
    mood = input("Are you motivated? yes or no: ").lower()
    snack = input("Pick a snack: chips or fruit: ").lower()
    music = input("Music while working? yes or no: ").lower()

    if mood == "yes" and music == "yes":
        print("You enter a productivity trance and finish a week's worth of work in 12 minutes.")
    elif mood == "yes":
        print("You complete the homework flawlessly and ascend academically.")
    elif snack == "fruit":
        print("The vitamins grant you temporary brainpower and you barely finish on time.")
    else:
        print("You finish, but only after questioning every life choice ever.")

else:
    reason = input("Why not? lazy or busy: ").lower()
    friend = input("A friend texts you. Do you respond? yes or no: ").lower()
    game = input("Do you start gaming? yes or no: ").lower()

    if reason == "lazy" and game == "yes":
        print("You game for 9 hours straight and forget what homework even is.")
    elif reason == "busy":
        print("You attempt to multitask and fail spectacularly.")
    elif friend == "yes":
        print("One text becomes 87 texts and suddenly it's tomorrow.")
    else:
        print("You do nothing. Time passes. Your GPA cries.")
