row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

while True:


  p1_x_cord = input("What is the x coordinate of your choice?\n ")
  p2_y_cord = input("What is the y coordinate of your choice?\n ")
  
  
  column_chosen = int(position[1])-1
  row_chosen = int(position[0])-1
  map[(column_chosen)][(row_chosen)] = "X"
  
  print(f"{row1}\n{row2}\n{row3}")