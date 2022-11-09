def electricity_bill(name:str, prev_reading:float, current_reading:float, rate:float, bal_fwd:float):
  units = current_reading - prev_reading
  amount_due = bal_fwd + units * rate
  output = f"{name}, your electricity bill is now at UGX {amount_due}"
  return output
  
customer_name = input("Enter customer name: ")
prev_meter_reading = input("Enter the previous meter reading: ")
current_meter_reading = input("Enter the current meter reading: ")
power_rate = input("Enter the power rate: ")
balance = input("Enter the balance brought forward: ")

if bool(customer_name) and bool(prev_meter_reading) and bool(current_meter_reading) and bool(power_rate) and bool(balance):
  try:
    prev_meter_reading = float(prev_meter_reading)
    current_meter_reading = float(current_meter_reading)
    power_rate = float(power_rate)
    balance = float(balance)
    my_bill = electricity_bill(customer_name, prev_meter_reading, current_meter_reading, power_rate, balance)
    print(my_bill)
  
  except:
    print("There was a problem, please enter numeric values only for readings, rate and balance.")
else:
  print("You must enter values for readings, rate and balance")