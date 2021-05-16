# get rank which takes the users rank as an argument and determines
# if it is valid input

def getRank(x):
    # make a list of the acceptable choices
    choices = ['l','m','h']
    # convert the users rank to lowercase
    x = x.lower()
    # create a while True loop that only runs if x is not in the choices
    while True:
        if x not in choices:
            # remind the user of the valid choices
            print('Only enter a valid choices')
            print(choices[0:3])
            x = input('Please enter a rank: ')
            x = x.lower()
            # add an if statement to continue the loop if the users new input is still incorrect
            if x not in choices:
                continue
        # if everything is all good break from the loop
        else:
            break
    return x

def main():
    print('Please enter a ranking for the items')
    print('l for low,m for medium,h for high')
    print('')
    print('Please enter a rank for milk')
    # prompt the user to enter their rate
    userRate = input('Please enter a rank: ')
    # validate their input
    validRank = getRank(userRate)
    # assign the users rating to validRank as it will only hold a valid choice
    # continue doing this for each item
    milkRate = validRank
    print('Please enter a rank for cheese')
    userRate = input('Please enter a rank: ')
    validRank = getRank(userRate)
    cheeseRank = validRank
    print('Please enter a rank for eggs')
    userRate = input('Please enter a rank: ')
    validRank = getRank(userRate)
    eggRank = validRank
    print('')
    #output the users ratings for the items
    print('Your overall ratings are:')
    print('Milk:',milkRate)
    print('Cheese:',cheeseRank)
    print('Eggs:',eggRank)

main()