def largest(in_list):
    if not in_list:
        return None
    largest = in_list[0]
    for element in in_list:
        if element > largest:
            largest = element
    return largest

user_list = eval(input('Enter the list: '))
largest_element = largest(user_list)

if largest_element is not None:
    print('Largest:', largest_element)
else:
    print('It is an empty list')
 
