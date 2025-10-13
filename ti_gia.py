import requests
import xml.etree.ElementTree as ET
import pandas as pd

def get_vcb_rates_all():
    xml_url = "https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx?b=10"
    resp = requests.get(xml_url)
    resp.encoding = 'utf-8'
    if resp.status_code != 200:
        print("Lỗi khi truy cập XML API:", resp.status_code)
        return None

    root = ET.fromstring(resp.text)

    data = []
    for ex in root.findall(".//Exrate"):
        data.append(ex.attrib) 

    return pd.DataFrame(data)

if __name__ == "__main__":
    df = get_vcb_rates_all()
    if df is not None and not df.empty:
        
        print(df.head())  
        df.to_csv("ty_gia_vcb_api_1.csv", index=False, encoding="utf-8-sig")
        print("Đã lưu vào file ty_gia_vcb_api.csv (không có EUR)")
    else:
        print("Không có dữ liệu hoặc truy vấn thất bại.")
