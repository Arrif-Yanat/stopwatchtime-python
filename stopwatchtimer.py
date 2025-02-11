import time  # นำเข้าโมดูล time เพื่อใช้จัดการเวลา

# ฟังก์ชัน Stopwatch จับเวลา
def stopwatch():
    print("เริ่มการจับเวลา... กด Enter เพื่อหยุด ⏱️")
    input("กด Enter เพื่อเริ่ม")  # เริ่มต้นเมื่อผู้ใช้กด Enter
    start_time = time.time()  # บันทึกเวลาเริ่มต้น
    input("กด Enter อีกครั้งเพื่อหยุด")  # หยุดจับเวลาหลังจากกด Enter อีกครั้ง
    end_time = time.time()  # บันทึกเวลาสิ้นสุด
    elapsed_time = end_time - start_time  # คำนวณเวลาที่ผ่านไป
    print(f"เวลาที่จับได้: {elapsed_time:.2f} วินาที")

# ฟังก์ชัน Timer นับถอยหลัง
def timer():
    seconds = int(input("ป้อนจำนวนวินาทีที่ต้องการนับถอยหลัง: "))  # รับเวลาจากผู้ใช้
    print(f"เริ่มนับถอยหลัง {seconds} วินาที ⏳")
    while seconds > 0:
        print(f"เหลือเวลา: {seconds} วินาที", end="\r")  # แสดงเวลาที่เหลือ (ไม่ขึ้นบรรทัดใหม่)
        time.sleep(1)  # รอ 1 วินาที
        seconds -= 1  # ลดเวลาลงทีละ 1 วินาที
    print("หมดเวลา! ⏰")

# เมนูหลัก
def main():
    while True:
        print("\nโปรแกรม Stopwatch และ Timer ⏱️⏳")
        print("1. จับเวลา (Stopwatch)")
        print("2. นับถอยหลัง (Timer)")
        print("3. ออกจากโปรแกรม")
        choice = input("เลือกเมนู (1-3): ")  # รับเมนูจากผู้ใช้

        if choice == '1':
            stopwatch()  # เรียกใช้ฟังก์ชัน Stopwatch
        elif choice == '2':
            timer()  # เรียกใช้ฟังก์ชัน Timer
        elif choice == '3':
            print("ขอบคุณที่ใช้โปรแกรม! 👋")
            break  # ออกจากลูป
        else:
            print("โปรดเลือกเมนูที่ถูกต้อง (1-3)")

# เริ่มโปรแกรม
main()