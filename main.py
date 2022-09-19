row0 = ["⬜️", "⬜️", "⬜️"]
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
map = [row0, row1, row2]
print("     Column0  Column1  Column2")
print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")

# TODO 1. Add multiple players
# TODO 2. Add end game conditions
# TODO 3. UX improvements to prevent user from crashing game
# TODO 4. UI
# TODO
# TODO
# TODO

while True:

    p1_x_cord = int(input("Player 1: Type the X coordinate of your move. \n "))
    p1_y_cord = int(input("Player 1: Type the Y coordinate of your move.\n "))

    map[p1_y_cord][p1_x_cord] = "X    "

    print("     Column0  Column1  Column2")
    print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")

    p2_x_cord = int(input("Player 2: Type the X coordinate of your move. \n "))
    p2_y_cord = int(input("Player 2: Type the Y coordinate of your move.\n "))

    map[p2_y_cord][p2_x_cord] = "O    "

    print("     Column0  Column1  Column2")
    print(f"Row0{row0}\nRow1{row1}\nRow2{row2}")

#
# column_chosen = int(position[1])-1
# row_chosen = int(position[0])-1
# map[(column_chosen)][(row_chosen)] = "X"

# print(f"{row0}\n{row1}\n{row2}")

