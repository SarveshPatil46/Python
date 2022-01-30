car_state = ""
while True:
    user_input = input("> ")
    if user_input == "help":
        car_state = "help"
        print("""Enter
        start : to start the car
        stop : to  stop the car
        quit : to quit the game
        """)

    elif user_input == "start" and not car_state == "start":
        car_state = "start"
        print("Car has started")

    elif user_input == "start" and car_state == "start":
        car_state = "start"
        print("Car has already started")

    elif user_input == "stop" and not car_state == "stop":
        car_state = "stop"
        print("Car has stopped")

    elif user_input == "stop" and car_state == "stop":
        car_state = "stop"
        print("Car has already stopped")

    elif user_input == "quit":
        break

    else:
        print("I don't understand that")
