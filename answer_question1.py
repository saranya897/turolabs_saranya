def findProcessors(start, stop, n):
    for i in start:


if __name__ == '__main__':
    start = [900, 940, 950, 1000, 1500, 1600]
    stop = [910, 1020, 1010, 1015, 1620, 1700]
    n = len(start)
    print("Minimum Number of Processors Required = ",
          findProcessors(start, stop, n))
