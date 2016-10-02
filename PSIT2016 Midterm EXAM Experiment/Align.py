"""Exam2: Align

เพื่อที่จะกลับโลกของคุณ คุณจะต้องเข้าเมืองเพื่อใช้บริการ Warp Portal
แต่ว่าตอนนี้คุณไม่มีเงินเลย ถึงมีก็เป็นคนละหน่วยกับโลกคู่ขนานนี้
สิ่งของที่ติดตัวคุณอยู่มีเพียง Notebook ที่ใช้ Hack AI, ของติดตัว กระเป๋าเงิน มือถือ กุญแจบ้าน และ Harddisk ลูกนั้น
คุณจึงลองเปิด Notebook เพื่อที่จะลองหาข้อมูล แต่คุณก็นึกได้ว่าที่นี่เป็นโลกคู่ขนาน คงไม่มีเทคโนโลยีอะไรที่จะเข้ากับอุปกรณ์ของคุณได้

คุณจึงลองหางานแถวๆนั้นทำดู เพื่อหาเงินเข้าเมือง
จึงได้พบกับร้านขายของที่มีหน้าจอขนาดกลางแสดงข้อความเป็นชื่อร้าน
แต่ว่ากลับไม่มีข้อความใดๆแสดงขึ้นมา คุณจึงเข้าไปถาม เผื่อที่จะได้งานทำ

เจ้าของร้านบอกว่าโปรแกรมที่ใช้ส่งข้อความไปให้ตัวป้ายไฟนั้น ใช้งานยาก
คุณจึงออกตัวเสนอที่จะรับงานช่วยเหลือนี้
 
เจ้าของร้านท่านหนึ่งได้กล่าวไว้ว่า หน้าจอไฟนี้มีขนาด size ตัวอักษร
เค้าต้องการข้อความขึ้นไปแสดงผลเพียงบรรทัดเดียว แต่ให้สามารถกำหนดได้ว่า จะให้ข้อความนั้นอยู่ ทางซ้าย ตรงกลาง หรือทางขวา
ถ้าหากให้ข้อความอยู่ตรงกลาง แล้วช่องว่างระหว่างทางซ้ายและทางขวาของข้อความไม่พอดีกัน ให้เอาเศษของช่องว่างไว้ทางซ้ายเสมอ


by นายพิชาธร เอกอุ่น 
1 October 2016, 20:58
 Specification
 Input Specification	 Output Specification

สามบรรทัด
บรรทัดแรกเป็นขนาดของจอป้ายไฟ size
บรรทัดที่สองเป็นคำสั่งให้ข้อความชิดซ้าย อยู่กึ่งกลาง หรือทางขวา (left, center, right) เป็นพิมพ์เล็กทั้งหมดเสมอ
บรรทัดที่สามเป็นข้อความ โดยที่ขนาดของข้อความจะไม่ใหญ่เกินกว่า size 

บรรทัดเดียว เป็นข้อความที่แสดงตามความต้องการที่กำหนดให้ 
 Sample Case
 Sample Input	 Sample Output
30
left
Hello, world!
Hello, world!                 
20
center
Caution
       Caution      
40
right
Good beer, free wi-fi.
                  Good beer, free wi-fi."""
def align(space, ali, word):
    """..."""
    if ali == "left":
        print(word)
    elif ali == "right":
        print(" "*(space-len(word))+word)
    elif ali == "center":
        num = space/2-len(word)/2
        if num%1 != 0:
            num = num+1
        print(" "*(int(num))+word)
align(int(input()), input(), input())
