import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mở file CSV để ghi dữ liệu
input_data = input("Ban co muon nhap chuc nang them sv ko: ")
if (input_data == 'Y' or input_data == 'y'):
    with open('F:\\projectPython\\Thuc_hanh\\KTra_TX2\\diemPython.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        while True:
            stt = input("Nhap so thu tu: ")
            if stt == '':
                break
            msv = input("Nhap ma sinh vien: ")
            lop = input("Nhap lop hoc: ")
            hoVaTen = input("Nhap ho va ten: ")
            DiemA = input("Nhap diem A: ")
            if DiemA == '':
                break
            DiemB = input("Nhap diem B: ")
            data = [stt, msv, lop, hoVaTen, DiemA, DiemB]
            writer.writerow(data)

# Đọc dữ liệu từ file CSV
df = pd.read_csv('F:\\projectPython\\Thuc_hanh\\KTra_TX2\\diemPython.csv', header=None)
in_data = np.array(df.iloc[:, :])
print(in_data)

# Xử lý và hiển thị dữ liệu
msv = in_data[:, 1]
tongSV = len(msv)
print('Tong SV: ' + str(tongSV) + " sinh viên")

# Tính tổng điểm không phân biệt giữa điểm A và điểm B
diemA = np.array(in_data[:, 4], dtype=float)
diemB = np.array(in_data[:, 5], dtype=float)
msv  = np.array(in_data[:,1],dtype= str)

diemA[np.isnan(diemA)] = 0  # Nếu không có điểm A, thì giả sử là 0
diemB[np.isnan(diemB)] = 0  # Nếu không có điểm B, thì giả sử là 0
tong_diem = diemA + diemB
maxA = diemA.max()
i = np.where(diemA == maxA)
# Lấy chỉ số sắp xếp của tổng điểm theo thứ tự giảm dần
sort_index_tong_diem = np.argsort(-tong_diem)

# Sắp xếp in_data theo chỉ số sắp xếp của tổng điểm
in_data_sorted_tong_diem = in_data[sort_index_tong_diem]

# Hiển thị dữ liệu đã sắp xếp
print('Dữ liệu sắp xếp theo tổng điểm (điểm A + điểm B):')
# print(in_data_sorted_tong_diem)

# Chỉ lấy số lượng dòng tương ứng với kích thước của danh sách ban đầu
in_data_sorted_tong_diem = in_data_sorted_tong_diem[:len(in_data)]

print(in_data_sorted_tong_diem)

# Tìm kiếm sinh viên  dựa vào mã sinh viên
mSV = input("Nhap ma sinh vien can tim kiem: ")
for i in range(len(in_data)):
    if (msv[i] == mSV):
        print(in_data[i])
# vẽ biểu đồ thể hiện số lượng điểm A , B
# Tính số lượng điểm A và điểm B
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
# print('Lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i,2], len(diemA)))


