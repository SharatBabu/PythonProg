def circle_radius():
    try:
        rad = float(input("Enter radius : "))
        if (rad > 0):
            aoc = (3.14 * (rad ** 2))
            coc = (2 * 3.14 * rad)
            print("Area of Circle : ", aoc, "\nCircumference of Circle", coc)
        else:
            print("Give proper values")
            circle_radius()
    except ValueError:
        print("enter valid input")
        circle_radius()

circle_radius()