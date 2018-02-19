'''
Source - https://www.geeksforgeeks.org/k-nearest-neighbours/

Algorithm
Let m be the number of training data samples. Let p be an unknown point.

Store the training samples in an array of data points arr[]. This means each element of this array represents a tuple (x, y).
for i=0 to m:
  Calculate Euclidean distance d(arr[i], p).
Make set S of K smallest distances obtained. Each of these distances correspond to an already classified data point.
Return the majority label among S.

'''
import math
def euclidean_distance(data_point_1,data_point_2):
    return math.sqrt((data_point_1[0]-data_point_2[0])**2 + (data_point_1[1]-data_point_2[1])**2)


def knn(dict_data_points,to_be_classified_data_point,k):

    distances_group = []

    for group in dict_data_points:
        for feature in dict_data_points[group]:
            distances_group.append((euclidean_distance(feature,to_be_classified_data_point),group))

    sorted_distances_group = sorted(distances_group)[:k]

    freq1 = 0
    freq2 = 0
    for d in sorted_distances_group:
        if d[1] == 0:
            freq1 += 1
        elif d[1] == 1:
            freq2 += 1
    return 0 if freq1 > freq2 else 1



dict_data_points = {0:[(1,12),(2,5),(3,6),(3,10),(3.5,8),(2,11),(2,9),(1,7)],
              1:[(5,3),(3,2),(1.5,9),(7,2),(6,1),(3.8,1),(5.6,4),(4,2),(2,5)]}
new_data_point = (2.5,7)
k_nearest_neighbor_value = 3
print(knn(dict_data_points,new_data_point,k_nearest_neighbor_value))