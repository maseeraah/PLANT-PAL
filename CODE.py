import datetime

plants = []

def add_plant(name, frequency):
    plant = {
        "name": name.strip(),
        "frequency": frequency,
        "last_watered": datetime.date.today()
    }
    plants.append(plant)
    print(f"✅ Added {name} (water every {frequency} days).")

def list_plants():
    """Show all plants currently stored."""
    if not plants:
        print("🌱 No plants added yet.")
    else:
        print("\n📋 Your Plants:")
        for plant in plants:
            print(f"- {plant['name']} (every {plant['frequency']} days, last watered {plant['last_watered']})")

def water_plant():
    """Ask user to choose from the list of plants before watering."""
    if not plants:
        print("⚠️ No plants added yet. Please add a plant first.")
        return
    
    print("\n📋 Choose a plant to water:")
    for i, plant in enumerate(plants, start=1):
        print(f"{i}. {plant['name']}")

    try:
        choice = int(input("Enter the number of the plant: ").strip())
        if 1 <= choice <= len(plants):
            plants[choice - 1]["last_watered"] = datetime.date.today()
            print(f"💧 You watered {plants[choice - 1]['name']} today!")
        else:
            print("⚠️ Invalid choice.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def check_reminders():
    today = datetime.date.today()
    print("\n🌿 Plant Watering Reminders:")
    if not plants:
        print("No plants added yet.")
        return
    for plant in plants:
        days_since = (today - plant["last_watered"]).days
        if days_since >= plant["frequency"]:
            print(f"👉 Water {plant['name']} today! (Last watered {days_since} days ago)")
        else:
            print(f"✅ {plant['name']} is fine (next in {plant['frequency'] - days_since} days).")

def show_menu():
    while True:
        print("\n--- Plant Watering Reminder ---")
        print("1. Add Plant")
        print("2. Water Plant")
        print("3. Check Reminders")
        print("4. List Plants")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            name = input("Enter plant name: ").strip()
            try:
                frequency = int(input("Enter watering frequency (days): ").strip())
                add_plant(name, frequency)
            except ValueError:
                print("⚠️ Please enter a valid number for frequency.")
        elif choice == "2":
            water_plant()
        elif choice == "3":
            check_reminders()
        elif choice == "4":
            list_plants()
        elif choice == "5":
            print("👋 Goodbye! Keep your plants healthy!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    show_menu()

