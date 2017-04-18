# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

def odd_average(list_of_numbers):
    alist = []
    try:
        try:
            for odd in list_of_numbers:
                if odd % 2 == 1:
                    alist.append(odd)
            average = sum(alist) /len(alist)
            return average
        except ZeroDivisionError:
            return 0
    except:
        return "That is not a list."

print(odd_average([1,2,3,4,5,6,7,8]))
print(odd_average(1))
print(odd_average([2,4]))
