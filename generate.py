import numpy as np

def genHeightMap(xp=10, yp=10, passes=1):
    '''
    Parameters:
        xp, yp: dimentions of map, default 10 (int)
        passes: number of passes, default 1 (int)

    Returns:
        arr: generated map (numpy ndarray)
    '''
    arr = np.random.rand(xp, yp)
    for i in range(1,passes+1):
        for y in range(1,yp-1, 1):
            for x in range(1, xp-1, 1):
                arr[x,y] = 0.25 * np.sum([arr[x-1, y], arr[x, y-1], arr[x, y+1], arr[x+1, y]])
    return arr

def remEdges(arr):
    for y in range(0, arr.shape[1]):
        for x in range(0, arr.shape[0]):
            if (x == 0 or y == 0 or x == arr.shape[0] or x == arr.shape[1]):
                arr[x,y] = 0
            
    return arr
