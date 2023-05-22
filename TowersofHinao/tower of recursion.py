import time

def main():
    discs=int(input('Enter a number of disks in tower'))    # size of tower
    # set up start, destination and extra tower.
    moveDisk(discs,"Tower 1","Tower 3","Tower 2")           # initiate recursion
    
def moveDisk(discs, A, B, C): 
    if discs >= 1:
        # recursively calls this function until discs = 0
        # to get access to the base disc that will move to the
        # bottom of the destination tower. 
        moveDisk(discs - 1, A, C, B)
        # print when discs are moved after each iteration of
        # the recursion is called.
        printDisk(A, B)
        # moves all discs from extra tower to destination tower
        # after the base discs is moved.
        moveDisk(discs - 1, C, B, A)
        

def printDisk(fromTower, toTower):
    print("Disk moved from", fromTower,"to",toTower)
    time.sleep(0)

main()
