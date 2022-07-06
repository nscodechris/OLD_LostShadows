while True:
    vertical = 1
    # second = ""
    while vertical == 1:
        print("---------------------------------------------------------")
        print("As you hold on to the hard cliffs you see a light coming out from the mountain to the left\n"
              "To the right you can see the shadows moves in a mysterious way")
        where_to_climb = input("Where do you want to climb?")
        if "left" in where_to_climb:
            vertical = 2
        elif "right" in where_to_climb:
            vertical = 3
    while vertical == 2:
        print("---------------------------------------------------------")
        print("You choose the left way....")
        print("")

        input("Press enter")

        break
        # story1_first_crossing()

    while vertical == 3:
        print("---------------------------------------------------------")
        print("You choose the right way....")
        input("Press enter")
        break
        # story1_first_crossing()
        # YourHero.x_battle(cloud, 1, cloud, elena, "yes")