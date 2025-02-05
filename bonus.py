user_wieght:float=float(input("enter your weight in kg:"))
user_height:float=float(input("enter your height in cm:"))/100
bmi:float=user_wieght/user_height**2
print(f"Your BMI is: = {round(bmi,2)}")
suggested_weight_range_from:float=18.5*user_height**2
suggested_weight_range_to:float=24.9*user_height**2

if bmi >=25:
    print("You are overwieght you need to work out more and watch your diet")
    print(f"Your suggested weight range: {round(suggested_weight_range_from,1)}-{round(suggested_weight_range_to,1)} kg")
elif bmi >18.5:
    print("You are fit & healthy.")
    print(f"Your suggested weight range: {round(suggested_weight_range_from,1)}-{round(suggested_weight_range_to,1)} kg")

else:
    print("You are underweight. Watch your health.")
    print(f"Your suggested weight range: {round(suggested_weight_range_from,1)}-{round(suggested_weight_range_to,1)} kg")
