#Section 2.1
meal = 44.50

#Section 2.2
meal = 44.50
tax = 6.75/100

#Section 2.3
meal = 44.50
tax = 0.0675
tip = 15.0/100

#Section 2.4
meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal*tax

#Section 2.5
meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal*tip

print("%.2f" % total)
