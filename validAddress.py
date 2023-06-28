import pandas as pd
import unidecode


def load_address():
    df = pd.read_csv('data/provinceLib.csv')
    provinces = df['Tỉnh Thành Phố']
    districts = df['Quận Huyện']
    wards = df['Phường Xã']
    address = {}
    for i in range(len(df)):
        province = unidecode.unidecode(provinces[i]).upper()
        district = unidecode.unidecode(districts[i]).upper()
        ward = unidecode.unidecode(wards[i]).upper()

        if not province in address.keys():
            address[province] = {}
            address[province][district] = []
        else:
            if not district in address[province].keys():
                address[province][district] = []
                address[province][district].append(ward)
            else:
                address[province][district].append(ward)
    return address


class ValidAddress:

    address = load_address()

    def check_province(self, full_address):
        result = None
        address_list = full_address.split(',')
        for add in address_list:
            add = add.strip().upper()
            if add in self.address.keys():
                result = add
                full_address = full_address.replace(add, '')
                break
        return full_address, result

    def check_district(self, full_address, province):
        result = None
        address_list = full_address.split(',')
        for add in address_list:
            add = add.strip().upper()
            if add in self.address[province].keys():
                result = add
                full_address = full_address.replace(add, '')
                break
        return full_address, result

    def check_ward(self, full_address, province, district):
        result = None
        address_list = full_address.split(',')
        for add in address_list:
            add = add.strip().upper()
            if add in self.address[province][district]:
                result = add
                full_address = full_address.replace(add, '')
                break
        return full_address, result

    def valid_address(self, address_text):
        full_address, province = self.check_province(address_text)
        if province == None:
            return {'province': None, 'district': None, 'ward': None}
        else:
            full_address, district = self.check_district(
                full_address, province)
            if district == None:
                return {'province': province, 'district': district, 'ward': None}
            else:
                full_address, ward = self.check_ward(
                    full_address, province, district)
                return {'province': province, 'district': district, 'ward': ward}
