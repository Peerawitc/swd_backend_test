
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).
 
"""
number = 9876521
def convert_number_to_thai_text(number):
    thai_numerals = [
            "ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"
        ]
    thai_units = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
    # 0=>2 
    # 1->1 
    # 2->0 
    #11 20 =ยี่ 
    number_str = str(number)
    result = ""
    for i in range(len(number_str)):
        if i != len(number_str)-1 and number_str[i]=="0" :
            continue
        if i == len(number_str)-1 and  number_str[i]=="1" and len(number_str)>1:
            result+=("เอ็ด")
            break
        if i == len(number_str)-2 and number_str[i]=="2" :
            result+=("ยี่")
        elif not(i == len(number_str)-2 and number_str[i]=="1") :
            result+=thai_numerals[int(number_str[i])]
        result+=thai_units[(len(number_str)-i)-1]
        
    return result
print(convert_number_to_thai_text(number))