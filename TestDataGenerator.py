
# coding: utf-8

# In[130]:


import numpy as np


# In[131]:


def generateDataPoints(count, dimensions, coordSize):
    datapoints = np.random.rand(count, dimensions) * coordSize
    return datapoints


# In[132]:


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
    
    return distances, datapoints


# In[133]:


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
    
    return distances, datapoints


# In[ ]:





