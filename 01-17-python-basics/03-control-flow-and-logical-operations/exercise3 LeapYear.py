year = int(input("Choose a year to see if it is a Leap Year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not leap year")


# должен ровно делиться на 4
# должен быть остаток при делении на 100
# должен ровно делиться на 400
