while True:
    height = float(input("Enter your height (cm) : "))
    weight = float(input("Enter your weight (kg)  : "))
    
    height_1 = height/100

    bMi = weight/height_1**2

    if bMi < 18.5 :
        print ("""
Result -------------------------------
Weight Status  : Underweight
BMI            : """,round(bMi))
    elif 18.5 <= bMi <= 24.9 :
        print ("""
Result -------------------------------
Weight Status  :Ideal
BMI            : """,round(bMi))
    elif 25.0 <= bMi <= 29.9 :
        print ("""
Result -------------------------------
Weight Status  : Overweight
BMI            : """,round(bMi))
    elif bMi >= 30 :
        print ("""
Result -------------------------------
Weight Status  : Obesity
BMI            : """,round(bMi))

    next_session = input("Would you like to repeat (Y/N)? ")

    if next_session.upper() == 'Y' :
        print('\n')
        pass
    else :
        break