student_names=["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]

for name in student_names:
    if name == "Bort":
        continue
        print("Fount him! " + name)
    print("Currently testing " + name)
    

'''NOTES:
Python automatically assumes you want to start at the start of list,
and iterate over it incrementally by one, and track the length of a 
list.
the range function is helpful, it generates a list
for index in range
it takes 3 arguments, start(optional), end(required) and increment(optional)

the break keyword breaks a loop
everything below the continue keyworrd would not be implemented

'''
