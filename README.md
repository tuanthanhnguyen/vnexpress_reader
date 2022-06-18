# Voice reader for [Vnexpress](https://vnexpress.net)
Phần mềm đọc tin trên báo Vnexpress

## Cách sử dụng:
```
git clone https://github.com/tuanthanhnguyen/vnexpress_reader.git
cd vnexpress_reader/src
pip install -r requirements.txt
python main.py
```
### **Chú ý : Phần mềm không thể hoạt động nếu không có file config.ini trong cùng thư mục**
## Chỉnh sửa config.ini:

1. ```save_html_content``` (True/False) : Lưu trang chủ Vnexpress dưới dạng html (thường để debug)
2. ```log_erors``` (True/False) : Lưu lại các lỗi khi chạy
3. ```save_article_text``` (True/False) : Lưu bài đọc dưới dạng văn bản
4. ```save_article_audio``` (True/False) : Lưu bài đọc dưới dạng văn âm thanh