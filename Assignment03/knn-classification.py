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


def getClass(neighbors):
    votes = {}
    for neighbor in neighbors:
        currentClass = neighbor[-1]
        if currentClass in votes:
            votes[currentClass] += 1
        else:
            votes[currentClass] = 1
    votesSorted = sorted(votes.items(), key=operator.itemgetter(1), reverse=True)
    return votesSorted[0][0]


def correctlyClassifiedInstances(testingInstances, predictions):
    correct = 0
    for i in range(len(testingInstances)):
        if testingInstances[i][-1] == predictions[i]:
            correct += 1
    return correct


def main():
    trainingInstances = arff.load(open('yeast_train.arff', 'r'))['data']
    testingInstances = arff.load(open('yeast_test.arff', 'r'))['data']
    k = int(input('Enter Value of K : '))
    print("K value: %d" % k)
    predictions = []
    for testingInstance in testingInstances:
        neighbors = getNeighbors(trainingInstances, testingInstance, k)
        result = getClass(neighbors)
        predictions.append(result)
        print("Predicted class: %s    Actual class: %s" % (result, testingInstance[-1]))
    numberOfCorrectInstances = correctlyClassifiedInstances(testingInstances, predictions)
    numberOfTotalInstances = len(testingInstances)
    print("Number of correctly classified instances: %d" % numberOfCorrectInstances)
    print("Total number of instances: %d" % numberOfTotalInstances)
    print("Accuracy : %f" % (numberOfCorrectInstances / numberOfTotalInstances))


main()
