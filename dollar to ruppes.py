# Program to convert dollars to Indian rupees

def convert_dollars_to_inr(dollars):
    return dollars*85.1
# Input
amount = input("Enter amount in dollars (e.g., 5, 20, or 1M for 1 million): ").strip().upper()
# exchange_rate = float(input("Enter current USD to INR exchange rate: "))

# Check if input is in millions
if 'M' in amount:
        million_value = float(amount.replace('M', ''))
        dollars = million_value * 1_000_000
elif "CR" in amount:
      cr_value = float(amount.replace("CR"," "))
      dollars = cr_value * 10000000
elif "LAKHS" in amount:
      lakhs_value = float(amount.replace("LAKHS"," "))
      dollars = lakhs_value * 100000



else:
        dollars = int(amount)

# Conversion
rupees = convert_dollars_to_inr(dollars)
if (rupees >= 10000000):
       print(f"${amount} is equal to ₹{(rupees/10000000)} cr.")
elif(rupees >= 100000 or rupees<=10000000):
      print(f"${amount:} is equal to ₹{rupees/100000} lakhs.")

else:
    print(f"${amount} is equal to ₹{rupees}")
