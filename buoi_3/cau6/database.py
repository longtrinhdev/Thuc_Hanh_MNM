path = 'D:\projectPython\Project_3\QLSV.txt'
def save(line):
    try:
        f = open(path,'a',encoding='utf8') # mở file
        f.writelines(line) # đọc từng dòng
        f.writelines('\n')# đọc cả dấu xuống dòng
        f.close()
    except:
        pass

# hàm đọc dữ liệu 
def read():
    sv=[]
    try:
        f = open(path,'r',encoding='utf8') # mở file
        for i in f:
            data = i.strip() # xóa khoảng trắng đầu và cuỗi
            arr = data.split('-') # cắt dữ liệu dựa trên dấu '-'
            sv.append(arr)

        f.close()
    except:
        pass
    return sv
