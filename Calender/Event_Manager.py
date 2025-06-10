# A simple event manager using dictionary , functions , loop , oops 

class EventManager:
    def __init__(self):
        self.events = {}

    def add_event(self, date, event):
        if date in self.events:
            self.events[date].append(event)
        else:
            self.events[date] = [event]

    def remove_event(self, date, event):
        if date in self.events and event in self.events[date]:
            self.events[date].remove(event)
            if not self.events[date]:  # Remove the date if no events left
                del self.events[date]

    def get_events(self, date):
        return self.events.get(date, [])
    
    def get_all_events(self):
        return self.events
    
    def clear_events(self):
        self.events.clear()
        return "All events cleared."
    

def main():
    print("Welcome to the Event Manager!")
    manager = EventManager()

    while True:
        print("\nChoose an option:")
        print("1. Add Event")
        print("2. Remove Event")
        print("3. View Events on a Date")
        print("4. View All Events")
        print("5. Clear All Events")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            event = input("Enter the event description: ")
            manager.add_event(date, event)
            print(f"Event '{event}' added on {date}.")

        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD): ")
            event = input("Enter the event description to remove: ")
            manager.remove_event(date, event)
            print(f"Event '{event}' removed from {date}.")

        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD): ")
            events = manager.get_events(date)
            if events:
                print(f"Events on {date}: {', '.join(events)}")
            else:
                print(f"No events found on {date}.")

        elif choice == '4':
            all_events = manager.get_all_events()
            if all_events:
                for date, events in all_events.items():
                    print(f"{date}: {', '.join(events)}")
            else:
                print("No events scheduled.")

        elif choice == '5':
            confirmation = input("Are you sure you want to clear all events? (yes/no): ")
            if confirmation.lower() == 'yes':
                manager.clear_events()
                print("All events cleared.")
        
        elif choice == '6':
            print("Exiting Event Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()