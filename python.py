print("Hello, I am AI, what is your name?")

name = input()

print(f"Hello {name}, nice to meet you")
print("How has your day been? Good or Bad?")

mood = input().lower()

if mood == "good":
    print("That's nice to hear")
else:
    print("It's okay to have a bad day, come back stronger!")


print("Thank you for talking to AI")