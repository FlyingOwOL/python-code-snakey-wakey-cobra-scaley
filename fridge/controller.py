import dto as fridge_dto

actions = ["put", "take", "leave"]
while True:
    print("Choose an action:" + "")
    selection = input("Your choice(put, take, leave):")

    print("Your choice: " + selection + "\n")
    match selection:
        case "put":
            fridge_dto.put_item()
        case "take":
            fridge_dto.take_item()
        case "leave":
            print("\n\nLeaving the fridge controller.")
            break
        case __:
            print("Invalid action. Please try again.\n\n\n")
    