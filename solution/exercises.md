# Ngày 1 — Bài Tập & Phản Ánh
## Nền Tảng LLM API | Phiếu Thực Hành

**Thời lượng:** 1:30 giờ  
**Cấu trúc:** Lập trình cốt lõi (60 phút) → Bài tập mở rộng (30 phút)

---

## Phần 1 — Lập Trình Cốt Lõi (0:00–1:00)

Chạy các ví dụ trong Google Colab tại: https://colab.research.google.com/drive/172zCiXpLr1FEXMRCAbmZoqTrKiSkUERm?usp=sharing

Triển khai tất cả TODO trong `template.py`. Chạy `pytest tests/` để kiểm tra tiến độ.

**Điểm kiểm tra:** Sau khi hoàn thành 4 nhiệm vụ, chạy:
```bash
python template.py
```
Bạn sẽ thấy output so sánh phản hồi của GPT-4o và GPT-4o-mini.

---

## Phần 2 — Bài Tập Mở Rộng (1:00–1:30)

### Bài tập 2.1 — Độ Nhạy Của Temperature
Gọi `call_openai` với các giá trị temperature 0.0, 0.5, 1.0 và 1.5 sử dụng prompt **"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> *Khi temperature thấp như 0.0, phản hồi của mô hình ổn định, ít sáng tạo và tập trung vào thông tin chính xác, nhất quán. Khi tăng temperature lên 1.0 và 1.5, phản hồi trở nên đa dạng và chi tiết hơn, sử dụng cách diễn đạt phong phú hơn nhưng đôi khi cũng thay đổi số liệu hoặc thêm thông tin khác nhau giữa các lần gọi. Temperature càng cao thì mức độ ngẫu nhiên và sáng tạo của mô hình càng lớn.*

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> *Tôi sẽ đặt temperature khoảng 0.2–0.5 cho chatbot hỗ trợ khách hàng. Mức này giúp chatbot vẫn giữ được cách diễn đạt tự nhiên và thân thiện, nhưng đồng thời đảm bảo phản hồi đủ ổn định, chính xác và nhất quán trong các tình huống hỗ trợ thực tế. Temperature quá cao có thể khiến chatbot trả lời sáng tạo nhưng dễ thiếu chính xác hoặc lan man, không phù hợp trong các tình huống hỗ trợ thực tế.*

---

### Bài tập 2.2 — Đánh Đổi Chi Phí
Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350 token.

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> *Mỗi ngày có khoảng 10.000 người dùng, mỗi người gọi API 3 lần  với trung bình 350 token/call. Tổng số token mỗi ngày là khoảng 10.500.000 token. Với mức giá 0.010 USD / 1K output token cho GPT-4o và 0.0006 USD / 1K output token cho GPT-4o-mini, GPT-4o sẽ đắt hơn khoảng 16–17 lần so với GPT-4o-mini cho cùng workload này.*

**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> *Chi phí cao hơn của GPT-4o là xứng đáng trong các ứng dụng cần độ chính xác và khả năng suy luận cao, ví dụ như trợ lý pháp lý, phân tích tài liệu phức tạp hoặc hỗ trợ y tế. Ngược lại, GPT-4o-mini phù hợp hơn cho các tác vụ thường xuyên, quy mô lớn nhưng không yêu cầu chất lượng quá cao, chẳng hạn như chatbot chăm sóc khách hàng cơ bản, trả lời FAQ hoặc tạo nội dung ngắn với chi phí thấp hơn nhiều.*

---

### Bài tập 2.3 — Trải Nghiệm Người Dùng với Streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> *Streaming đặc biệt quan trọng trong các ứng dụng tương tác thời gian thực, như chatbot AI, trợ lý học tập hoặc công cụ hỗ trợ lập trình. Khi câu trả lời xuất hiện từng phần theo thời gian thực, người dùng cảm thấy hệ thống phản hồi nhanh hơn và tự nhiên hơn, ngay cả khi tổng thời gian xử lý không thay đổi. Ngược lại, non-streaming phù hợp hơn với các tác vụ cần kết quả hoàn chỉnh trước khi hiển thị, chẳng hạn như tạo báo cáo, phân tích dữ liệu hoặc xuất nội dung dài, vì người dùng thường ưu tiên tính đầy đủ và ổn định của kết quả hơn là tốc độ hiển thị ban đầu.*


## Danh Sách Kiểm Tra Nộp Bài
- [ ] Tất cả tests pass: `pytest tests/ -v`
- [ ] `call_openai` đã triển khai và kiểm thử
- [ ] `call_openai_mini` đã triển khai và kiểm thử
- [ ] `compare_models` đã triển khai và kiểm thử
- [ ] `streaming_chatbot` đã triển khai và kiểm thử
- [ ] `retry_with_backoff` đã triển khai và kiểm thử
- [ ] `batch_compare` đã triển khai và kiểm thử
- [ ] `format_comparison_table` đã triển khai và kiểm thử
- [ ] `exercises.md` đã điền đầy đủ
- [ ] Sao chép bài làm vào folder `solution` và đặt tên theo quy định 
