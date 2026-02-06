# Phân tích xu hướng đọc sách theo thể loại

## Giới thiệu đề tài
Trong thời đại số, dữ liệu về sách và hành vi đọc của người dùng ngày càng phong phú. Việc phân tích dữ liệu này giúp hiểu rõ xu hướng đọc, thị hiếu của độc giả cũng như đánh giá mức độ phổ biến của từng thể loại sách.

Đề tài này thực hiện phân tích tập dữ liệu **Best Books 10k – Multi Genre Dataset** nhằm:
- Xác định các thể loại sách phổ biến nhất.
- Phân tích xu hướng đọc theo thời gian.
- So sánh điểm đánh giá trung bình và số lượt đánh giá giữa các thể loại.

## Mục tiêu nghiên cứu
- Làm sạch và tiền xử lý dữ liệu sách.
- Phân tích xu hướng đọc sách theo thể loại.
- Trực quan hóa kết quả bằng biểu đồ.
- Đưa ra nhận xét và kết luận từ dữ liệu.

##  Dataset
- Tên: **Best Books 10k – Multi Genre Dataset**
- Nguồn: Kaggle  
- Số lượng bản ghi: ~10,000 cuốn sách  
- Các thuộc tính chính:
  - Book (Tên sách)
  - Author (Tác giả)
  - Description (Mô tả)
  - Genres (Thể loại)
  - Avg_Rating (Điểm đánh giá trung bình)
  - Num_Ratings (Số lượt đánh giá)
  - URL (Liên kết sách)
  - 
## Công nghệ sử dụng
- **Python**
- **Pandas** – xử lý dữ liệu
- **NumPy** – hỗ trợ tính toán
- **Matplotlib** – trực quan hóa dữ liệu
- 
## Các bước thực hiện

###  Load dữ liệu
- Đọc dữ liệu từ file CSV.
- Kiểm tra cấu trúc và kích thước dataset.

### Khám phá dữ liệu
- Kiểm tra kiểu dữ liệu.
- Thống kê số lượng giá trị thiếu.

### Làm sạch và tiền xử lý dữ liệu
- Chuẩn hóa tên cột.
- Đổi tên cột cho thống nhất.
- Loại bỏ các cột không cần thiết.
- Chuyển đổi kiểu dữ liệu sang dạng số.
- Loại bỏ các dòng có giá trị thiếu và trùng lặp.
- Tách các sách có nhiều thể loại thành từng dòng riêng biệt.

### Phân tích dữ liệu
- Phân tích số lượng sách theo từng thể loại.
- Phân tích xu hướng đọc theo thời gian.
- So sánh điểm đánh giá trung bình giữa các thể loại.
- Phân tích mức độ phổ biến dựa trên tổng số lượt đánh giá.

### Trực quan hóa
- Biểu đồ cột: Top 10 thể loại phổ biến.
- Biểu đồ đường: Xu hướng đọc theo thời gian.
- Biểu đồ thanh ngang: Thể loại có rating cao nhất.
- Biểu đồ cột: Thể loại có nhiều lượt đánh giá nhất.

##  Kết quả và nhận xét

- Các thể loại **Fiction, Fantasy, Romance** chiếm tỷ trọng lớn nhất.
- Xu hướng đọc sách có xu hướng tăng theo thời gian, đặc biệt từ sau năm 2010.
- Một số thể loại có điểm đánh giá trung bình cao nhưng số lượng sách không nhiều, cho thấy mức độ yêu thích cao trong nhóm độc giả chuyên biệt.
- Các thể loại phổ biến thường có tổng lượt đánh giá rất lớn, phản ánh thị hiếu đọc chung của cộng đồng.

##  Kết luận

Đề tài đã thực hiện thành công việc phân tích xu hướng đọc sách dựa trên dữ liệu thực tế. Kết quả cho thấy thị hiếu đọc của người dùng thay đổi theo thời gian, trong đó các thể loại giải trí và tiểu thuyết hiện đại ngày càng chiếm ưu thế.

Nghiên cứu giúp cung cấp góc nhìn trực quan về hành vi đọc sách, hỗ trợ các nhà xuất bản, thư viện và nền tảng phân phối sách trong việc xây dựng chiến lược phát triển nội dung phù hợp.

## Thông tin sinh viên

- **Họ và tên:** Đỗ Trọng Mạnh, Nguyễn Đức Hiếu
- **Môn học:** Phân tích dữ liệu lớn  

## Hướng dẫn chạy chương trình trên Visual Studio Code 
Máy tính cần có Visual Studio Code và Python
Tải file và mở trong Visual Studio Code 
Mở New Terminal(ctrl+shift+`) tạo một Command Prompt
Sau đó gõ lệnh
pip install pandas numpy matplotlib
Sau đó gõ lệnh
python book.py
