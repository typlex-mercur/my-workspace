# 🎓 Typlex All-in-One Workspace & GPA Tracker

Hệ thống cá nhân All-in-One kết hợp toàn diện giữa **GPA Tracker**, **Thời khóa biểu (Timetable)**, **Lịch & Quản lý Nhiệm vụ**, **Phòng học Focus (Pomodoro)**, **Trình phát nhạc Miniplayer** và **Đồng bộ thời gian thực (Real-time Cloud Sync)** trên mọi thiết bị (PC, Laptop, Điện thoại iOS/Android).

---

## 🌟 Các Phân hệ Tính năng Chính

### 1. 📊 Tổng quan (Overview Hub)
- Thẻ thống kê thời gian thực: CGPA hiện tại, Tín chỉ tích lũy, Thời gian học trong ngày.
- **Lớp học hôm nay**: Tự động lọc và hiển thị ca học, phòng học theo thời khóa biểu ngày hiện tại.
- **Nhiệm vụ hôm nay**: Thêm nhanh việc cần làm và đánh dấu hoàn thành trực tiếp từ trang chủ.
- **Widget Focus & Miniplayer**: Bắt đầu phiên tập trung nhanh hoặc bật nhạc chỉ với 1 click.

### 2. 🎓 GPA Tracker (Quản lý Điểm & Dự báo Mục tiêu)
- Quản lý học kỳ dạng accordion tiện lợi, hỗ trợ thêm/sửa/xóa môn học.
- Tự động tính toán điểm hệ 10, quy đổi điểm chữ (A+, A, B+, B, C+, C, D+, D, F) và điểm hệ 4.0.
- Tính GPA từng học kỳ và CGPA toàn khóa học.
- Biểu đồ biến động GPA qua các kỳ học bằng Chart.js (tương thích hoàn hảo Dark/Light mode).
- **Bộ dự báo Mục tiêu (Goal Predictor)**: Nhập điểm mục tiêu mong muốn $\to$ hệ thống tự động phân tích GPA cần đạt và gợi ý lộ trình số môn đạt điểm A+, A, B+ cho các tín chỉ còn lại.
- Nút liên kết nhanh: Đưa môn học từ GPA Tracker vào Thời khóa biểu chỉ với 1 chạm.

### 3. 📅 Thời khóa biểu Hàng tuần (Weekly Timetable)
- Chế độ xem **Ma trận Lưới tuần (Weekly Grid)** trên máy tính và **Danh sách theo ngày (Day Cards)** trên điện thoại.
- Thêm lớp học linh hoạt:
  - Ngày trong tuần (Thứ 2 $\to$ Chủ Nhật).
  - Ca học (Ca 1 $\to$ Ca 5 hoặc khung giờ tùy chỉnh).
  - Phòng học (ví dụ: `203B`, `Giảng đường C`, `Lab 402`...).
  - Giảng viên & Ghi chú (ví dụ: `Mang laptop thực hành`, `Kiểm tra 15p`...).
  - Nhãn màu sắc phân loại môn học (Xanh dương, Xanh lá, Vàng cam, Tím, Đỏ hồng).

### 4. ✅ Lịch Tháng & Quản lý Nhiệm vụ (Calendar & Tasks)
- Lịch tháng tương tác với **Heatmap năng suất**:
  - Huy hiệu xanh lá nếu học $\ge 6$ giờ trong ngày.
  - Huy hiệu xanh dương nếu có thời gian học trong ngày.
  - Tỷ lệ hoàn thành công việc (ví dụ: `☑ 3/5`).
- Danh sách việc cần làm (To-Do List) chi tiết theo từng ngày: Checkbox hoàn thành, xóa việc đã xong, chỉnh sửa thời gian học thủ công.

### 5. ⏱️ Phòng Focus & Pomodoro
- Chế độ Pomodoro (25m), Nghỉ ngắn (5m), Nghỉ dài (15m), Deep Work (45m) hoặc Tùy chỉnh (1 - 240 phút).
- Cơ chế **System Clock Delta Sync**: Đảm bảo đồng hồ chạy chuẩn xác 100%, không bị sai lệch hay đứng hình khi tắt màn hình điện thoại hoặc chuyển tab.
- Tự động ghi nhận thời gian học (Study Time Logging) vào Lịch ngày hôm đó khi hoàn thành.
- Nút **"🛑 Kết thúc & Lưu"**: Dừng sớm và ghi nhận chính xác số phút đã học thực tế.
- Âm thanh chuông báo (Web Audio API) khi kết thúc phiên học.
- Danh ngôn truyền cảm hứng thay đổi ngẫu nhiên theo khung giờ.

### 6. 🎵 Persistent Miniplayer (Nhạc Học tập & Lo-Fi)
- Cửa sổ nổi (Floating) hoặc ghim góc màn hình, không bị ngắt quãng khi chuyển qua lại giữa các tab tính năng.
- Tích hợp sẵn 7+ Playlist chọn lọc (RandomVie, Motiv, Đánh đổi, BGM Study, Ballad Chill, Hà Nội Lofi, Lofi Girl Beats).
- Hỗ trợ thêm Playlist YouTube cá nhân tùy ý.
- Công nghệ **Google Cloud YouTube Data API v3** & **True Shuffle** (xáo trộn ngẫu nhiên thực sự toàn bộ video trong playlist).
- Phím tắt toàn cục:
  - `Space`: Bắt đầu / Tạm dừng Focus Timer.
  - `←` / `→`: Chuyển bài hát trước / sau.

### 7. 💾 Sao lưu & Phục hồi JSON Local & Mobile PWA
- **Lưu trữ Offline 100%**: Mọi dữ liệu (Điểm số, TKB, Nhiệm vụ, Cài đặt) được lưu an toàn trong `localStorage` của trình duyệt.
- **Xuất / Nhập JSON (Backup & Restore)**: Mở menu Cài đặt ⚙️ để tải bản sao lưu file `.json` hoặc nhập dữ liệu sang máy/thiết bị khác chỉ với 1 chạm.
- **PWA (Progressive Web App)**: Cài đặt trực tiếp lên màn hình chính điện thoại (Add to Home Screen) trên cả iOS và Android, hỗ trợ sử dụng mượt mà khi offline.

---

## 🚀 Hướng dẫn Sử dụng

### 1. Trên Máy tính (PC / Laptop)
- Cách 1: Chạy file `run.vbs` (chạy ngầm không hiện cửa sổ đen) hoặc `mywsp.bat`.
- Cách 2: Mở trực tiếp file `index.html` trên trình duyệt bất kỳ.

### 2. Trên Điện thoại (Mobile - iOS / Android)
- Host thư mục này lên GitHub Pages, Vercel hoặc server local của bạn.
- Mở liên kết trên trình duyệt Safari (iOS) hoặc Chrome (Android).
- Chọn **"Thêm vào Màn hình chính" (Add to Home Screen)** để cài đặt ứng dụng độc lập như Native App.

### 3. Sao lưu & Đồng bộ Dữ liệu Thủ công
1. Nhấn nút **Cài đặt ⚙️** ở thanh điều hướng trên cùng.
2. Chọn **Xuất file JSON** để tải file sao lưu về máy.
3. Trên thiết bị mới hoặc trình duyệt khác, mở **Cài đặt ⚙️** $\to$ Chọn **Nhập file JSON** để khôi phục toàn bộ dữ liệu.
