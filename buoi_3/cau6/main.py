from tkinter import *
from database import *
# hàm add
def add():
    # dùng phương thức get() để lấy dữ liệu
    line = id.get() + '-'+ name.get() + '-' + wasBorn.get()
    save(line)
    show()
def show():
    sv= read()
    listbox.delete(0, END) # làm sạch lưới
    for i in sv:
        listbox.insert(END,i) # đưa list sinh viên vào listbox
def sort():
    sv= read()
    for i in range(len(sv)):
        for j in range(len(sv)):
            x, y = sv[i], sv[j] # sắp xếp theo năm sinh
            if (x[2] > y[2]):
                sv[i], sv[j]= y ,x
    listbox.delete(0, END) # reset list
    for i in sv:
        listbox.insert(END,i) # thêm danh sách sau khi được sắp xếp vào listbox
    

win = Tk()
# tạo các biến để lưu dữ liệu khi nhập vào các entry và đưa các biến này vào trong entry bằng textVariable
id = StringVar()
name = StringVar()
wasBorn = StringVar()

win.title('Quan ly sinh vien')
win.minsize(height=500,width=500)
Label(win,text ='Ung dung quan ly sinh vien',fg='red',font =('cambria',15),width=25).grid(row=0)
# Tạo listbox để hiển thị (chỉ truyền độ rộng và chiều cao)
listbox = Listbox(win,width=80,height=20)
listbox.grid(row=1,columnspan=2)
show()
# tạo các label để người dùng xác định vị trí nhập
Label(win,text ='Ma SV: ').grid(row=2,column=0)
Entry(win,width=35,textvariable=id).grid(row =2,column=1)
Label(win,text ='Ten SV: ').grid(row=3,column=0)
Entry(win,width=35, textvariable= name).grid(row =3,column=1)
Label(win,text ='Nam Sinh: ').grid(row=4,column=0)
Entry(win,width=35, textvariable= wasBorn).grid(row =4,column=1)
# tạo ra các button để xử lý thao tác
button = Frame(win) # tạo 1 khối button
Button(button,text= 'add',command= add).pack(side = LEFT) # các button nằm trong khối trên
Button(button,text = 'Show',command=show).pack(side = LEFT) # các button nằm trong khối trên
Button(button,text = 'Sort', command= sort).pack(side = LEFT) # các button nằm trong khối trên
Button(button,text = 'Exit',command=win.quit).pack(side = LEFT) # các button nằm trong khối trên chức năng thoát khỏi chương trình
button.grid(row=5,column=1)




win.mainloop()