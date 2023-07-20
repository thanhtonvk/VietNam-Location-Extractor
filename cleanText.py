import unicodedata
import unidecode
vietnamletters = ["a", "á", "à", "ả", "ạ", "ã", "ă", "ắ", "ằ", "ẳ", "ặ", "ẵ", "â", "ấ", "ầ", "ẩ", "ậ", "ẫ", "b",
                  "c", "d", "đ", "e", "é", "è", "ẻ", "ẹ", "ẽ", "ê", "ế", "ề", "ể", "ệ", "ễ", "f", "g", "h", "i",
                  "í", "ì", "ỉ", "ị", "ĩ", "j", "k", "l", "m", "n", "o", "ó", "ò", "ỏ", "ọ", "õ", "ô", "ố", "ồ",
                  "ổ", "ộ", "ỗ", "ơ", "ớ", "ờ", "ở", "ợ", "ỡ", "p", "q", "r", "s", "t", "u", "ú", "ù", "ủ", "ụ",
                  "ũ", "ư", "ứ", "ừ", "ử", "ự", "ữ", "v", "w", "x", "y", "ý", "ỳ", "ỹ", "ỵ", "ỷ", "z",
                  "A", "Á", "À", "Ả", "Ạ", "Ã", "Ă", "Ắ", "Ằ", "Ẳ", "Ặ", "Ẵ", "Â", "Ấ", "Ầ", "Ẩ", "Ậ", "Ẫ", "B",
                  "C", "D", "Đ", "E", "É", "È", "Ẻ", "Ẹ", "Ẽ", "Ê", "Ế", "Ề", "Ể", "Ệ", "Ễ", "F", "G", "H", "I",
                  "Í", "Ì", "Ỉ", "Ị", "Ĩ", "J", "K", "L", "M", "N", "O", "Ó", "Ò", "Ỏ", "Ọ", "Õ", "Ô", "Ố", "Ồ",
                  "Ổ", "Ộ", "Ỗ", "Ơ", "Ớ", "Ờ", "Ở", "Ợ", "Ỡ", "P", "Q", "R", "S", "T", "U", "Ú", "Ù", "Ủ", "Ụ",
                  "Ũ", "Ư", "Ứ", "Ừ", "Ử", "Ự", "Ữ", "V", "W", "X", "Y", "Ý", "Ỳ", "Ỷ", "Ỵ", "Ỹ", "Z", " ",
                  "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", ".", ","]


def text_clean(text):
    text = unicodedata.normalize('NFC', text)
    text = "".join(i for i in text if i in vietnamletters).strip()
    text = " ".join(text.split())
    text = text.upper()
    text = unidecode.unidecode(text)
    return text


def clearColumns(data):
    clearProvinceName = ['TINHTP',"TINH ", "T.",
                         "THANH PHO ", "THANHPHO ", "TP ", "TP."]
    clearDistrictName = ['QUANHUYEN',"HUYEN ", "H.", ' Q ','Q ',"QUAN ", "Q.", "THANH PHO ",
                         "THANHPHO ", "TP ", "TP.", "TX.", "TX", "THI XA", "THI XA."]
    clearCivilName = ['PHUONGXA',"XA ", "X.", "XA.", "PHUONG ", " P.", " P-", " P ",
                      "X .", "TT.", "TT ", "T.T",  "THI TRAN", "F.", "F "]
    clearListName = []
    dataAnalysis = data
    clearListName = clearProvinceName + clearDistrictName + clearCivilName
    # clearListName = set(clearListName)
    # print(clearListName)
    for item in clearListName:
        if item=='PHUONG ' or item =='XA ' or item=='QUAN ' or item=='TINH ':
            dataAnalysis = dataAnalysis.replace(item, "",1)
        else:
            dataAnalysis = dataAnalysis.replace(item, "")
    return dataAnalysis.lstrip().rstrip()
