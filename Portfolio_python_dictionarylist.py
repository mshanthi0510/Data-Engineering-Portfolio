# 1. Create a Tuple for event info (Name, Date)
EVENT_INFO = ("Python Gala", "2024-12-25")

# 2. Initialize your List, Set, and Dictionary
guest_list = []  # Chronological list
unique_guests = set()  # Unique names only
diet_prefs = {}  # Name: Diet Mapping


# 3. Define the Function
def add_guest(name, diet):
    # YOUR CODE HERE: Clean the name string
    clean_name = name.strip().capitalize()
    # YOUR CODE HERE: Add name to the list
    if clean_name in unique_guests:
        print(f"Notice {clean_name} is already invited! ReCheck the dietary preferences")
        diet_prefs[clean_name] = diet
        print(f"Updated {clean_name} Preference's to {diet}")
        pass
    else:
        guest_list.append(clean_name)
    # YOUR CODE HERE: Add name to the set
        unique_guests.add(clean_name)
    # YOUR CODE HERE: Update the dictionary with the diet
        diet_prefs.update({clean_name:diet})
        print(f"Guest {name} added!")


# 4. The Loop
while True:
    print(f"\nWelcome to {EVENT_INFO[0]} on {EVENT_INFO[1]}")
    action = input("Type 'add' to invite or 'view' to see list (or 'exit'): ").lower()
    if action == "add":
        n = input("Guest Name: ")
        d = input("Dietary Preference: ")
        # YOUR CODE HERE: Call your function
        add_guest(n,d)

    elif action == "view":
        # YOUR CODE HERE: Use a Loop to print every guest in the list
        for i,r in diet_prefs.items():
            print(f"{i} : {r}")
        pass

    elif action == "exit":
        break