from random import shuffle



class Minesweep():
    def __init__(this):
        #images
        
        
        
        #creating bombs
        
        this.data=[]
        
        for l in range(81):
            
            if 10>l:
                this.data.append(-1)
                
            else:
                this.data.append(0)
                    
        shuffle(this.data)
        
        temp=[]
        
        for i in range(9):
            temp.append([])
            
            for j in range(9):
                temp[i].append(this.data[i*9+j])
                
        this.data=temp
        
        #creating numbers
        
        for i in range(9):
            for j in range(9):
                
                if this.data[i][j]!=-1:
                    sum=0
                    
                    for m in range(3):
                        for n in range(3):
                            
                            if not (m==1 and n==1) and i+m-1>-1 and j+n-1>-1:
                                try:
                                    if this.data[i+m-1][j+n-1]==-1:
                                        sum+=1
                                        
                                except:
                                    a=1
                                        
                    this.data[i][j]=sum
                    
        #hiding array
        this.ha=[]
        
        for i in range(9):
            this.ha.append([])
                           
            for j in range(9):
                this.ha[i].append(0)
                
        #check if over var
        
        this.over=False
        this.state="nothing"
                                            
    def display(this):
        this.mine=loadImage("assets/mine.jpg")
        this.tiles=loadImage("assets/tiles.png")
        this.flag=loadImage("assets/flag.png")
        
        s=700/9
    
        for i in range(9):
            for j in range(9):
                noFill()
                
                if this.data[i][j]==-1:
                    image(this.mine,i*s,j*s,s,s)
                    
                elif this.data[i][j]!=0:
                    textSize(s)
                    fill(0)
                    text(this.data[i][j],i*s+10,j*s+s-10)
                
                    noFill()
                    
                rect(i*s,j*s,s,s)
                
                if this.ha[i][j]==0 or this.ha[i][j]==2:
                    image(this.tiles,i*s,j*s,s,s)
                    
                if this.ha[i][j]==2:
                    image(this.flag,i*s,j*s,s,s)
                    
    def op(this,x,y):
        if mouseButton==LEFT and this.ha[x][y]!=2:
            this.ha[x][y]=1
            
            this.zer(x,y)
            
            if this.data[x][y]==-1:
                
                for i in range(9):
                    for j in range(9):
                        this.ha[i][j]=1
                        
                this.over=True
                this.state="lost"
                            
                this.gameover(this.state)  
                
            for l in range(81):
                j=l%9
                i=(l-j)/9
                            
                if this.data[i][j]==-1 and this.ha[i][j]==1:
                    break
                
                if this.data[i][j]!=-1 and this.ha[i][j]!=1:
                    break
                
                if l==80:
    
                    this.state="won"
                    this.gameover(this.state)
                    this.over=True
                

        if this.ha[x][y]!=1:
            if mouseButton==RIGHT and this.ha[x][y]!=2:
                this.ha[x][y]=2
                
            elif mouseButton==RIGHT:
                this.ha[x][y]=0
                
    def zer(this,x,y):
        if this.data[x][y]==0:
            this.ha[x][y]=1
            
            for m in range(3):
                    for n in range(3):
                        try:
                            if not (m==1 and n==1) and x+m-1>-1 and y+n-1>-1 and this.ha[x+m-1][y+n-1]!=1:
                                this.zer(x+m-1,y+n-1)
                                
                        except:
                            mns=1                               
        this.ha[x][y]=1                   
                
    def gameover(this,st):
                  
        if st=="lost":
            print("You lost!         Press r to restart.")
            
        elif st=="won":
            print("You won!         Press r to restart.")
