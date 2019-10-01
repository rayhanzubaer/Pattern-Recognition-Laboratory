import arff
import math
import operator


def euclideanDistance(instanceOne, instanceTwo, length):
    distance = 0
    for i in range(length):
        distance += math.pow(instanceOne[i] - instanceTwo[i], 2)
    return math.sqrt(distance)


def getNeighbors(trainingInstances, testingInstance, k):
    distances = []
    for trainingInstance in trainingInstances:
        currentDistance = euclideanDistance(trainingInstance, testingInstance, len(trainingInstance) - 1)
        distances.append((trainingInstance, currentDistance))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors


def getResponse(neighbors, k):
    total = 0
    for neighbor in neighbors:
        total += neighbor[-1]
    return total / k


def meanAbsoluteError(testingInstances, predictions):
    total = 0
    for i in range(len(testingInstances)):
        total += abs(predictions[i] - testingInstances[i][-1])
    return total / len(testingInstances)


def main():
    trainingInstances = arff.load(open('wine_train.arff', 'r'))['data']
    testingInstances = arff.load(open('wine_test.arff', 'r'))['data']
    k = int(input('Enter Value of K : '))
    print("K value: %d" % k)
    predictions = []
    for testingInstance in testingInstances:
        neighbors = getNeighbors(trainingInstances, testingInstance, k)
        result = getResponse(neighbors, k)
        predictions.append(result)
        print("Predicted Value: %f    Actual Value: %f" % (result, testingInstance[-1]))
    print("Mean absolute error : %f" % meanAbsoluteError(testingInstances, predictions))
    print("Total number of instances: %d" % len(testingInstances))


main()
