def electricity_bill(name: str, current_reading: float, prev_reading: float,
                     flat_units: float, flat_rate: float,
                     remaining_units_rate: float, vat_rate: float,
                     monthly_service_fee: float, bal_fwd: float):
  units = current_reading - prev_reading
  if units <= flat_units:
    total_cost = units * flat_rate
  else:
    remaining_units = (units - flat_units) * remaining_units_rate
    total_cost = flat_units * flat_rate + remaining_units
  vat = (vat_rate / 100) * total_cost
  service_fee = monthly_service_fee
  total_invoice_bill = total_cost + vat + service_fee + bal_fwd

  output = f"{name}, your electricity bill is now at UGX {total_invoice_bill}"
  return output


customer_name = input("Enter customer name: ")
current_meter_reading = input("Enter the current meter reading: ")
previous_meter_reading = input("Enter the previous meter reading: ")
flat_meter_units = input("Enter the flat units: ")
flat_meter_rate = input("Enter the flat rate: ")
remaining_units_meter_rate = input("Enter the remaining units meter rate: ")
vat_tax = input("Enter the VAT rating: ")
meter_serice_fee = input("Enter the monthly service fee: ")
balance = input("Enter the balance brought forward: ")
if bool(customer_name) and bool(current_meter_reading) and bool(
    previous_meter_reading) and bool(flat_meter_units) and bool(
      flat_meter_rate) and bool(remaining_units_meter_rate) and bool(
        vat_tax) and bool(meter_serice_fee) and bool(balance):
  try:
    current_meter_reading = float(current_meter_reading)
    previous_meter_reading = float(previous_meter_reading)
    flat_meter_units = float(flat_meter_units)
    flat_meter_rate = float(flat_meter_rate)
    remaining_units_meter_rate = float(remaining_units_meter_rate)
    vat_tax = float(vat_tax)
    meter_serice_fee = float(meter_serice_fee)
    balance = float(balance)
    my_bill = electricity_bill(customer_name, current_meter_reading,
                               previous_meter_reading, flat_meter_units,
                               flat_meter_rate, remaining_units_meter_rate,
                               vat_tax, meter_serice_fee, balance)
    print(my_bill)

  except:
    print(
      "There was a problem, please enter numeric values only for readings, rate and balance."
    )
else:
  print("You must enter values for readings, rate and balance")
