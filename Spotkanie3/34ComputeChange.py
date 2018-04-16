# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

numberOfWholeZlotys = int(amount)
numberOfGroszes = int((amount * 100) % 100)

# Find the number of five hundreds zlotys
numberOfFiveHundredZlotys = numberOfWholeZlotys // 500
remainingWholeZlotys = numberOfWholeZlotys % 500

# Find the number of two hundreds zlotys
numberOfTwoHundredsZlotys = remainingWholeZlotys // 200
remainingWholeZlotys = remainingWholeZlotys % 200

# Find the number of one hundred zlotys
numberOfOneHundredsZlotys = remainingWholeZlotys // 100
remainingWholeZlotys = remainingWholeZlotys % 100

# Find the number of fifty zlotys
numberOfFiftyZlotys = remainingWholeZlotys // 50
remainingWholeZlotys = remainingWholeZlotys % 50

# Find the number of twenty zlotys
numberOfTwentyZlotys = remainingWholeZlotys // 20
remainingWholeZlotys = remainingWholeZlotys % 20

# Find the number of ten zlotys
numberOfTenZlotys = remainingWholeZlotys // 10
remainingWholeZlotys = remainingWholeZlotys % 10

# Find the number of five zlotys
numberOfFiveZlotys = remainingWholeZlotys // 5
remainingWholeZlotys = remainingWholeZlotys % 5

# Find the number of two zlotys
numberOfTwoZlotys = remainingWholeZlotys // 2
remainingWholeZlotys = remainingWholeZlotys % 2

# Find the number of one zlotys
numberOfOneZlotys = remainingWholeZlotys

# Find the number of fifty groszes
numberOfFiftyGroszes = numberOfGroszes // 50
remainingGroszes = numberOfGroszes % 50

# Find the number of twenty groszes
numberOfTwentyGroszes = remainingGroszes // 20
remainingGroszes = remainingGroszes % 20

# Find the number of ten groszes
numberOfTenGroszes = remainingGroszes // 10
remainingGroszes = remainingGroszes % 10

# Find the number of five groszes
numberOfFiveGroszes = remainingGroszes // 5
remainingGroszes = remainingGroszes % 5

# Find the number of two groszes
numberOfTwoGroszes = remainingGroszes // 2
remainingGroszes = remainingGroszes % 2

# Find the number of pennies in the remaining amount
numberOfOneGroszes = remainingGroszes

# Display the results
print("Your amount", amount, numberOfFiveHundredZlotys, numberOfTwoHundredsZlotys, numberOfOneHundredsZlotys,
      numberOfFiftyZlotys,
      numberOfTwentyZlotys, numberOfTenZlotys, numberOfFiveZlotys, numberOfTwoZlotys, numberOfOneZlotys,
      numberOfFiftyGroszes,
      numberOfTwentyGroszes, numberOfTenGroszes, numberOfFiveGroszes, numberOfTwoGroszes, numberOfOneGroszes)
