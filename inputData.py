import pandas as pd
import numpy as np
from cleanText import text_clean, clearColumns
import json
textTest = ". KHU PHO TAN BINH P.TAN BINH HUYEN DONG XOAI BINH PHUOC"
filename = "data/provinceLib.csv"
renameObject = {
    "Tỉnh Thành Phố": "province",
    "Quận Huyện": "district",
    "Phường Xã": "civil",
    "Cấp": "civil_level"
}
with open('./abbreviation.json') as f:
    provinceAbbreviation = json.load(f)
df = pd.read_csv(filename)
df = df.rename(index=str, columns=renameObject)


def parseLocation():
    provinceList = [text_clean(item) for item in df["province"].unique()]
    districtList = [text_clean(item) for item in df["district"].unique()]
    civilList = [text_clean(item) for item in df["civil"].unique()]
    return provinceList, districtList, civilList

provinceList, districtList, civilList = parseLocation()
def textTransfer(text):
    listTemp = text.split()
    for i in range(len(listTemp)):
        if (listTemp[i] in provinceAbbreviation):
            listTemp[i] = provinceAbbreviation[listTemp[i]]
    text = ' '.join(listTemp)
    textTemp = text_clean(text)
    textFinal = textTemp
    for item in provinceList:
        if (item in textTemp):
            textTemp = textTemp.replace(item, "")
            textFinal = textFinal.replace(item, ","+item)
            break
    for item in districtList:
        if (item in textTemp):
            textTemp = textTemp.replace(item, "")
            textFinal = textFinal.replace(item, ","+item)
            break
    for item in civilList:
        if (item in textTemp):
            textTemp = textTemp.replace(item, "")
            textFinal = textFinal.replace(item, ","+item)
            break
    return clearColumns(textFinal)


if __name__ == "__main__":
    provinceList, districtList, civilList = parseLocation()
    print(textTransfer('TO 1 TAN LAP-PHUONG PHUONG DONG-THANH PHO UONG BI-TINH QUANG NINH-VIET NAM'))
