import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv('lab1/ITA105_Lab_1.csv')

# Bài 1: Khám phá
print("--- KẾT QUẢ BÀI 1 ---")
print(df.shape)
print(df.isnull().sum())
input("\n[Đã xong Bài 1] Nhấn Enter để chạy Bài 2...")

# Bài 2: Xử lý thiếu
print("\n--- KẾT QUẢ BÀI 2 ---")
df['Price'] = df['Price'].fillna(df['Price'].mean())
df['Rating'] = df['Rating'].fillna(df['Rating'].mode()[0])
print("Đã điền giá trị thiếu.")
input("\n[Đã xong Bài 2] Nhấn Enter để chạy Bài 3...")

# Bài 3: Xử lý lỗi
print("\n--- KẾT QUẢ BÀI 3 ---")
df = df[(df['Price'] > 0) & (df['StockQuantity'] >= 0)]
df = df[(df['Rating'] >= 1) & (df['Rating'] <= 5)]
print("Đã lọc dữ liệu lỗi.")
input("\n[Đã xong Bài 3] Nhấn Enter để xem Biểu đồ Bài 4...")

# Bài 4: Làm mượt & Vẽ hình
print("\n--- KẾT QUẢ BÀI 4 ---")
df['Price_MA'] = df['Price'].rolling(window=3).mean()
df[['Price', 'Price_MA']].head(50).plot(figsize=(10, 5))
print("Đang hiển thị biểu đồ... (Hãy tắt cửa sổ biểu đồ để chạy tiếp Bài 5)")
plt.show()

# Bài 5: Chuẩn hóa
print("\n--- KẾT QUẢ BÀI 5 ---")
df['Category'] = df['Category'].str.lower()
df['Description'] = df['Description'].str.strip()
df['Price_VND'] = df['Price'] * 25000
print(df.head())
print("\n--- HOÀN THÀNH BÀI LAB ---")