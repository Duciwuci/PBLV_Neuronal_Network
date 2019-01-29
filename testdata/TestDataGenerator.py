
# coding: utf-8

# In[60]:


import numpy as np


# In[61]:


def generateDataPoints(count, dimensions, coordSize):
    datapoints = np.random.rand(count, dimensions) * coordSize
    return datapoints


# In[62]:


def generateIO(dataCount, sensorCount, dimensions, coordSize):
    sensors = generateDataPoints(sensorCount, dimensions, coordSize)
    datapoints = generateDataPoints(dataCount, dimensions, coordSize)
    distances = []
    
    
    for i in range(len(datapoints)):
        distancevector = sensors - datapoints[i]
        distance = []
        for j in range(len(distancevector)):
            distance.append(np.linalg.norm(distancevector[j]))
        
        distances.append(distance)
        
    distances = np.array(distances)
    return distances, datapoints, sensors


# In[63]:


def generateStatic4PointIO(dataCount, dimensions, coordSize):
    sensors = [[0.0,0.0], [0.0, coordSize], [coordSize, 0.0], [coordSize, coordSize]]
    datapoints = generateDataPoints(dataCount, dimensions, coordSize)
    distances = []
    
    
    for i in range(len(datapoints)):
        distancevector = sensors - datapoints[i]
        distance = []
        for j in range(len(distancevector)):
            distance.append(np.linalg.norm(distancevector[j]))
        
        distances.append(distance)
    distances = np.array(distances)
    return distances, datapoints, sensors

