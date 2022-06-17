#input a purchase price
purchasePrice = float(input("Enter a puchase price: $"))

downPayment = purchasePrice * 0.1
balance = purchasePrice - downPayment
monthlyPayment = balance * 0.05
month = 1
remainingBalance = 0

print("Month | Total Balance | Monthly Interest | Monthly Principal | Monthly Payment | Balance Remaining")
while balance >= 0.01:
  print("%-6d" % (month), end = "")
  print("| $%-13.2f" % balance, end = "")
  interest = (balance * 0.12)/12
  print("| $%-16.2f" % interest, end = "")
  principal = monthlyPayment - interest
  print("| $%-17.2f" % principal, end = "")
  print("| $%-15.2f" % monthlyPayment, end = "")
  remainingBalance = balance - interest - principal - monthlyPayment
  print("| $%-7.2f" % remainingBalance)
  balance = remainingBalance
  month += 1