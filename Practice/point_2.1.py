points_ahead = int(input("Enter the lead in points"))
lead_calculation = float(points_ahead - 3)
has_ball = input("Does the lead team have the ball (Yes or No): ")
if has_ball == 'Yes':
    lead_calculation = lead_calculation + 0.5
else:
    lead_calculation = lead_calculation - 0.50

if lead_calculation < 0:
    lead_calculation = 0

lead_calculation = lead_calculation** 2

seconds_remaining = int(input("Enter the number of remaining seconds: "))

if lead_calculation > seconds_remaining:
    print("Lead is safe")
else:
    print("Lead is not safe")