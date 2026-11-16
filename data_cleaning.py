import pandas as pd
from pandas._config.config import is_callable

df = pd.read_csv("/home/amorntep/hotel-booking-cancellation-analysis/data/hotels.csv")
df["hotel"].unique()
pd.set_option("display.max_columns", None)
df.sample(20)
df.describe()
print(df["hotel"].unique())
# 1. อัตรายกเลิกของแต่ละโรงแรม ช่องทางจอง (`distribution_channel`) และกลุ่มลูกค้า (`market_segment`) เป็นเท่าไหร่ — ต้องรายงาน **จำนวนการจองของแต่ละกลุ่มคู่กับอัตราเสมอ** เพราะกลุ่มที่อัตราสูงแต่มีการจองไม่กี่ร้อยรายการไม่คุ้มที่จะลงมือแก้
# หรือก็คือเอาการจองมา-ลูกค้าที่ยกเลิก
result = df.groupby("hotel").agg(
    booking=("is_canceled", "count"), cancel=("is_canceled", "mean")
)
print(result)
city_cancel = result.loc["City Hotel", "cancel"]
resort_cancel = result.loc["Resort Hotel", "cancel"]
print(f"จากโจทย์ข้อแรกอัตราการยักเลิกการจองขอแต่ละ Hotel คือ\nอัตราการยกเลิกการจองของ City Hotel : {city_cancel*100:.2f}% \nอัตราการยกเลิกการจองของ Resort Hotel : {resort_cancel*100:.2f}%")
)
#NOTE: โจทย์ข้อสอง
df['lead_group']=pd.cut(df['lead_time'],
    bins=[-1,7,14,30,60,90,180,365,800],
    labels=['0-7','8-14','15-30','31-60','61-90','91-180','181-365','366+']
                                                                 )
result2=df.groupby(['hotel','lead_group'],observed=True).agg(
    booking=('is_canceled','count') ,
    cancel=('is_canceled','mean')

)
print(result2)

city = result2.loc['City Hotel']
city_above = city['cancel'] > city_cancel
print(city_above)
print(f"City Hotel: อัตรายกเลิกเพิ่มจาก {city['cancel'].iloc[0]*100:.2f}% (0-7 วัน) เป็น {city['cancel'].iloc[-1]*100:.2f}% (366+ วัน)")
print(f"City Hotel: เริ่มเสี่ยงที่ช่วง {city_above.idxmax()} วัน (สูงกว่าค่าเฉลี่ย {city_cancel*100:.2f}%)")

resort = result2.loc['Resort Hotel']
resort_above = resort['cancel'] > resort_cancel
print(resort_above)
print(f"Resort Hotel: อัตรายกเลิกเพิ่มจาก {resort['cancel'].iloc[0]*100:.2f}% (0-7 วัน) เป็น {resort['cancel'].iloc[-1]*100:.2f}% (366+ วัน)")
print(f"Resort Hotel: เริ่มเสี่ยงที่ช่วง {resort_above.idxmax()} วัน (สูงกว่าค่าเฉลี่ย {resort_cancel*100:.2f}%)")
#NOTE:3. ประเภทมัดจำ (`deposit_type`) สัมพันธ์กับการยกเลิกอย่างไร
print(df['deposit_type'].unique())
cancel_deposit=df.groupby('deposit_typel').agg(
    booking=('is_canceled','count'),
    cancel=('is_canceled','mean')
)
print(cancel_deposit)
