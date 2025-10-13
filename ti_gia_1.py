import requests
import xml.etree.ElementTree as ET
import pandas as pd

def get_vcb_rates_from_xml():
    xml_url = "https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx?b=10"
    resp = requests.get(xml_url)
    resp.encoding = 'utf-8'
    if resp.status_code != 200:
        print("Lỗi khi truy cập XML API:", resp.status_code)
        return None

    xml_text = resp.text
    root = ET.fromstring(xml_text)

    data = []
    for ex in root.findall(".//Exrate"):
        data.append(ex.attrib)

    return pd.DataFrame(data)

if __name__ == "__main__":
    df = get_vcb_rates_from_xml()
    if df is not None and not df.empty:
        print(df)
        df.to_excel("ty_gia_vcb_2.csv", index=False, engine="openpyxl")
        print("Đã lưu vào file ty_gia_vcb.xlsx")
    else:
        print("Không có dữ liệu hoặc truy vấn thất bại.")
