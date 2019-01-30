
# coding: utf-8

# In[77]:


import numpy as np


# In[78]:


def generateDataPoints(count, dimensions, coordSize):
    datapoints = np.random.rand(count, dimensions) * coordSize
    return datapoints


# In[79]:


def generateIO(dataCount, sensorCount, dimensions, coordSize):
    sensors = generateDataPoints(sensorCount, dimensions, coordSize)
    datapoints = generateDataPoints(dataCount, dimensions, coordSize)
    return calculateIO(datapoints, sensors)


# In[80]:


def generateStatic4PointIO(dataCount, dimensions, coordSize):
    sensors = [[0.0,0.0], [0.0, coordSize], [coordSize, 0.0], [coordSize, coordSize]]
    datapoints = generateDataPoints(dataCount, dimensions, coordSize)
    return calculateIO(datapoints, sensors)


# In[81]:


def generateFromSensors(dataCount, dimensions, coordSize, sensors):
    datapoints = generateDataPoints(dataCount, dimensions, coordSize)
    return calculateIO(datapoints, sensors)


# In[82]:


def calculateIO(datapoints, sensors):
    distances = []
    points = [[] for x in range(len(datapoints[0]))]
    
    for i in range(len(datapoints)):
        distancevector = sensors - datapoints[i]
        distance = []
        for j in range(len(distancevector)):
            distance.append(np.linalg.norm(distancevector[j]))
        
        for k in range(len(datapoints[i])): 
            points[k].append(np.array(datapoints[i][k]))

        distances.append(distance)
    distances = np.array(distances)
    return distances, points, sensors

