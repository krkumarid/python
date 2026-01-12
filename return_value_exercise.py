def get_bmi():
    weight = input("Enter your weight in kg  >")
    height =input("Enter your weight in meter >")

    bmi = float(weight)/(float(height)*float(height))

    return weight,height, bmi


def main():
    

    weight,height,bmi = get_bmi()
    print( "Weight :" + weight + "Height :"+ height + "BMI : "+ str(bmi ))



main()