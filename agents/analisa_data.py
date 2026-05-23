import pandas as pd

# Membaca file CSV yang tadi Anda buat
# Pastikan nama filenya sama persis dengan yang Anda simpan
data = pd.read_csv('penjualan.csv')

# Menampilkan 5 baris pertama untuk memastikan Python berhasil membaca data
print("Data berhasil dimuat:")
print(data.head())

# Menampilkan ringkasan singkat (Total rata-rata penjualan)
print("\nRingkasan Penjualan:")
print(data.describe())

# Menambahkan logika keputusan (Decision Logic)
print("\n--- ANALISA OTOMATIS AGENT ---")
for index, row in data.iterrows():
    # Contoh aturan: Jika penjualan di bawah 80, berikan peringatan
    if row['Penjualan'] < 80:
        print(f"[{row['Tanggal']}] PERINGATAN: Penjualan {row['Nama_Produk']} rendah ({row['Penjualan']}). Segera update iklan!")
    elif row['Penjualan'] >= 100:
        print(f"[{row['Tanggal']}] INFO: Penjualan {row['Nama_Produk']} bagus ({row['Penjualan']}). Pertahankan!")
    else:
        print(f"[{row['Tanggal']}] INFO: Penjualan {row['Nama_Produk']} stabil ({row['Penjualan']}).")

import json

# Menyiapkan list untuk menampung hasil keputusan
hasil_log = []

for index, row in data.iterrows():
    tindakan = ""
    if row['Penjualan'] < 80:
        tindakan = "Segera update iklan!"
    elif row['Penjualan'] >= 100:
        tindakan = "Pertahankan!"
    else:
        tindakan = "Monitor."

    # Menyimpan hasil ke dalam list
    hasil_log.append({
        "tanggal": row['Tanggal'],
        "produk": row['Nama_Produk'],
        "penjualan": int(row['Penjualan']),
        "rekomendasi": tindakan
    })

# Menyimpan hasil ke file JSON (Simulasi database/log)
with open('laporan_optimasi.json', 'w') as f:
    json.dump(hasil_log, f, indent=4)

print("\n[SUKSES] Laporan optimasi telah disimpan ke 'laporan_optimasi.json'")

def kirim_notifikasi_iklan(produk, rekomendasi):
    # Simulasi mengirim perintah ke API Iklan (Meta/TikTok/Google)
    print(f"\n[API CALL] Sedang mengirim instruksi ke Platform Iklan untuk produk: {produk}...")
    print(f"[API CALL] Perintah: {rekomendasi}")
    print("[API CALL] Status: Berhasil Terkirim ke Server Iklan.\n")

# Integrasikan fungsi ini ke dalam loop keputusan kita
for item in hasil_log:
    if item['rekomendasi'] == "Segera update iklan!":
        kirim_notifikasi_iklan(item['produk'], item['rekomendasi'])