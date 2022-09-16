event_type = int(input("Enter your event type- Press 1 for private - 2 for cooperate: "))
if event_type == 1:
    event_manager = "C. Larman"
elif event_type == 2:
    event_manager = "Ken Bass"
else:
    event_manager = "Unknown - Invalid Event Type"

print("You chose an event of type:", event_type, "and will be managed by :", event_manager)