allin = ""
while True:
    try:
        allin += input() + "\n"
    except:
        break
raise ValueError("%s"%allin)