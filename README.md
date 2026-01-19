# Nghiên cứu phương pháp Gauss-Seidel giải phương trình Laplace 2D
(Research on Gauss-Seidel method for solving 2D Laplace equation in viscous flow)

## 🏫 Thông tin chung
* **Trường:** Đại học Bách Khoa Hà Nội - Trường CNTT & TT
* **Môn học:** Tính toán khoa học (Scientific Computing)
* **Giảng viên hướng dẫn:** TS. [cite_start]Vũ Văn Thiệu
* **Học kỳ:** 2025.1 (Tháng 1/2026)

## 👥 Nhóm thực hiện
| STT | Họ và tên | MSSV |
|:---:|:---|:---:|
| 1 | Đinh Việt Hoàng | 202416917 |
| 2 | Nguyễn Huy Hoàng | 202416921 |
| 3 | Nguyễn Đình Hùng | 202416925 |
| 4 | Nguyễn Việt Hưng | 202416933 |
| 5 | Phùng Nam Khánh | 202416949 |
| 6 | Nguyễn Tài Kiên | 202416957 |

## 📄 Giới thiệu đề tài
Dự án nghiên cứu và cài đặt phương pháp lặp **Gauss-Seidel** kết hợp với phương pháp **Sai phân hữu hạn (Finite Difference Method - FDM)** để giải phương trình Laplace hai chiều $(\nabla^2 \phi = 0)$.

Ứng dụng cụ thể:
1.  **Bài toán kiểm chứng:** Giải phương trình Laplace trên miền hình chữ nhật đơn giản với điều kiện biên Dirichlet.
2.  **Bài toán ứng dụng:** Mô phỏng dòng chảy nhớt trong kênh dẫn có tiết diện hình chữ C (C-section channel).

## 📊 Kết quả mô phỏng
Chương trình được viết bằng Python, sử dụng thư viện `numpy` để tính toán ma trận và `matplotlib` để trực quan hóa dữ liệu (Contour plot & 3D Surface plot).

* **Phương pháp:** Gauss-Seidel Iteration.
* **Điều kiện dừng:** Sai số hội tụ $\epsilon < 10^{-4}$.
* **Kết quả:** Thuật toán hội tụ sau khoảng 828 bước lặp (đối với lưới 31x31).

<img width="365" height="89" alt="image" src="https://github.com/user-attachments/assets/24f7875d-7e49-48d4-a44e-24df07a6ae2a" />

<img width="1200" height="500" alt="Figure_2d" src="https://github.com/user-attachments/assets/858dea3d-40cc-4249-848d-7aaeef6893b9" />

<img width="1536" height="754" alt="Figure_3d" src="https://github.com/user-attachments/assets/f1df6ec9-a535-46a7-b0e2-b5d52cac896c" />


## 🛠️ Cài đặt và Chạy chương trình

### Yêu cầu hệ thống
* Python 3.x
* Các thư viện: `numpy`, `matplotlib`

### Cài đặt thư viện
```bash
pip install numpy matplotlib
```

### Chạy mô phỏng
Để chạy bài toán kiểm chứng trên miền hình chữ nhật:
```bash
python laplace_rect_solver.py
```

## 📂 Cấu trúc thư mục
* `laplace_rect_solver.py`: Mã nguồn giải bài toán trên miền hình chữ nhật (Code Demo).
* `Report_GaussSeidel_Laplace.pdf`: Báo cáo chi tiết bao gồm cơ sở lý thuyết và phân tích sai số.

---
