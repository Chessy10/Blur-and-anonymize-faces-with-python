# Blur-and-anonymize-faces-with-python
# Face Anonymizer App
## Giới thiệu
Face Anonymizer là một ứng dụng sử dụng OpenCV và Tkinter để nhận diện và làm mờ hoặc pixel hóa các khuôn mặt trong video trực tiếp từ webcam. Ứng dụng hỗ trợ ba chế độ: làm mờ, pixel hóa, và thay thế khuôn mặt bằng biểu tượng. Giao diện người dùng thân thiện giúp người dùng dễ dàng tùy chỉnh mức độ làm mờ hoặc pixel hóa.

## Tính năng
- Nhận diện khuôn mặt trong thời gian thực.
- Làm mờ khuôn mặt bằng cách điều chỉnh thanh trượt.
- Pixel hóa khuôn mặt với mức độ tùy chỉnh.
- Thay thế khuôn mặt bằng biểu tượng.
- Giao diện người dùng đẹp mắt và dễ sử dụng.

## Yêu cầu
- Python 3.x
- Thư viện OpenCV
- Thư viện Pillow
- Thư viện Tkinter (thường có sẵn trong Python)

## Công nghệ sử dụng

### Haar Cascade
Haar Cascade là một thuật toán nhận diện đối tượng, được phát triển bởi Paul Viola và Michael Jones. Thuật toán này sử dụng các đặc trưng Haar để phát hiện các khuôn mặt trong hình ảnh. Cách hoạt động của Haar Cascade như sau:
1. **Huấn luyện Mô hình**: Một mô hình Haar Cascade được huấn luyện bằng cách sử dụng một tập hợp các ảnh có và không có khuôn mặt. Mô hình học cách phân tích các đặc trưng của các khuôn mặt.
2. **Quét Hình ảnh**: Khi một bức ảnh được nhập vào, mô hình sẽ quét hình ảnh và kiểm tra các vùng khác nhau để tìm các đặc trưng giống như khuôn mặt.
3. **Nhận diện**: Nếu mô hình phát hiện một khuôn mặt, nó sẽ trả về tọa độ của khuôn mặt đó.

Trong ứng dụng của bạn, mô hình Haar Cascade được sử dụng để phát hiện khuôn mặt trong video trực tiếp từ webcam.

### Thuật toán Gaussian Blur
Gaussian Blur là một phương pháp làm mờ hình ảnh sử dụng hàm Gaussian để giảm độ sắc nét của hình ảnh. Cách hoạt động của thuật toán này như sau:
1. **Lọc Hình ảnh**: Hàm Gaussian được áp dụng lên hình ảnh bằng cách tính toán trung bình có trọng số của các điểm ảnh xung quanh mỗi pixel.
2. **Kích thước Kernel**: Kích thước của kernel (một ma trận số liệu) quyết định mức độ mờ. Kernel lớn hơn sẽ tạo ra mức độ mờ cao hơn.
3. **Ứng dụng**: Gaussian Blur thường được sử dụng để làm mờ các chi tiết không cần thiết trong hình ảnh, làm nổi bật các phần quan trọng hơn.

Trong ứng dụng của bạn, Gaussian Blur được sử dụng để làm mờ khuôn mặt khi người dùng chọn chế độ làm mờ.

### Cách hoạt động của Pixelate_face
`pixelate_face` là một hàm trong ứng dụng của bạn để biến đổi khuôn mặt thành dạng pixel. Cách hoạt động của nó như sau:
1. **Kích thước Pixel hóa**: Hàm nhận vào kích thước pixel mà người dùng chọn (ví dụ: 25x25).
2. **Thay đổi Kích thước**: Khuôn mặt được thu nhỏ xuống kích thước pixel (giả sử 25x25) để giảm chi tiết.
3. **Mở Rộng**: Khuôn mặt sau đó được mở rộng trở lại kích thước ban đầu của nó bằng phương pháp nội suy không tuyến tính (`INTER_NEAREST`), giúp tạo ra hiệu ứng pixel hóa.
4. **Cập nhật Hình ảnh**: Khuôn mặt đã được pixel hóa được cập nhật vào bức ảnh gốc.

Phương pháp này giúp ẩn danh khuôn mặt mà vẫn giữ được vị trí và hình dạng tổng thể của nó trong khung hình.

## Lưu ý
Các phương pháp nhận diện khuôn mặt và xử lý hình ảnh trong ứng dụng của bạn giúp tăng cường sự riêng tư và bảo mật cho người dùng. Chúng cũng có thể được áp dụng trong nhiều lĩnh vực khác nhau, bao gồm bảo mật video và nhận diện khuôn mặt trong các ứng dụng thương mại.



## Cài đặt
1. Clone hoặc tải về dự án từ kho lưu trữ.
   ```bash
   git clone <https://github.com/Chessy10/Blur-and-anonymize-faces-with-python>
   cd Face-Anonymizer```
2. Cài đặt các thư viện cần thiết:
   ```pip install onpencv-python pillow```

## Cách sử dụng
1. Chạy ứng dụng:
   ```python main.py```
2. Chọn chế độ xử lý(Làm mờ, Pixel hóa, hoặc chèn biểu tượng) bằng cách nhấn vào các nút tương ứng.
3. Điều chỉnh mức độ làm mờ hoặc pixel hóa bằng cách sử dụng các thanh trượt.

## Lưu ý 
- Đảm bảo webcam của bạn được kết nối và hoạt động bình thường.
- Đảm bảo rằng bạn tải xuống hình ảnh biểu tượng mà bạn muốn sử dụng(ví dụ: mixi.jpg) và đặt nó vào cùng thư mục với mã nguồn.
## Ảnh chụp màn hình
## Tài liệu tham khảo
- OpenCV Documentation: https://opencv.org/
- Tkinter Documentation: https://docs.python.org/3/library/tkinter.html


