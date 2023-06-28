import re
import string


def vn_norm_text(text, english=False, rm_pun=False, low=True):
    import unicodedata
    import unidecode
    import string

    if text == None:
        text = ""
    text = str(text)
    # thay the nhieu spaces bang dau space
    text = re.sub('  +', ' ', text)
    # thay the ki tu dac biet bang khaong trang
    text = re.sub("[,.;@#?!&$]+", " ", text)
    text = re.sub("-", " ", text)

    vietnamletters = ["a", "á", "à", "ả", "ạ", "ã", "ă", "ắ", "ằ", "ẳ", "ặ", "ẵ",
                      "â", "ấ", "ầ", "ẩ", "ậ", "ẫ", "b", "c", "d", "đ", "e", "é", "è", "ẻ", "ẹ",
                      "ẽ", "ê", "ế", "ề", "ể", "ệ", "ễ", "f", "g", "h", "i", "í", "ì", "ỉ", "ị",
                      "ĩ", "j", "k", "l", "m", "n", "o", "ó", "ò", "ỏ", "ọ", "õ", "ô", "ố", "ồ",
                      "ổ", "ộ", "ỗ", "ơ", "ớ", "ờ", "ở", "ợ", "ỡ", "p", "q", "r", "s", "t", "u",
                      "ú", "ù", "ủ", "ụ", "ũ", "ư", "ứ", "ừ", "ử", "ự", "ữ", "v", "w", "x", "y",
                      "ý", "ỳ", "ỹ", "ỵ", "ỷ", "z", "A", "Á", "À", "Ả", "Ạ", "Ã", "Ă", "Ắ", "Ằ",
                      "Ẳ", "Ặ", "Ẵ", "Â", "Ấ", "Ầ", "Ẩ", "Ậ", "Ẫ", "B", "C", "D", "Đ", "E", "É",
                      "È", "Ẻ", "Ẹ", "Ẽ", "Ê", "Ế", "Ề", "Ể", "Ệ", "Ễ", "F", "G", "H", "I", "Í",
                      "Ì", "Ỉ", "Ị", "Ĩ", "J", "K", "L", "M", "N", "O", "Ó", "Ò", "Ỏ", "Ọ", "Õ",
                      "Ô", "Ố", "Ồ", "Ổ", "Ộ", "Ỗ", "Ơ", "Ớ", "Ờ", "Ở", "Ợ", "Ỡ", "P", "Q", "R",
                      "S", "T", "U", "Ú", "Ù", "Ủ", "Ụ", "Ũ", "Ư", "Ứ", "Ừ", "Ử", "Ự", "Ữ", "V",
                      "W", "X", "Y", "Ý", "Ỳ", "Ỷ", "Ỵ", "Ỹ", "Z", " ", "0", "1", "2", "3", "4",
                      "5", "6", "7", "8", "9"]

    if rm_pun == False:
        vietnamletters = list(vietnamletters + list(string.punctuation))
    text = unicodedata.normalize('NFC', text)
    text = "".join(i for i in text if i in vietnamletters).strip()
    text = " ".join(text.split())
    if low == True:
        text = text.lower()
    if english == True:
        text = unidecode.unidecode(text)
    else:
        list1 = ["oà", "oá", "oả", "oã", "oạ", "oè", "oé",
                 "oẻ", "oẽ", "oẹ", "uỳ", "uý", "uỷ", "uỹ", "uỵ"]
        list2 = ["òa", "óa", "ỏa", "õa", "ọa", "òe", "óe",
                 "ỏe", "õe", "ọe", "ùy", "úy", "ủy", "ũy", "ụy"]
        for i in range(15):
            text = text.replace(list1[i], list2[i])
    text = re.sub('  +', ' ', text)
    text = text.strip()
    text = ' ' + text + ' '
    return text


stop_words = ['thành phố', 'tỉnh', 'quận', 'huyện',
              'thị xã', 'phường', 'xã', 'thị trấn', 'chi cục thuế']
stop_words = stop_words + \
    [vn_norm_text(item, english=True).strip() for item in stop_words]


def rm_stopWord(text):
    for word in stop_words:
        text = ' ' + text + ' '
        w = ' ' + word + ' '
        text = re.sub(w, ' ', text)
    text = re.sub('  +', ' ', text)
    text = text.strip()
    text = ' ' + text + ' '
    return text


def rm_stopWord_fix(text):
    stop_words_fix = ['thành phố', 'tỉnh', 'quận', 'huyện',
                      'thị xã', 'phường', 'xã', 'thị trấn', 'chi cục thuế']
    for word in stop_words_fix:
        text = ' ' + text + ' '
        w = ' ' + word + ' '
        text = re.sub(w, ' ', text)
    text = re.sub('  +', ' ', text)
    text = text.strip()
    text = ' ' + text + ' '
    return text


def add_space(text):
    text = ' ' + text + ' '
    return text


def capitalize_first_letter(text):
    listText = str(text).lstrip().rstrip().split()
    capitalizedText = " "
    for item in listText:
        capitalizedText += item.capitalize() + " "
    return capitalizedText


if __name__ == "__main__":
    print(capitalize_first_letter(" thua thien hue "))
    print(stop_words)
