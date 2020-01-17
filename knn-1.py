import pandas as pd
import numpy as np
import operator


def euclidean_dist(data1, data2, length ):
    distance = 0;
    for i in range(length):
        distance += pow((data1[i] - data2[i]),2)
    return np.sqrt(distance)

#data_a = [2,2,2,'a']
#data_b = [4,4,4,'b']

#dist = euclidean_dist(data_a,data_b,3)

#print(dist)


def get_neighbors(train, test, k):
    
    length = len(test)-1
    distance = []
        
    for i in range(len(train)):
        dist = euclidean_dist(test, train[i], length)
        distance.append([train[i],dist])
            
    distance.sort(key=operator.itemgetter(1))
    
    #print(distance)
    
    neighbors = []

    for x in range(k):
        neighbors.append(distance[x][0])
    
    return neighbors



def get_class(neighbors):
    
    classVotes = {}

    for x in range(len(neighbors)):
        response = neighbors[x][3]
        
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
        
    print("Selecting majority class : ",classVotes)

    #classVotes = sorted(classVotes.values(),reverse=True)
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)

    return sortedVotes[0][0]

#data = pd.read_csv('iris.csv')

#print(data.head(5))

#k=3
#testSet = [[7.2, 3.6, 5.1, 2.5]]
#test = pd.DataFrame(testSet)
#print(test)

#neighbor = [[2,2,2,'a'],[3,3,3,'b'],[4,4,4,'b']]

#neighbors = get_neighbors(data,test,k)

#print(neighbors)
    
train = [[3,3,3,'a'],[7,7,7,'b'],[4,4,4,'a'],[6,6,6,'b'],[2,2,2,'a']]
test = [5,5,5]
k=3
neighbors = get_neighbors(train,test,k)

print(neighbors)

class1 = get_class(neighbors)

print("Predicted class of ",test," is : ",class1)