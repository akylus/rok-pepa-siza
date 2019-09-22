def winchecker(player,cpu):
    if(player == cpu):
        return 2
    elif(player == 1):
        if(cpu == 2):
            return 1
        else:
            return 0
    elif(player == 2):
        if(cpu == 3):
            return 1
        else:
            return 0
    elif(player == 3):
        if(cpu == 1):
            return 1
        else:
            return 0