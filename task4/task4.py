import pandas as pd
import numpy
import math
import openpyxl

# Step 6

# Function to calculate distance between two points
def distance2Point(inputLat1, inputLon1, inputLat2, inputLon2):
    # Convert inputs into floats, which can accept decimal point for lat and long
    lat1 = float(inputLat1)
    lon1 = float(inputLon1)
    lat2 = float(inputLat2)
    lon2 = float(inputLon2)
    R = 6371 # earth's radius
    # haversine formula below via numpy and math module
    radLat1 = lat1 * (numpy.pi) / 180
    radLat2 = lat2 * (numpy.pi) / 180
    diffLat = (lat2 - lat1) * (numpy.pi) / 180
    diffLong = (lon2 - lon1) * (numpy.pi) / 180
    a = numpy.sin(diffLat / 2) * numpy.sin(diffLat / 2) + numpy.cos(radLat1) * numpy.cos(radLat2) * numpy.sin(diffLong / 2) * numpy.sin(diffLong / 2)
    c = 2 * math.atan((math.sqrt(a)) / (math.sqrt(1 - a)))
    d = R * c  # distance
    # gives an output for distance between two points
    return d

# step 7

# reads to excel sheets from account location and store location
accountLocation = pd.read_excel("Backup.xlsx", header=None)
storeLocationData = pd.read_excel("locations.xlsx", header=None)

# Calculates the distance of each account between all the possible store
storeDistanceFromAccount = [[] for _ in range(len(storeLocationData.index))]
for i in range(0, len(accountLocation.index)):
    for j in range(0, len(storeLocationData.index)):
        currentDistance = distance2Point(accountLocation.iloc[i, 2], accountLocation.iloc[i, 3], storeLocationData.iloc[j, 1], storeLocationData.iloc[j, 2])
        storeDistanceFromAccount[j].append(currentDistance)

# Estimates the income of each Account's Men/Women/Children purchase total with the probability of visiting all the possible stores.
estimatedIncome = [[0 for _ in range(3)] for _ in range(len(storeLocationData.index))]
for a in range(0, 3):
    for b in range(0, len(storeDistanceFromAccount)):
        for c in range(0, len(accountLocation.index)):
            currentCityDistance = storeDistanceFromAccount[b][c]
            sizeAccountTotal = accountLocation.iloc[c, a + 4]
            if currentCityDistance <= 5:
                estimatedSizeAccountTotal = (sizeAccountTotal*1).round(2)
                estimatedIncome[b][a] = float("{:.2f}".format(estimatedIncome[b][a] + estimatedSizeAccountTotal))
            elif 5 < currentCityDistance <= 10:
                estimatedSizeAccountTotal = (sizeAccountTotal*0.7).round(2)
                estimatedIncome[b][a] = float("{:.2f}".format(estimatedIncome[b][a] + estimatedSizeAccountTotal))
            elif 10 < currentCityDistance <= 15:
                estimatedSizeAccountTotal = (sizeAccountTotal*0.4).round(2)
                estimatedIncome[b][a] = float("{:.2f}".format(estimatedIncome[b][a] + estimatedSizeAccountTotal))
            elif 15 < currentCityDistance <= 25:
                estimatedSizeAccountTotal = (sizeAccountTotal*0.1).round(2)
                estimatedIncome[b][a] = float("{:.2f}".format(estimatedIncome[b][a] + estimatedSizeAccountTotal))
            else:
                estimatedSizeAccountTotal = (sizeAccountTotal*0).round(2)
                estimatedIncome[b][a] = float("{:.2f}".format(estimatedIncome[b][a] + estimatedSizeAccountTotal))
for i in range(0,len(storeLocationData)):
    estimatedIncome[i].insert(0, storeLocationData.iloc[i, 0])
estimatedIncomeDataFrame = pd.DataFrame(estimatedIncome)
# Saves all data into excel sheet called "income.xlsx"
estimatedIncomeDataFrame.to_excel("Income.xlsx", index=False, header=False)

# Step 8

# Prints the best possible location by total estimated income
estimatedIncomeDataFrame['Total'] = estimatedIncomeDataFrame[list(estimatedIncomeDataFrame.columns)].sum(axis=1, numeric_only=True)
print(estimatedIncomeDataFrame.nlargest(3, "Total", keep='first'))