import pandas as pd

df = pd.read_csv("/home/amorntep/hotel-booking-cancellation-analysis/data/hotels.csv")
df.info()
pd.set_option("display.max_columns", None)
df.sample(20)
df.describe()
# ===== ขั้น 0: Base Cleaning (ทำครั้งเดียว มีผลกับทุกคำถาม -> แก้ df หลักได้) =====
# NOTE: 1) จัดการค่าว่าง  2) ตัดสินใจเรื่องแถวซ้ำ 31,994 แถว (ยังไม่ตัดสินใจ)

# ===== Loop 1: โจทย์ข้อ 1 =====
# NOTE: อัตรายกเลิกของแต่ละโรงแรม / distribution_channel / market_segment เป็นเท่าไหร่
#       ผลลัพธ์ต้องมี "จำนวนการจอง" คู่กับ "อัตรายกเลิก" เสมอ ไม่งั้นตัดสินใจไม่ได้
#
# A (ใช้คำนวณคำตอบข้อนี้):
#     'hotel', 'is_canceled', 'distribution_channel', 'market_segment'
# B (ใช้ตรวจว่าคำตอบเชื่อได้):
#     'reservation_status'                        -> is_canceled ตรงกับสถานะจริงไหม (No-Show นับยังไง)
#     'arrival_date_year', 'arrival_date_month'   -> ข้อมูลมีแค่ ก.ค.2015-ส.ค.2017 ปีไม่ครบ สัดส่วนอาจเอียง
#     'agent', 'company'                          -> สอดคล้องกับ distribution_channel ไหม
# C (ยังไม่ใช้ใน loop นี้):
#     ที่เหลือทั้งหมด -- 'adults', 'meal', 'previous_cancellations', 'booking_changes'
#     จะย้ายขึ้น A ตอน loop ข้อ 7 (ทำไมถึงยกเลิก)
#
# NOTE: การกรองเฉพาะข้อนี้ให้เก็บในตัวแปรใหม่ ห้ามแก้ df หลัก
