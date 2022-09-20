def end_game_check2():
    if row0[0] == row0[1] == row0[2]:
        return False
    elif row1[0] == row1[1] == row2[2]:
        return False
    elif row2[0] == row2[1] == row2[2]:
        return False
    elif row0[0] == row1[0] == row2[0]:
        return False
    elif row0[1] == row1[1] == row2[1]:
        return False
    elif row0[2] == row1[2] == row2[2]:
        return False
    elif turns_taken == 9:
        return False
    else:
        return True