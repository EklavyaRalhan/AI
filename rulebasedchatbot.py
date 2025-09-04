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


