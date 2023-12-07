from tkinter import*
from tkinter import messagebox
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from database import*


def add():
    diema = diemA.get()
    diemb = diemB.get()
    if (msv.get()!='' and hoTen.get()!=''and lop.get()!=''):
        if (diema == ''):
            diema = None
            line = stt.get() + ','+ msv.get()+','+ lop.get()+','+ hoTen.get()+','+ str(diema)+ ',' +diemb
            save(line)
        if (diemb == ''):
            diemb = None
            line = stt.get() + ','+ msv.get()+','+ lop.get()+','+ hoTen.get()+','+ diema+ ',' +str(diemb)
            save(line)
    else:
        messagebox.showinfo("Khong duoc bo trong","Vui long nhap day du")
    show()
# hàm show
def show():
    sv= read()
    listbox.delete(0,END)
    for i in sv:
        listbox.insert(END,i)
# hàm sort
def sort():
    df = pd.read_csv('D:\\Zalo_dowload\\KTra_TX2\\diemPython.csv',header =None)
    in_data = np.array(df.iloc[:,:])
    DiemA = np.array(in_data[:,4],dtype=float)
    DiemB = np.array(in_data[:,5],dtype=float)
    # trong điểm a, b nếu bằng không 
    DiemA[np.isnan(DiemA)] = 0
    DiemB[np.isnan(DiemB)] = 0

    ds = DiemA + DiemB
    for i in range(len(ds)):
        for j in range(len(ds)-1):
            if (ds[i] > ds[j]):
                tg = in_data[i]
                in_data[i] = in_data[j]
                in_data[j] = tg
    listbox.delete(0,END)
    for i in in_data:
        listbox.insert(END,i)
# hàm tìm kiếm
def find():
    df = pd.read_csv('D:\\Zalo_dowload\\KTra_TX2\\diemPython.csv',header= None)
    in_data = np.array(df.iloc[:,:])
    mSV= np.array(in_data[:,1],dtype=str)
    
    for i in range(len(mSV)):
        if(msv.get() == mSV[i]):
            messagebox.showinfo('Thong tin sinh vien:',str(in_data[i]))
            return
    messagebox.showinfo('Khong tim thay sinh vien co ma:' ,msv.get())
# hàm hiển thi biểu đồ 
def chart():
    df =pd.read_csv('D:\\Zalo_dowload\\KTra_TX2\\diemPython.csv',header=None)
    in_data = np.array(df.iloc[:,:])

    demA = np.count_nonzero(~np.isnan(in_data[:,4].astype(float)))
    demB = np.count_nonzero(~np.isnan(in_data[:,5].astype(float)))

    labels = ['Diem A','Diem B']
    cnts = [demA,demB]

    plt.bar(labels,cnts,color = ['red','blue'])
    plt.xlabel('Loai diem')
    plt.ylabel('So luong sinh vien')
    plt.title('Bieu do phan bo luong diem voi sinh vien')
    plt.show()
# hàm xuất file
def out_File():
    df =pd.read_csv('D:\\Zalo_dowload\\KTra_TX2\\diemPython.csv',header=None)
    in_data = np.array(df.iloc[:,:])
    tenSV = np.array(in_data[:,3],dtype=str)
    ten_sinh_vien = [ten.split()[-1] for ten in tenSV]
    ten_SV= np.argsort(ten_sinh_vien)
    infor_student = in_data[ten_SV]

    with open('D:\\Zalo_dowload\\KTra_TX2\\fileTen.txt','w',newline='',encoding='utf-8') as f:
        write = csv.writer(f)
        write.writerows(infor_student)
    messagebox.showinfo("Xuat file","Thanh cong")

win = Tk()
stt= StringVar()
msv= StringVar()
lop= StringVar()
hoTen= StringVar()
diemA= StringVar()
diemB= StringVar()
win.title('Ung Dung Quan Ly Sinh Vien')
win.minsize(height=600,width=500)
Label(win,text='Ung Dung Quan Ly Sinh Vien',fg='red',font=('cambria',15),width=25).grid(row=0)
# tạo listbox
listbox = Listbox(win,height=20,width=80)
listbox.grid(row=1,columnspan=2)
show()
# tạo các label và ô nhập

Label(win,text='STT:').grid(row= 2,column=0)
Entry(win,width=33 ,textvariable=stt).grid(row=2,column=1)
Label(win,text='MSV:').grid(row= 3,column=0)
Entry(win,width=33 ,textvariable=msv).grid(row=3,column=1)
Label(win,text='Lop:').grid(row= 4,column=0)
Entry(win,width=33 ,textvariable=lop).grid(row=4,column=1)
Label(win,text='Ten SV:').grid(row= 5,column=0)
Entry(win,width=33 ,textvariable=hoTen).grid(row=5,column=1)
Label(win,text='Diem A:').grid(row= 6,column=0)
Entry(win,width=33 ,textvariable=diemA).grid(row=6,column=1)
Label(win,text='Diem B:').grid(row= 7,column=0)
Entry(win,width=33 ,textvariable=diemB).grid(row=7,column=1)

# tạo các nút bấm
button = Frame(win)
Button(button,text='ADD',command=add).pack(side=LEFT)
Button(button,text='SHOW',command=show).pack(side=LEFT)
Button(button,text='SORT',command=sort).pack(side=LEFT)
Button(button,text='FIND',command=find).pack(side=LEFT)
Button(button,text='CHART',command=chart).pack(side=LEFT)
Button(button,text='OUT FILE',command=out_File).pack(side=LEFT)
Button(button,text='EXIT',command=win.quit).pack(side=LEFT)
button.grid(row=8,column= 1)

win.mainloop()