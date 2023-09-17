class Node:
    PARENT = None
    def __init__(self, state, cost, parent):
        self.STATE = state
        self.PATH_COST = cost
        self.PARENT = parent

class Problem:
    
    INITIAL_STATE = [
        [ '4', '6', '1' ],
        [ '5', ' ', '3' ],
        [ '2', '7', '8' ],
    ]
    
    FINAL_STATE = [
        [ '1', '2', '3' ],
        [ '4', '5', '6' ],
        [ '7', '8', ' ' ]
    ]
    
    def GOAL_TEST(self, STATE: list):
        if STATE == self.FINAL_STATE:
            return True
        return False

    def ACTIONS(self, STATE: list):
        a = ['l', 'r', 'u', 'd']
        bi, bj = 0, 0
        for i in STATE:
            if ' ' in i:
                bi = STATE.index(i)
                bj = i.index(' ')
        if bi == 0:
            a.remove('u')
        elif bi == 2:
            a.remove('d')
        if bj == 0:
            a.remove('l')
        elif bj == 2:
            a.remove('r')
        return a

def child_node(node: Node, action):
    state = []
    bi = bj = 0
    for i in node.STATE:
        state.append(i.copy())
        if ' ' in i:
            bi = node.STATE.index(i)
            bj = i.index(' ')
    if action == 'l':
        state[bi][bj-1], state[bi][bj] = state[bi][bj], state[bi][bj-1]
    elif action == 'r':
        state[bi][bj+1], state[bi][bj] = state[bi][bj], state[bi][bj+1]
    elif action == 'u':
        state[bi-1][bj], state[bi][bj] = state[bi][bj], state[bi-1][bj]
    else:
        state[bi+1][bj], state[bi][bj] = state[bi][bj], state[bi+1][bj]
    child = Node(state, node.PATH_COST+1, node)
    return child    

def solution(node):
    l = [node]
    while node.PARENT!=None:
        l.append(node.PARENT)
        node = node.PARENT
    return l

def DFS(problem):
    state = []
    for i in problem.INITIAL_STATE:
        state.append(i.copy())
    node = Node(state, 0, None)
    if problem.GOAL_TEST(node.STATE):
        return solution(node)
    frontier = [node]
    explored = []
    while frontier!=[]:
        node = frontier.pop()
        explored.append(node.STATE)
        for action in problem.ACTIONS(node.STATE):
            child = child_node(node, action)
            for i in frontier:
                if child.STATE == i.STATE:
                    break
            else:
                if child.STATE not in explored:
                    if problem.GOAL_TEST(child.STATE):
                        return solution(child)
                    frontier.append(child)
    return None

p = Problem()
s = DFS(p)
for i in s[::-1]:
    print(i.STATE)