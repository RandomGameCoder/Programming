class Node:
    PARENT = None
    def __init__(self, state, cost):
        self.STATE = state
        self.PATH_COST = cost
    
    def set_parent(self, node):
        self.PARENT = node

class Problem:
    
    INITIAL_STATE = [
        [ '5', '7', '3' ],
        [ '4', ' ', '2' ],
        [ '8', '1', '6' ],
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

def child_node(problem: Problem, node: Node, action):
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
    child = Node(state, node.PATH_COST+1)
    child.set_parent(node)
    return child    

if __name__ == "__main__":
    p = Problem()
    state = []
    for i in p.INITIAL_STATE:
        state.append(i.copy())
    n = Node(state, 0)
    child = child_node(p,n,'l')
    print(p.INITIAL_STATE, n.STATE, child.STATE, sep = '\n')