
def findStats(seed):

    currentNum = seed

    stoppingTime = None
    totalStoppingTime = 0
    maxNum = seed

    while currentNum != 1:

        if currentNum % 2 == 0:
            currentNum //= 2

            if stoppingTime == None and currentNum < seed:
                stoppingTime = totalStoppingTime + 1

        else:
            currentNum = (3*currentNum + 1) // 2

            if maxNum < currentNum:
                maxNum = currentNum

        totalStoppingTime += 1

    expansionFactor = round(maxNum/seed, 2)

    return stoppingTime, totalStoppingTime, expansionFactor

def main():

    print('~ Collatz Stats ~\n')

    run = True

    while run:

        seed = input("Enter a seed : ")
        print()

        try:
            seed = int(seed)
            if seed < 1:
                raise ValueError
        except:
            print('The seed must be a positive integer.\n')
            continue

        if seed != 1:
            st, tst, ef =  findStats(seed)

        else:
            st, tst, ef = 'infinity', 2, 2

        print("Stopping time       : " + str(st))
        print("Total stopping time : " + str(tst))
        print("Expansion factor    : " + str(ef) + '\n') 

        choice = None

        while choice not in ('y', 'n'):

            choice = input("Would you like to enter another seed? [y/n] : ").lower()
            print()

            if choice == 'n':
                run = False
            
            if choice != 'y' and choice != 'n':
                print('Invalid choice.\n')

if __name__=='__main__':
    main()
