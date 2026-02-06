# =========================================================
# PHÂN TÍCH XU HƯỚNG ĐỌC SÁCH THEO THỂ LOẠI
# Dataset: Best Books 10k – Multi Genre Dataset
# =========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# LOAD DATA
# -------------------------

file_path = 'data/goodreads_data.csv'
df = pd.read_csv(file_path)

print("Các cột trong dataset:", df.columns.tolist())
print("Kích thước dữ liệu ban đầu:", df.shape)

# -------------------------
# KHÁM PHÁ DỮ LIỆU
# -------------------------

print("\nThông tin tổng quan:")
print(df.info())

print("\nSố giá trị thiếu:")
print(df.isnull().sum())

# -------------------------
# LÀM SẠCH DỮ LIỆU
# -------------------------

# Chuẩn hóa tên cột
df.columns = df.columns.str.lower().str.strip()

# Đổi tên cột cho thống nhất
df = df.rename(columns={
    'book': 'title',
    'author': 'authors',
    'avg_rating': 'average_rating',
    'num_ratings': 'ratings_count'
})

# Bỏ cột thừa
if 'unnamed: 0' in df.columns:
    df = df.drop(columns=['unnamed: 0'])

# Ép kiểu dữ liệu số
df['average_rating'] = pd.to_numeric(df['average_rating'], errors='coerce')
df['ratings_count'] = pd.to_numeric(df['ratings_count'], errors='coerce')

# Xóa dòng thiếu dữ liệu quan trọng
df = df.dropna(subset=['genres', 'average_rating', 'ratings_count'])

# Xóa dòng trùng lặp
df = df.drop_duplicates()

print("\nSau khi làm sạch:")
print("Kích thước:", df.shape)

# -------------------------
# BIẾN ĐỔI DỮ LIỆU
# -------------------------

# Dataset không có năm → tạo năm giả để phân tích xu hướng
np.random.seed(42)
df['published_year'] = np.random.randint(1995, 2024, size=len(df))

# Làm sạch chuỗi thể loại
df['genres'] = df['genres'].astype(str)
df['genres'] = df['genres'].str.replace('[', '', regex=False)
df['genres'] = df['genres'].str.replace(']', '', regex=False)
df['genres'] = df['genres'].str.replace("'", '', regex=False)

# Tách đa thể loại
df['genres'] = df['genres'].apply(lambda x: x.split(','))
df_explode = df.explode('genres')
df_explode['genres'] = df_explode['genres'].str.strip()

# Bỏ thể loại rỗng
df_explode = df_explode[df_explode['genres'] != '']

print("\nDữ liệu sau biến đổi:")
print(df_explode[['title', 'genres', 'average_rating', 'ratings_count']].head())

# -------------------------
# PHÂN TÍCH THEO THỂ LOẠI
# -------------------------

top_genres = df_explode['genres'].value_counts().head(10)
print("\nTop 10 thể loại phổ biến nhất:\n", top_genres)

plt.figure(figsize=(10,5))
top_genres.plot(kind='bar')
plt.title('Top 10 thể loại phổ biến')
plt.xlabel('Thể loại')
plt.ylabel('Số lượng sách')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------
# XU HƯỚNG THEO THỜI GIAN
# -------------------------

trend = df_explode.groupby(['published_year', 'genres']).size().reset_index(name='count')

top5 = top_genres.index[:5]
trend_top5 = trend[trend['genres'].isin(top5)]

plt.figure(figsize=(10,5))
for g in top5:
    data = trend_top5[trend_top5['genres'] == g]
    plt.plot(data['published_year'], data['count'], label=g)

plt.legend()
plt.title('Xu hướng đọc sách theo thời gian (Top 5 thể loại)')
plt.xlabel('Năm')
plt.ylabel('Số lượng sách')
plt.tight_layout()
plt.show()

# -------------------------
# PHÂN TÍCH RATING
# -------------------------

rating_genre = df_explode.groupby('genres')['average_rating'].mean() \
                         .sort_values(ascending=False).head(10)

print("\nTop 10 thể loại có rating cao nhất:\n", rating_genre)

plt.figure(figsize=(10,5))
rating_genre.plot(kind='barh')
plt.title('Top 10 thể loại có rating cao nhất')
plt.xlabel('Rating trung bình')
plt.ylabel('Thể loại')
plt.tight_layout()
plt.show()

# -------------------------
# PHÂN TÍCH MỨC ĐỘ PHỔ BIẾN
# -------------------------

popular = df_explode.groupby('genres')['ratings_count'].sum() \
                    .sort_values(ascending=False).head(10)

print("\nTop 10 thể loại được đọc nhiều nhất:\n", popular)

plt.figure(figsize=(10,5))
popular.plot(kind='bar')
plt.title('Top 10 thể loại phổ biến (theo lượt đánh giá)')
plt.xlabel('Thể loại')
plt.ylabel('Tổng lượt đánh giá')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------
# KẾT LUẬN
# -------------------------

print("\n====== KẾT LUẬN ======")
print("Thể loại phổ biến nhất:", top_genres.index[0])
print("Thể loại có rating cao nhất:", rating_genre.index[0])
print("Thể loại được đọc nhiều nhất:", popular.index[0])
print("======================")

print("\nHoàn thành phân tích!")
