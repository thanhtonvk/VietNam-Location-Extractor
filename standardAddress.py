import pandas as pd
import json
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from cleanText import text_clean, clearColumns

with open('./abbreviation.json') as f:
    provinceAbbreviation = json.load(f)


def normalizeAddress(listAddress):
    listTemp = [item for item in listAddress]
    for i in range(len(listTemp)):
        if (listTemp[i] in provinceAbbreviation):
            listTemp[i] = provinceAbbreviation[listTemp[i]]
    return listTemp


def addressList(provinceName):
    addressGoals = pd.read_csv(provinceName).astype(str)
    addressGoals["address"] = addressGoals['Phường Xã'] + ', ' + \
        addressGoals['Quận Huyện'] + ', ' + addressGoals['Tỉnh Thành Phố']
    return list(addressGoals["address"])


def loadAddressList(provinceName):
    addressGoals = pd.read_csv(provinceName)
    return set(list(addressGoals['Phường Xã']) + list(addressGoals['Quận Huyện']) + list(addressGoals['Tỉnh Thành Phố']))


def checkValidAddressElement(listTest, address):
    listTemp = normalizeAddress(listTest)
    length = len(listTemp)
    addressTemp = [text_clean(element) for element in address]
    minPoint = 100
    minIndex = 0
    pointTemp = 0
    i = 0
    for i in range(length):
        if len(listTemp[i]) > 10:
            pointTemp = process.extractOne(
                listTemp[i], addressTemp, scorer=fuzz.token_sort_ratio)[1]
        else:
            pointTemp = process.extractOne(
                listTemp[i], addressTemp, scorer=fuzz.token_set_ratio)[1]
        if pointTemp < minPoint:
            minPoint = pointTemp
            minIndex = i
        i += 1
    if minPoint < 90:
        listTemp[minIndex] = " "
        return listTemp
    else:
        return listTemp


def matchAddress(ls, matchStr):
    resultSet = process.extractOne(matchStr, ls, scorer=fuzz.token_set_ratio)
    resultSetString = resultSet[0]
    resultSetPoints = resultSet[1]
    resultSort = process.extractOne(matchStr, ls, scorer=fuzz.token_sort_ratio)
    resultSortString = resultSort[0]
    resultSortPoints = resultSort[1]
    if resultSortPoints > 90:
        resultString = resultSortString
        resultPoints = resultSortPoints
    else:
        resultString = resultSetString
        resultPoints = resultSetPoints
    return resultString, resultPoints
