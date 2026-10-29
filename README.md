# Cập nhật lan truyền – Quản lý nhập xuất tồn

Đồ án Hệ thống phân tán, đề 8. 1 client + 4 server (S1–S4), primary-backup.

## Cài đặt môi trường

Yêu cầu: Python 3.12, Docker Desktop.

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements-dev.txt
```

Kiểm tra trước khi push:

```bash
ruff format --check .
ruff check .
pytest
```

## Chạy cụm 4 node

(bổ sung khi có docker-compose.yml)

## Quy ước

- Nhánh: feat/<module>
- Commit: <loại>(<module>): <mô tả tiếng Việt>
