#Introduction
print("Hello There, I am simple table maker. Write me a natural number and I will create a table that contains all the numbers from 1 to that number")

# get user natural number which will be max in table
natural_number= int(input("Enter a natural number: "))

# initializing empty list that will store prime numbers
prime_numbers = []

# write the headers of the table
print("Number | Dividers")

# write - to separate headers from the content of table and it's look better this way
print("-"*42)

# looping through numbers from 1 to n + 1 (to include the user_number itself in the range)
for number in range(1, natural_number + 1):

    #creating empty list for each number in loop
    dividers = []
    
    # searching dividers for the current number
    for divider in range(1, number + 1):

        #look if the current number is divided by the current divider without a remainder
        if number % divider == 0:

            #if divided then add to list of dividers
            dividers.append(divider)

    # Check if the number has only 2 dividers that means it's prime number
    if len(dividers) == 2:

        #adding prime number to general list of prime numbers
        prime_numbers.append(number)

    # writes the number and its dividers that seperated by ,
    print(number, "|", dividers)

# writes the prime numbers
print("\nPrime Numbers:", prime_numbers)
