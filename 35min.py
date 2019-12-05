money = 1000
while money > 100:
    print("You are at a tech startup as a software engineer specializing in java, what do you want to name your company?")
    companyName = input()
    print("You venture into your long road at", companyName)
    print("Uh-oh, a company called", companyName, "threatens you with a lawsuit!")
    print("Will you take them to court(1) or pay them(2)?")
    choice = input()
    if (choice == "1"): 
        print("You take them to court")
        print("Is your company wanting to make more than $100,000 a year?")
        courtAnswer = input()
        if (courtAnswer == "yes"): 
            money = 0
            print("You lost the lawsuit and you are broke!")
    elif (choice == "2"):
        print("You pay them $500")
        money -= 500
        print("Your money is now", money)
        print("What will you invest in, new employees(1) or utilities(2)")
        choice = input()
        if (choice == "1"):
            print("You have 5 new employees")
            employees = 10
        elif (choice == "2"):
            lawyers = 3
            print("You have hired lawyers! You now have", lawyers)
            print("You won! Lawyers will guarentee your success")
        else:
            print("Invalid input")
    else:
        print("invalid input!")
