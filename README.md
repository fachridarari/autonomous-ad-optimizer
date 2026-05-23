# Autonomous Ad-Performance Optimizer
Sistem AI Agent yang memantau performa iklan secara otonom, menganalisis data *real-time*, dan memberikan optimasi konten berbasis model bahasa lokal (Llama 3.1). Proyek ini dirancang untuk otomasi e-commerce yang mengutamakan privasi data dan efisiensi operasional.

## 🚀 Fitur Utama
* **Autonomous Decision Engine:** Logika berbasis *threshold* untuk mendeteksi performa iklan secara instan.
* **Local AI Integration:** Menggunakan Ollama (Llama 3.1) untuk pembuatan *ad-copy* kreatif tanpa biaya API.
* **Audit Trail:** Sistem otomatis menyimpan log keputusan ke `logs/` untuk keperluan evaluasi.
* **Modular Architecture:** Struktur proyek yang rapi dan siap untuk skalabilitas tinggi.

## ⚙️ How it Works
![Alur Kerja Agent](logs/hasil_agent.png)

Sistem ini menjalankan *loop* optimasi sebagai berikut:
1. **Data Ingestion:** Agent membaca performa iklan dari `data/ad_data.csv`.
2. **Analysis:** Jika ROAS di bawah target (2.0), sistem akan memicu *Brain* (AI Agent).
3. **Execution:** Llama 3.1 secara otomatis menyusun variasi *copy* iklan baru yang lebih persuasif.
4. **Audit Trail:** Hasil keputusan dan *copy* baru disimpan di `logs/laporan_optimasi.json`.

## 🛠️ Cara Menjalankan
1. Pastikan **Ollama** terinstall dan model `llama3.1` sudah didownload.
2. Install dependensi:
   ```bash
   pip install -r requirements.txt
3. Jalankan Agent:
   ```bash
   python agents/optimizer_agent.py

## 🚀 Future Improvements

1. **API Integration:** Menghubungkan langsung ke Meta, Google, dan TikTok Marketing API.
2. **Database Migration:** Migrasi ke PostgreSQL/Supabase untuk data logging yang lebih kompleks.
3. **Observability:** Integrasi dengan Langfuse untuk tracking kualitas keputusan AI (evals).
4. **Cloud Deployment:** Otomatisasi *cron job* di cloud agar berjalan 24/7.

*Proyek ini dikembangkan sebagai solusi otomasi e-commerce yang efisien dan aman. Jika Anda tertarik untuk berkolaborasi atau memiliki pertanyaan mengenai implementasi sistem ini, silakan hubungi saya melalui GitHub.*

### Langkah terakhir untuk Anda:
1. Simpan (Save) isi di atas ke dalam file bernama **`README.md`** (pastikan tidak ada `.md` ganda).
2. Jalankan perintah ini di terminal VS Code Anda:
   ```bash
   git add README.md
   git commit -m "docs: finalize professional README layout"
   git push origin main

Setelah ini, repositori Anda sudah benar-benar siap dan terlihat sangat profesional. Apakah ada hal lain lagi yang ingin Anda tanyakan atau persiapkan?
