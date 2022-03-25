#start of loop

# initialised loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name !="xxx" and count < MAX_TICKETS:

   # tells user how many seats are left
   if count <4:
        print("You have {} seats "
          "left".format(MAX_TICKETS - count))

    # warn user that there is ONE available seat left
   else:
       print("*** There is ONE seat left! ***")

   # Get details...
   name = input("Name: ")
   count +=1
   print()

if count == MAX_TICKETS:
    print("You have sold all the available tickets")
else:
    print("You have sold {} ticket."
          "There are {} seats available".format(count, MAX_TICKETS - count))
