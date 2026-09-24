import sys

# เมธอดสำหรับตัดข้อความให้เหลือ 8 ตัวอักษรแรก (ใช้ Slicing)
def shrink(text):
    print(text[:8])

# เมธอดสำหรับเติมตัว 'Z' ต่อท้ายจนกว่าข้อความจะครบ 8 ตัวอักษร
def enlarge(text):
    padding = 'Z' * (8 - len(text))
    print(text + padding)

# ตรวจสอบว่ามีพารามิเตอร์ส่งเข้ามาอย่างน้อย 1 ตัวหรือไม่
if len(sys.argv) > 1:
    for param in sys.argv[1:]:
        length = len(param)
        
        if length > 8:
            shrink(param)
        elif length < 8:
            enlarge(param)
        else:
            print(param)
else:
    print("none")