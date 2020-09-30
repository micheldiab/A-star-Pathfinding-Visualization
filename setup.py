
columns = 50
rows = 50
class point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.neighbors=[]
        self.wall=False

    def add_neighbor(self,grid):
        if(self.x<columns-1 and grid[self.x +1][self.y].wall==False):
            self.neighbors.append(grid[self.x +1][self.y])

        if(self.x>0 and grid[self.x - 1][self.y].wall==False):
            self.neighbors.append(grid[self.x - 1][self.y])

        if(self.y<rows-1 and grid[self.x][self.y+1].wall==False):
            self.neighbors.append(grid[self.x][self.y+1])

        if(self.y>0 and grid[self.x][self.y-1].wall==False):
            self.neighbors.append(grid[self.x][self.y - 1])

grid = [[j for j in range(rows)] for i in range(columns)]
for i in range(rows):
    for j in range(columns):
        grid[i][j]=point(i,j)
