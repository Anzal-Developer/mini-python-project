# input we need to get from the user
# 1. total rent amount 
# 2. total food ordered for snacks
# 3. Electricity unit consumed 
# 4. charge per unit of electricity 
# 5. number of persons
## Output 
#  Total amount to be paid by each person 

rent = int (input("Enter your hostel/apartment rent amount = "))
food = int (input("Enter the total food amount = "))
electricity_unit = int (input("Enter the total electricity unit consumed ="))
charge_per_unit = int (input("Enter the charge per unit of electricity = ")) 
persons = int (input("Enter the number of persons = "))

total_bill = electricity_unit * charge_per_unit

Output = (rent + food + total_bill) //persons

print("Total amount to be paid by each person = ", Output)
