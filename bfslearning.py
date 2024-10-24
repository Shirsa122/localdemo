graph= {
        '5':['3','7'],
        '3':['2','4'],
        '7':['8'],
        '2':[],
        '4':['8'],
        '8':[]}

visited = []
queue =[]

def bfs(visited,queue, node):
    
    queue.append(node)
    visited.append(node)
    while queue:
        m = queue.pop(0) 
        print (m)  

        for neighbour in graph [m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append (neighbour)
                
                
print("Follow the breadth first search")
bfs(visited,queue, '5')            
print(visited)           
