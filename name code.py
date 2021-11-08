firstName, middleName, lastName = input ().split ()
firstInitial = firstName[0]
middleInitial = middleName[0]


initials = firstInitial, middleInitial

new_initials = ('.'). join(initials)

fullName_list = (lastName, new_initials+'.')

my_name_string = (‘,'). join(fullName_list)

print (my_name_string)