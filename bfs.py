import copy
from time import sleep
import sys, math

''' CONSTS '''
EMPTY = {'key': 0, 'view': "-"}
PLAYER = {'key': 1, 'view': "☻"}
OBJECTIVE = {'key': 2, 'view': "♥"}
BLOCK = {'key': 3, 'view': "█"}
VALIDS_MOVES = (EMPTY, OBJECTIVE)
''' GLOBAL '''
USES = 0
DEBUG_COMPLETE = False
SLOW = False

class Point():
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
    def __str__(self):
        return f'x = {self.x}, y = {self.y}'
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
class Game():

    def __init__(self, field = [], objective = None, player = None):
        self.field = field
        self.objective = objective
        self.player = player

    def __str__(self):
        ret = ""
        for line in range(len(self.field)):
            for item in self.field[line]:
                #print(item)
                ret += str(item['view']) +' '
            ret += "\n"
        return ret  

    def is_win(self):
        return self.player == self.objective

    def move(self, new_pos):
        self.field[self.player.x][self.player.y] = EMPTY
        self.field[new_pos.x][new_pos.y] = PLAYER
        self.player = new_pos
        
    def valid_moves(self):
        v_moves = []
        #up
        if self.player.x - 1 >= 0:
            if self.field[self.player.x-1][self.player.y] in VALIDS_MOVES:
                new_move = copy.deepcopy(self)
                new_move.move(Point(self.player.x-1, self.player.y))
                v_moves.append(new_move)                                                    
        #down
        if self.player.x + 1 <= (len(self.field)-1):
            if self.field[self.player.x+1][self.player.y] in VALIDS_MOVES:
                new_move = copy.deepcopy(self)
                new_move.move(Point(self.player.x+1, self.player.y))
                v_moves.append(new_move)
        #left
        if self.player.y - 1 >= 0:
            if self.field[self.player.x][self.player.y-1] in VALIDS_MOVES:
                new_move = copy.deepcopy(self)
                new_move.move(Point(self.player.x, self.player.y-1))
                v_moves.append(new_move)
        #right
        if self.player.y + 1 <= (len(self.field[0])-1):
            if self.field[self.player.x][self.player.y+1] in VALIDS_MOVES:
                new_move = copy.deepcopy(self)
                new_move.move(Point(self.player.x, self.player.y+1))
                v_moves.append(new_move)

        return v_moves
class Node():

    def __init__(self, value = None, parent = None, childrens = []):
        self.value = value
        self.parent = parent
        self.childrens = childrens

def BFS(queue):
    if SLOW: sleep(1)

    print(queue[0].value)
    
    global USES
    USES += 1
    
    if len(queue) == 0:
        raise Exception('Não há resultado para o problema')
           
    if queue[0].value.is_win():
        print(f'Resultado encontrado em {USES} passos!')
        return queue[0]

    for move in queue[0].value.valid_moves():
        if DEBUG_COMPLETE:
            print(move)
            print(move.player) 
            print(move.objective) 
            print(move.is_win())

        new_node = Node(move, queue[0])
        queue[0].childrens.append(new_node)
        queue.append(new_node)
    
    return BFS(queue[1:])


def main():
    sys.setrecursionlimit(10**9)
    game = Game([[PLAYER, EMPTY, BLOCK, EMPTY, EMPTY], 
          [EMPTY, EMPTY, BLOCK, EMPTY, EMPTY], 
          [EMPTY, BLOCK, BLOCK, EMPTY, EMPTY], 
          [EMPTY, EMPTY, EMPTY, EMPTY, OBJECTIVE]], Point(3,4), Point(0,0))

    queue = [Node(game, None)]

    print(game)
    result = BFS(queue)
    print(result.value)
        
if __name__ == "__main__":
    main()
