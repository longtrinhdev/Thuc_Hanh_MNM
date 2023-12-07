path = 'D:\\Zalo_dowload\\KTra_TX2\\diemPython.csv'
def save(line):
    try:
        f = open(path, 'a',encoding='utf-8') # mở file
        f.writelines(line) # đọc từng dòng
        f.writelines('\n') # đọc dấu xuống dòng
        f.close()

    except:
        pass
# hàm đọc dữ liệu
def read():
    sv =[]
    try:
        f = open(path,'r',encoding='utf-8')
        for i in f:
            data = i.strip() # xóa khoảng trắng đầu và cuối
            arr = data.split(',')
            sv.append(arr)

        f.close()
    except:
        pass
    
    return sv