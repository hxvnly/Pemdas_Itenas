import pandas as pd
import numpy as np

# Data
data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

# DataFrame
df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
df['Gaji_Tambahan'] = df.apply(lambda row: row['Gaji'] * 0.05 if row['Usia'] <= 30 else row['Gaji'] * 0.07, axis=1)

# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
print("DataFrame setelah peningkatan gaji tambahan:")
print(df)

# Pertanyaan 3:
# Tampilkan orang yang mendapatkan gaji tambahan
print("\nOrang yang mendapatkan gaji tambahan:")
print(df[df['Gaji_Tambahan'] > 0][['Nama', 'Usia', 'Gaji_Tambahan']])

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.
print("\nDataFrame setelah peningkatan gaji tambahan:")
print(df[['Nama', 'Usia', 'Gaji_Tambahan']])
print("\nRingkasan hasil setelah peningkatan gaji tambahan:")
print(df[['Usia', 'Gaji_Tambahan']].describe().astype(int))  # Convert to integers for 'Usia'
