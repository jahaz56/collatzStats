# This function takes a seed for the 3n + 1 algorithm and returns the stopping time,
# total stopping time and the expansion factor for that seed.
def findStats(seed):

    currentNum = seed

    # set the initial values
    stoppingTime = None
    totalStoppingTime = 0
    maxNum = seed
    sequence = [seed]

    # If the number equals 1, we have fallen into the 1, 2, 1 loop and must stop.
    while currentNum != 1:

        # check if currentNum is odd or even.
        if currentNum % 2 == 0:
            currentNum //= 2

            # The stopping time is the time (in steps) it takes to reach a number
            # lower than the seed.  It can only be reached after the division step
            # which is why we check for it here.
            if stoppingTime == None and currentNum < seed:
                stoppingTime = totalStoppingTime + 1

        else:
            currentNum = (3*currentNum + 1) // 2

            # Set the maxNum whenever a new max is reached.  This can only occur
            # after the multiplication step.
            if maxNum < currentNum:
                maxNum = currentNum

        sequence.append(currentNum)
        totalStoppingTime += 1

    # Calculate the expansion factor using maxNum.
    expansionFactor = round(maxNum/seed, 2)

    return stoppingTime, totalStoppingTime, expansionFactor, sequence

def main():

    print('~ Collatz Stats ~\n')

    run = True

    while run:

        seed = input("Enter a seed : ")
        print()

        # Make sure the user can only enter a positive integer.
        try:
            seed = int(seed)
            if seed < 1:
                raise ValueError
        except:
            print('The seed must be a positive integer.\n')
            continue

        # Make sure the seed does not equal 1. If the seed equals one, the findStats function
        # will not return the correct values.
        if seed != 1:
            st, tst, ef, seq =  findStats(seed)

        else:
            st, tst, ef, seq = 'infinity', 2, 2, [1, 2, 1]

        # print the results
        print("Stopping time       : " + str(st))
        print("Total stopping time : " + str(tst))
        print("Expansion factor    : " + str(ef))
        print("Sequence            : ", end='')
        for n in range(len(seq)-1):
            print(str(seq[n]), end=', ')

        print(str(seq[-1]) + "\n")

        choice = None

        # Ask the user if they want to continue
        while choice not in ('y', 'n'):

            choice = input("Would you like to enter another seed? [y/n] : ").lower()
            print()

            if choice == 'n':
                run = False
            
            if choice != 'y' and choice != 'n':
                print('Invalid choice.\n')

if __name__=='__main__':
    main()
