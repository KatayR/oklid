import math

# noktaları tanımlama
points = [(1,2 ), (3,4), (5,6), (7,8), (9,10)]

# mesafe için fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# mesafeleri hesağlama
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# minimum mesafenin bulunması
min_distance = min(distances)
print("Min mesafe:", min_distance)
