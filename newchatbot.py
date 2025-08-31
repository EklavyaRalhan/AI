print("Hello, I am your AI chatbot, what is your name?")

name = input("Enter Name: ")

print(f"Hello {name}, nice to meet you.")
print("How has your day been so far?")

day = input("How has your day been?")

if day.lower() == "good":
    print("That is good to hear")
    print(f"What have you done today? {name}")
    answers = input("")
    print(f"That's intresting to hear {name}, what do you plan to do tomorrow to make your day equally as good?")
    answers2 = input("")
    print(f"That sounds like an intresting plan, I hope that you enjoy your day tomorrow {name}")
elif day.lower() == "okay":
    print("An average day today, that's fine to have sometimes. Are you looking forward to the weekend for some excitment?")
    answers3 = input("")
    print(f"Sounds like a plan {name}, enjoy your weekend!")
elif day.lower() == "bad":
    print(f"I'm sorry to hear that {name}")
    print("Everyone has bad days, it's about how you get over them")
    print("Would you like to hear some more motivation?")
    answer = input("Enter Choice: ")
    if answer.lower() == "yes":
        print("Tough times never last, tough people do")
    else:
        print("That's fine!")

print("Would you like to continue talking")

userchoice = input("Enter Choice: ")

if userchoice.lower() == "yes":
    print("Let's keep talking!")
    print("Tell me about yourself, what's your favorite sport?")
    userchoice2 = input("")
    print("That is intresting, how many times do you train or play?")
    userchoice3 = input("")
    print("It is interesting to hear about your commitment to your sport, are there any other hobbies you persue?")
    userchoice4 = input("")
    print("That's nice to hear, is there anything else you would like to share?")
    userchoice5 = input("")
    if userchoice5.lower() == "yes":
        print("What would you like to share")
        sharedinfo = input("")
        print("Thank you for sharing, have a nice day!")
    else:
        print("Have a good day!")



else:
    print(f"Thanks for talking {name}")