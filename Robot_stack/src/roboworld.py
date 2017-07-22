'''
Created on 22 Jul 2017

@author: annub
'''
#from pprint import pprint
import re

def create_world(filename):
    
    buffer=open(filename).read()
    lines=buffer.splitlines()
    numbers=[] # numbers to be stored in a list.
    numbers+=re.findall("[-\d]+",lines[0])
    x=int(numbers[0])
    y=int(numbers[1])
    
    
    a2d = [ [0]*x for _ in range(y)]
    for i in range(1,len(lines)):
        wall=[]
        robot=[]
        goal=[]
        value=lines[i].strip().split()
        if value[0]=='w':
            for j in range(0,len(value)):
                wall+=re.findall("[-\d]+",value[j])
            wx=int(wall[0])
            wy=int(wall[1])
            a2d[wx][wy]=1
        if value[0]=="r2d2":
            for j in range(0,len(value)):
                robot+=re.findall("[-\d]+",value[j])
            rx=int(robot[2])
            ry=int(robot[3])
        if value[0]=="goal":
            for j in range(0,len(value)):
                goal+=re.findall("[-\d]+",value[j])
            gx=int(goal[0])
            gy=int(goal[1])
    e=rx
    f=ry
    r2d2 = a2d[e][f]
    a2d[e][f]='r'
    goal=a2d[gx][gy]
    a2d[gx][gy]='g'
    return a2d

# to get the location of the robot.
def where_is_robot(a2d):
    l=len(a2d)
    for i in range(l):
        for j in range(l):
            if(a2d[i][j]=='r'):
                n=[i,j]
                break;
    return n

    
# to move the robot.                          
def move_robot(x,y,a2d):
    r=where_is_robot(a2d)
    a2d[r[0]][r[1]]='p'
    a2d[x][y]='r'
    return a2d 


#
def goals_reached(a2d):

    for i in range(0,len(a2d)):
        for j in range(0,len(a2d[0])):
            if(a2d[i][j]=='g'):
                goals=[i,j]
                return False
                break
    return True        
                


def is_feasible(new_x,new_y,a2d):
    n = where_is_robot(a2d)
    p=len(a2d)
    q=len(a2d[0])
    
    
    if(0<=new_x<p and 0<=new_y<q):
        if((new_x==n[0] and new_y!=n[1])or(new_x!=n[0] and new_y==n[1])):
            if(a2d[new_x][new_y]==1 or a2d[new_x][new_y]=='p'):
                return False
            else:
                return True
        else:
            return False
    else:
        return False
    
    
def is_feasible2(new_x,new_y,a2d):
    n = where_is_robot(a2d)
    p=len(a2d)
    q=len(a2d[0])
    
    
    if(0<=new_x<p and 0<=new_y<q):
        if((new_x==n[0] and new_y!=n[1])or(new_x!=n[0] and new_y==n[1])):
            if(a2d[new_x][new_y]==1):
                return False
            else:
                return True
        else:
            return False
    else:
        return False
    
