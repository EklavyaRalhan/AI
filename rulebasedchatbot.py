import re,random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches":["Bali","Malidves","Thailand"],
    "Mountains":["Swiss Alps","Himalyas","USA National Park"],
    "Cities":["Paris","Tokyo","Dubai"]
}

jokes = {
    "Why don't programmers like nature, because there are too many bugs!",
    "Why did the computer go to the docter, because it had a virus!",
    "Why do travellers always feel warm, because of all their hot spots!"
}

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, Mountains or Cities")
    preference = input(Fore.YELLOW + "YOU: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + f"TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ")
        
        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Amazing, enjoy {suggestion}")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another one")
            recommend()
        else:
            print(Fore.RED+"TravelBot: I'll suggest again")
            recommend()
    else: print("TravelBot: Sorry, we don't have that type of destination")

    show_help()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in  {location}")
    print(Fore.GREEN + "TravelBot: Pack versatile clothes")
    print(Fore.GREEN + "TravelBot: Bring chargers/adapters")
    print(Fore.GREEN + "TravelBot: Check the weather forecast")

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can: ")
    print(Fore.GREEN + "Suggest travel spots (type recommendation) ")
    print(Fore.GREEN + "Offer packing tips (type packing) ")
    print(Fore.GREEN + "Tell a joke (type joke) ")
    print(Fore.CYAN + "Type exit or bye to end \n")

def chat():
    print(Fore.CYAN + "TravelBot: Hello, I am TravelBot, what is your name?")
    name = input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + f"Nice to meet you {name}")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "exit" in user_input or "bye" in user_input:
            break
        else:
            print(Fore.RED + "Could you please rephrase?")

if __name__ == "__main__":
    chat()
    

