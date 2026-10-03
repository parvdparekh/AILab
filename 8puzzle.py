def solve(stack,visited,goal):
    if not stack:   return None
    curr=stack.pop()
    if curr==goal:  return curr
    moves=[
        [1,3],[0,2,4],[1,5],
        [0,4,6],[1,3,5,7],[2,4,8],
        [3,7],[4,6,8],[5,7]]
    ind=curr.index(0)
    combinations=[]
    for i in range(len(moves[ind])):
        x=curr.copy()
        x[moves[ind][i]],x[ind]=x[ind],x[moves[ind][i]]
        if x not in visited:
            stack+=[x]
            visited+=[x]
    return solve(stack,visited,goal)
        
initial=[]
print('Enter initial state ')
for i in range(9):
    initial+=[int(input('Enter number '))]
goal=[]
print('Enter goal state ')
for i in range(9):
    goal+=[int(input('Enter number '))]
stack=[initial]
visited=[initial]
solved=solve(stack,visited,goal)
for i in range(9):
    if i%3==2:
        print(solved[i])
    else:
        print(solved[i],end=' ')