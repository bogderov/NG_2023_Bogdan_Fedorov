#Introduction
#initialize variable
user_things_digits = 0
print("Hello There, I am simple unifier. Write me anything writeble and I will display only unique things you wrote!\nP.s. To stop writing your things type ':wq' or 'alt+F4' to exit without saving.")
#Initialise empty list for user things
user_things = []
 #User can write things until he want or run out of memory, it's Infinite loop
while True:

    user_things_input = input("Write your thing\n")
    #it checks whether the user wants to give up if true than it exits Infinite loop 
    if user_things_input == ':wq':
      break
    #Adding user things to the end of the list    
    user_things.append(user_things_input)
    #Cheks if user wrote numeric thing, .replace(".", "") - remove . from user thing and then isdigit() - cheks is it made of digits and return True
    if user_things_input.replace(".", "").isdigit():
      user_things_digits += 1
    
#Removing duplicates by using 'set' which converts list into a set( it's an unordered collection of unique elements when you convert a list to a set, it automatically removes any duplicates, leaving nly the unique elements from the original list), then with 'list' convert it back into a list 
unique_user_things = list(set(user_things))
#Output list of unique user things
print (unique_user_things)
#Output number of numeri things in user_things list
print ("You wrote so many numbers in list:", user_things_digits)