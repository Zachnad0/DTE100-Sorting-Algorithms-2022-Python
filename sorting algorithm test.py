import datetime as dtime
import random as rand
import os
import sys
# # print("f: " +os.getcwd()) #debug
# sys.path.insert(0, os.getcwd() + "\AnythingLib")
import AnythingLib


class Program:
    defArrSize = 10
    defValSize = 1000
    defIterSize = 1

    def Main():
        errZone1 = True
        while errZone1:  # captivate for options
            errZone1 = False
            try:
                choice1 = input(
                    "\nWhat type of sorting algorithm?\n0: Bubble (Default)\n1: Bubble-Optimized\n2: Selection\n3: Displacement\n69: All\n")
                tmp = input(str.format(
                    "\nHow many randomized values in the input array? (Default: {0}): ", Program.defArrSize))
                randArraySize = int(tmp) if tmp != "" else Program.defArrSize
                tmp = input(str.format(
                    "\nLargest possible number? (Default: {0}): ", Program.defValSize))
                maxValSize = int(tmp) if tmp != "" else Program.defValSize
                if choice1 == "69":
                    tmp = input(str.format(
                        "How many times to test? (Default: {0}): ", Program.defIterSize))
                    iterations: int = int(
                        tmp) if tmp != "" else Program.defIterSize
            except:
                print("\nerr - INVALID VALUE")
                errZone1 = True

        # generate random array
        sortThis = []
        if choice1 != "69":
            for i in range(0, randArraySize):
                sortThis.append(rand.randint(0, maxValSize))
            print("Input: " + str(sortThis))  # debug

        match choice1:
            case "1":
                itersXSwapsXCompares = AnythingLib.SortingAlgorithms.OptimalBubbleSort(
                    sortThis)
                print("Optimized Bubble Sorting")

            case "2":
                itersXSwapsXCompares = AnythingLib.SortingAlgorithms.SelectionSort(
                    sortThis)
                print("Selection Sorting")

            case "3":
                itersXSwapsXCompares, sortThis = AnythingLib.SortingAlgorithms.DisplaceSort(
                    sortThis)
                print("Displacement Sorting")

            case "69":  # all
                for i in range(0, iterations):
                    print(str.format("\n========== Iter {0} ==========\n", i))
                    # fill
                    sortThis = []
                    for f in range(0, randArraySize):
                        sortThis.append(rand.randint(0, maxValSize))
                    sortThis2 = sortThis.copy()
                    sortThis3 = sortThis.copy()
                    sortThis4 = sortThis.copy()

                    # bubble
                    a = dtime.datetime.now()
                    itersXSwapsXCompares = AnythingLib.SortingAlgorithms.BubbleSort(
                        sortThis)
                    b = dtime.datetime.now()
                    print(str.format("Bubble Sorting:\nIterations: {0}  Swaps: {1}  Compares: {2}  Time: {3}\n",
                          itersXSwapsXCompares[0], itersXSwapsXCompares[1], itersXSwapsXCompares[2], b-a))

                    # optimal bubble
                    a = dtime.datetime.now()
                    itersXSwapsXCompares = AnythingLib.SortingAlgorithms.OptimalBubbleSort(
                        sortThis2)
                    b = dtime.datetime.now()
                    print(str.format("Optimized Bubble Sorting:\nIterations: {0}  Swaps: {1}  Compares: {2}  Time: {3}\n",
                          itersXSwapsXCompares[0], itersXSwapsXCompares[1], itersXSwapsXCompares[2], b-a))

                    # selection
                    a = dtime.datetime.now()
                    itersXSwapsXCompares = AnythingLib.SortingAlgorithms.SelectionSort(
                        sortThis3)
                    b = dtime.datetime.now()
                    print(str.format("Selection Sorting:\nIterations: {0}  Swaps: {1}  Compares: {2}  Time: {3}\n",
                          itersXSwapsXCompares[0], itersXSwapsXCompares[1], itersXSwapsXCompares[2], b-a))

                    # displacement
                    a = dtime.datetime.now()
                    itersXSwapsXCompares, sortThis4 = AnythingLib.SortingAlgorithms.DisplaceSort(
                        sortThis4)
                    b = dtime.datetime.now()
                    print(str.format("Displacement Sorting:\nIterations: {0}  Swaps: {1}  Compares: {2}  Time: {3}\n",
                          itersXSwapsXCompares[0], itersXSwapsXCompares[1], itersXSwapsXCompares[2], b-a))

            case _:  # default
                itersXSwapsXCompares = AnythingLib.SortingAlgorithms.BubbleSort(
                    sortThis)
                print("Bubble Sorting")

        if choice1 != "69":
            print("\nOutput: " + str(sortThis))
            print("\nIterations: " + str(itersXSwapsXCompares[0]) + "\nSwaps: " + str(
                itersXSwapsXCompares[1]) + "\nCompares: " + str(itersXSwapsXCompares[2]))


Program.Main()
