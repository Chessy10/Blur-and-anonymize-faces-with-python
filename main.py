import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

class FaceAnonymizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Face Anonymizer')
        self.root.geometry('800x600')
        self.root.configure(bg='#2b2b2b')  # Màu nền tổng thể cho cửa sổ

        # Tạo phong cách ttk
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12), background='#2196F3', foreground='white')
        style.configure('TLabel', font=('Helvetica', 14), background='#2b2b2b', foreground='white')

        # Logo hoặc tiêu đề lớn
        self.title_label = ttk.Label(root, text="Face Anonymizer App", background='#2b2b2b', foreground='white', font=('Helvetica', 18, 'bold'))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Hiển thị video (khung video)
        self.video_label = tk.Label(root)
        self.video_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Thanh trượt điều chỉnh độ mờ
        self.blur_slider = tk.Scale(root, from_=1, to_=101, orient="horizontal", label="Blur Level", bg="#2b2b2b", fg="white", highlightbackground="#2b2b2b",command=self.update_blur, resolution=2)
        self.blur_slider.grid(row=2, column=0, padx=20, pady=10)

        self.pixeize_level = tk.Scale(root, from_=1, to_=50, orient="horizontal", label="Pixelize Level", bg="#2b2b2b", fg="white", highlightbackground="#2b2b2b",command=self.update_pixel, resolution=2)
        self.pixeize_level.pack()

        # Nút để chọn chế độ Blur
        self.blur_button = tk.Button(root, text="Blur", font=("Arial", 12, "bold"), bg="#2196F3", fg="white", command=self.apply_blur)
        self.blur_button.grid(row=3, column=0, padx=20, pady=10)

        # Nút để chọn chế độ Pixelize
        self.pixelize_button = tk.Button(root, text="Pixelize", font=("Arial", 12, "bold"), bg="#FF5722", fg="white", command=self.apply_pixelization)
        self.pixelize_button.grid(row=3, column=1, padx=20, pady=10)

        # Biến lưu trạng thái
        self.blur_value = 51
        self.pixelize_value = 10
        self.mode = "blur"

        # Video capture
        self.cap = cv2.VideoCapture(0)

        # Cập nhật frame video
        self.root.after(0, self.update_frame)

    def update_blur(self, value):
        self.blur_value = int(value)

    def update_pixel(self, value):
        self.pixelize_value = int(value)

    def apply_blur(self):
        self.mode = "blur"
        print(f"Mode changed to: {self.mode}")

    def apply_pixelization(self):
        self.mode = "pixelize"
        print(f"Mode changed to: {self.mode}")

    def update_frame(self):
        _, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Giả sử bạn có face_cascade để phát hiện khuôn mặt
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Áp dụng blur hoặc pixelization tùy theo mode
        if self.mode == "blur":
            print("Applying blur...")
            frame = blur_faces(frame, faces, self.blur_value)
        elif self.mode == "pixelize":
            print("Applying pixelization...")
            frame = pixelate_faces(frame, faces, self.pixelize_value)

        # Hiển thị video lên GUI
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        photo = ImageTk.PhotoImage(image=image)
        self.video_label.config(image=photo)
        self.video_label.image = photo

        self.root.after(10, self.update_frame)

# Hàm xử lý làm mờ khuôn mặt (ví dụ đơn giản)
def blur_faces(frame, faces, blur_value):
    for (x, y, w, h) in faces:
        face_region = frame[y:y+h, x:x+w]
        blurred_face = cv2.GaussianBlur(face_region, (blur_value, blur_value), 30)
        frame[y:y+h, x:x+w] = blurred_face
    return frame

# Hàm xử lý pixelization khuôn mặt (ví dụ đơn giản)
def pixelate_faces(frame, faces, pixel_size=10):
    for (x, y, w, h) in faces:
        face_region = frame[y:y+h, x:x+w]
        small = cv2.resize(face_region, (pixel_size, pixel_size), interpolation=cv2.INTER_LINEAR)
        pixelated_face = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
        frame[y:y+h, x:x+w] = pixelated_face
    return frame

def replace_faces_with_icon(frame, faces, icon_path):
    icon = cv2.imread(icon_path, cv2.IMREAD_UNCHANGED)
    for (x, y, w, h) in faces:
        icon_resized = cv2.resize(icon, (w, h))
        if icon_resized.shape[2] == 4:
            alpha_s = icon_resized[:, :, 3] / 255.0
            alpha_l = 1.0 - alpha_s
            for c in range(0, 3):
                frame[y: y+h, x: x+w, c] = (alpha_s * icon_resized[:, :, c] +
                                           alpha_l * frame[y: y+h, x: x+w, c])
        else:
            frame[y: y+h, x: x+w] = icon_resized
    return frame

icon_path = 'mixi.jpg'
anonymized_fram = replace_faces_with_icon(fram, faces, icon_path)

# Giả sử bạn đã khởi tạo face_cascade ở đây, ví dụ:
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Chạy ứng dụng
root = tk.Tk()
app = FaceAnonymizerApp(root)
root.mainloop()
