def make_fizz_buzz():
    """This function creates the fizz buzz game for the numbers 3 and 5"""
    my_num_list = []
    counter = 1
    while len(my_num_list) < 100:
        my_num_list.append(counter)
        counter+=1

    for num in my_num_list:
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

make_fizz_buzz()