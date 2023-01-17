from Ex8 import p8
from Ex9 import p9
from Ex12 import p12

def testp8():
    """
    Test pentru functia p8
    """
    assert p8(0,[]) == "No available sequence"
    assert p8(3,[12,13,14]) == "No available sequence"
    assert p8(7,[2,3,14,3,5,6,7]) == [3,5,6,7]
    assert p8(9, [14, 10, 3, 55, -2, -3, -7, -10,-5]) == [10,3]

def testp9():
    """
    Test pentru functia p9
    """
    assert p9(0,[]) == "No available sequence"
    assert p9(1,[12]) == "No available sequence"
    assert p9(3,[1,2,3]) == [1,2]
    assert p9(4,[1,2,3,2]) == [2,3,2]
    assert p9(7,[2,4,2,14,15,14,15]) == [14,15,14,15]
    assert p9(7,[2,3,3,4,4,3,4]) == [2,3,3,4,4,3,4]
#Test pentru functia p12
def testp12():
    """"
    Test pentru functia p12
    """
    assert p12(0,[]) == "No available sequence"
    assert p12(3,[1,2,1]) == [1]
    assert p12(5,[1,2,-2,2,-2]) == [2,-2,2,-2]
    assert p12(10,[2,-2,2,-2,-2,3,-3,3,-3,3]) == [-2,3,-3,3,-3,3]

def printMenu():
    """
    Used to print the menu of available commands when the input is "help"
    """
    print("Type 1 to start initializing the array")
    print("Type 2 to show the longest sequence with the 8th property")
    print("Type 3 to show the longest sequence with the 9th property")
    print("Type 4 to show the longest sequence with the 12th property")
    print("Type exit to stop the app")
#Starts the console app
def start():
    n=0
    l=[]
    while True:
        
        cmd = input()
        if cmd == "1":
            n = int(input("Enter the length of the array: "))
            l=[]
            for i in range(0,n):
                l.append(int(input("Enter element: ")))
        elif cmd == "2":
            print(p8(n,l))
        elif cmd == "3":
            print(p9(n,l))
        elif cmd == "4":
            print(p12(n,l))
        elif cmd == "exit":
            return
        elif cmd =="help":
            printMenu()
        else:
            print("Unknown command, type help to show list of available commands")
        
testp8()
testp9()
testp12()
start()

