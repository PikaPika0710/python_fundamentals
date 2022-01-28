def saveFile(path):
    file=open(path, 'w', encoding='utf-8')
    file.writelines("102190298; Trần Công Việt; 07/10/2001\n")
    file.writelines("102190290; Hồ Hoàng Thiện; 07/10/2001\n")
    file.writelines("102190278; Phạm Thành Nguyên; 07/10/2001\n")
    file.writelines("102190252; Đinh Gia Bảo; 07/10/2001")
    file.close()

saveFile("test.txt")

