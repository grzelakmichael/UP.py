def printGrade(score):
    if score < 0 or score > 100:
        print("Invalid score")
        return # Same as return None
    if score >= 90.0:
        print('A')
    elif score >= 80.0:
        print('B')
    elif score >= 70.0:
        print('C')
    elif score >= 60.0:
        print('D')
    else:
        print('F')