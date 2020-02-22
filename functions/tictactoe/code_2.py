import random

combinations = [[1,2,3],[4,5,6],[7,8,9],
                [1,4,7],[2,5,8],[3,6,9],
                [1,5,9],[3,5,7]]
occupied = []
positions = [i for i in range(0,9)]
def gameBoard():
    print("""
        {} | {} | {}
       -------------
        {} | {} | {}
       -------------
        {} | {} | {}
    """.format(positions[0],positions[1],positions[2],positions[3],
    positions[4],positions[5],positions[6],positions[7],positions[8]))

def userMove(user_ch):
    pos = int(input("Enter your position : "))
    positions[pos] = user_ch
    occupied.append(pos)
    gameBoard()

def cpuMove(cpu_ch):
    if len(occupied) <= 8:
        cpu_pos = random.randint(0, 8)
        if cpu_pos in occupied:
            print("Already Occupied")
            cpuMove(cpu_ch)
        else:
            positions[cpu_pos] = cpu_ch
            occupied.append(cpu_pos)
            print("CPU Picked",cpu_pos)
        gameBoard()
    else:
        print("Game Draw")

def checkWinner():
    pass

def main():
    gameBoard()
    user_ch = input("Enter your choice : O / X : ")
    cpu_ch = 'O' if user_ch == 'X' else 'X'
    while True:
        userMove(user_ch)
        cpuMove(cpu_ch)

main()