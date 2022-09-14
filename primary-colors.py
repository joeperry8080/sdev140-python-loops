# declare some variables and arrays
arr_colors = ["red", "blue", "yellow"]
primary_color_1 = ""
primary_color_2 = ""

# I had to declare these when I added a loop
secondary_color = ""
user_input = ""


while user_input != "n":
    primary_color_1 = input("Enter the first primary color: ")
    primary_color_2 = input("Enter the second primary color: ")


    if primary_color_1 not in arr_colors or primary_color_2 not in arr_colors:
        print("You did not specify a primary color, try again!")
    else:
        # test for purple
        if primary_color_1 == "red" and primary_color_2 == "blue":
            secondary_color = "purple"
        # test for orange
        elif primary_color_1 == "red" and primary_color_2 == "yellow":
            secondary_color = "orange"
        # test for green
        elif primary_color_1 == "blue" and primary_color_2 == "yellow":
            secondary_color = "green"

        print(secondary_color)

    user_input = input("Enter 'y' to specify another color, 'n' to end.")

