print('_______________________________________1')

def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl
print("did this work")
print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

###################
print('__________________________________2')

def sum(intx, intz=5):
    return intz + intx

print(sum(5))
print(sum(5,3))

################
print('____________________________________3')

def test(required_integer, optional_boolean=True, dict1={2:3, 4:5, 6:8}):
    if optional_boolean:
        if required_integer in dict1.keys():
            return dict1[required_integer]
    else:
        return False

print(test(5))
print(test(5,False))
print(test(2))
print(test(2,False))

#####################
print('______________________________________4')

def checkingIfIn(required_string, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction:
        if required_string in d.keys():
            return True
        else:
            return False
    elif not direction:
        if required_string not in d.keys():
            return True
        else:
            return False

print(checkingIfIn('apple'))
print(checkingIfIn('apple',False))
print(checkingIfIn('grape',False,))
print(checkingIfIn('grape'))

#############################
print('___________________________________________5')

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('app')
print(c_false)
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('appl', False)
print(c_true)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = 19
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = 8
