def main():
    
### Hello, World! ###
#     print("Hello, World!")


### functions ###
# def main():
#     print('This line is printed directly from the main function of the program')
#     secondary_function()
    
# def secondary_function():
#     print('This line is printed from a secondary function call within the main function')


### input / output ###
    # name = input('What is your name?')
    # print('Very nice to meet you,', name,'!')
    # print(f'Have a great day, {name.upper()}!')
    # print('See you soon, {}!'.format(name))


### type conversion ###
    # int_value = 4
    # print(int_value)
    # print(type(int_value))
    
    # print()
    
    # float_value = float(int_value)
    # print(float_value)
    # print(type(float_value))
    
### boolean values ###
    # x = 3
    # y = 4
    # result1 = 1 < x and y > 1 
    # result2 = x > 5 or y <= 3
    # result3 = not (x > 2 and y > 1) 
    # print(result1)
    # print(result2)
    # print(result3)


### if statements ###
    # score = input('What is your score? :')
    # score = int(score)
    
    # if score >= 92:
    #     print('Your final grade is an A')
    
    # elif score >= 85:
    #     print('Your final grade is a B')
    
    # elif score >= 70:
    #     print('Your final grade is a C')
    
    # else:
    #     print('Talk with your instructor about your grade!')


    nums = [3, 4, 16]
 
    print('This is an example of for loops')

    for num in nums:
        print(num ** 2)
        
        # while loop
        i = 3

    while i < 258:
        print(i)
        i = i ** 2
    
if __name__ == '__main__':
        main()