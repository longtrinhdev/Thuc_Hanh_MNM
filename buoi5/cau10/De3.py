# tạo giao diện
from  tkinter import *
import csv
from tkinter import messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from database import*

# hàm add
def add():
    # dùng phương thức get() để lấy dữ liệu
    scoreA = diemA.get()
    scoreB = diemB.get()
    if (scoreA == ''):
        scoreA = None
        line = stt.get() +',' +msv.get() +',' + lop.get() +',' + hoTen.get() + ',' + str(scoreA)+',' + scoreB
        save(line)
    if (scoreB == ''):
        scoreB = None
        line = stt.get() +',' +msv.get() +',' + lop.get() +',' + hoTen.get() + ',' + scoreA+',' + str(scoreB)
        save(line)
    Show()
# hàm sắp xếp
def Sort():
    df = pd.read_csv('D:\\Zalo_dowload\\KTra_TX2\\diemPython.csv', header=None)
    in_data = np.array(df.iloc[:, :])
    DiemA = np.array(in_data[:, 4], dtype=float)
    DiemB = np.array(in_data[:, 5], dtype=float)

    DiemA[np.isnan(DiemA)] = 0  # Nếu DiemA là NaN, giả sử nó bằng 0
    DiemB[np.isnan(DiemB)] = 0  # Nếu DiemB là NaN, giả sử nó bằng 0

    ds = DiemA + DiemB

    ds_sort = np.argsort(ds)
    dsSort = in_data[ds_sort]
    
    listbox.delete(0, END)
    print(dsSort)
    for i in dsSort:
        listbox.insert(END, i)  # Thêm danh sách sau khi sắp xếp
# Hàm tìm kiếm
def Find():
    df = pd.read_csv('D:\\Zalo_dowload\\KTra_TX2\\diemPython.csv', header=None)
    in_data = np.array(df.iloc[:, :])
    mSV= np.array(in_data[:,1],dtype=str)

    for i in range(len(mSV)):
        if (msv.get() == mSV[i]):
            messagebox.showinfo("Ket qua tim kiem",str(in_data[i]))
            return
    messagebox.showinfo("Ket qua tim kiem:","Khong tim thay sinh vien!")

# Hàm hiển thị
def Show():
    sv = read()
    listbox.delete(0, END) # làm sạch lưới
    for i in sv:
        listbox.insert(END,i) # đưa list sinh viên vào listbox
# hàm vẽ biểu đồ
def Chart():
    df = pd.read_csv('D:\\Zalo_dowload\\KTra_TX2\\diemPython.csv', header=None)
    in_data = np.array(df.iloc[:, :])
    
    count_diemA = np.count_nonzero(~np.isnan(in_data[:, 4].astype(float)))
    count_diemB = np.count_nonzero(~np.isnan(in_data[:, 5].astype(float)))

    # Vẽ biểu đồ
    labels = ['Diem A', 'Diem B']
    counts = [count_diemA, count_diemB]

    plt.bar(labels, counts, color=['red', 'green'])
    plt.xlabel('Loai Diem')
    plt.ylabel('So luong sinh vien')
    plt.title('So luong sinh vien theo loai diem')
    plt.show()

# Hàm xuất file
def outFile():
    df = pd.read_csv('D:\\Zalo_dowload\\KTra_TX2\\diemPython.csv', header=None)
    in_data = np.array(df.iloc[:, :])
    tenSV= np.array(in_data[:,3],dtype=str)
    ten_sinh_vien = [ten.split()[-1] for ten in tenSV]
    tenSinhVien = np.argsort(ten_sinh_vien)
    infor_student_sort = in_data[tenSinhVien]

    with open('D:\\Zalo_dowload\\KTra_TX2\\file_sort.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(infor_student_sort)
    messagebox.showinfo("Xuat File","Xuat file thanh cong")




win = Tk()
# tạo các biến để lưu dữ liệu khi nhập vào
stt = StringVar()
msv = StringVar()
lop = StringVar()
hoTen = StringVar()
diemA = StringVar()
diemB = StringVar()

win.title('Quan ly sinh vien')
win.minsize(height=600,width= 500)
Label(win,text= 'Ung dung quan ly sinh vien',fg = 'red',font=('cambria',15),width=25).grid(row= 0)
#tạo listbox để hiển thị
listbox = Listbox(win, width=80,height=20)
listbox.grid(row = 1, columnspan=2)
Show()
# tạo label để người dùng xác nhận vị trí nhập
Label(win, text ='STT: ').grid(row=2,column=0)
Entry(win,width=33,textvariable=stt).grid(row=2,column=1)
Label(win, text ='MSV: ').grid(row=3,column=0)
Entry(win,width=33,textvariable=msv).grid(row=3, column= 1)
Label(win, text ='Lop: ').grid(row=4,column=0)
Entry(win, width=33, textvariable=lop).grid(row= 4, column=1)
Label(win, text ='Ten SV: ').grid(row=5,column=0)
Entry(win, width=33, textvariable=hoTen).grid(row=5, column=1)
Label(win, text= 'Diem A: ').grid(row = 6, column=0)
Entry(win, width=33, textvariable= diemA).grid(row=6, column=1)
Label(win, text= 'Diem B: ').grid(row = 7, column=0)
Entry(win, width= 33, textvariable= diemB).grid(row=7, column=1)


#tạo các button để xử lý thao tác
button = Frame(win) # tạo khối button
Button(button, text='Add', command= add).pack(side=LEFT)
Button(button, text='Sort',command=Sort).pack(side=LEFT)
Button(button, text='Find',command= Find).pack(side=LEFT)
Button(button, text='Show', command= Show).pack(side=LEFT)
Button(button, text='Chart', command=Chart).pack(side=LEFT)
Button(button, text='Out File',command=outFile).pack(side=LEFT)
Button(button, text='Exit', command=win.quit).pack(side=LEFT)
button.grid(row=8, column=1)


win.mainloop()