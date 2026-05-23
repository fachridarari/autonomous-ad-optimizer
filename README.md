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

 Tentu, mari kita rapikan file README.md Anda. Anda bisa langsung melakukan copy-paste draf di bawah ini ke dalam file README.md di komputer Anda. Saya telah menyesuaikan instruksi cara menjalankannya dengan struktur folder baru Anda (agents/) dan menambahkan bagian-bagian profesional.

Salin konten ini ke README.md:
Markdown
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
Jalankan Agent:

Bash
python agents/optimizer_agent.py

## 🚀 Future Improvements
1. API Integration: Menghubungkan langsung ke Meta, Google, dan TikTok Marketing API.
2. Database Migration: Migrasi ke PostgreSQL/Supabase untuk data logging yang lebih kompleks.
3. Observability: Integrasi dengan Langfuse untuk tracking kualitas keputusan AI (evals).
4. Cloud Deployment: Otomatisasi cron job di cloud agar berjalan 24/7.

Proyek ini dikembangkan sebagai solusi otomasi e-commerce yang efisien dan aman.

---

### Langkah terakhir setelah *save* file ini:

1.  **Rename file:** Pastikan di laptop Anda file tersebut bernama `README.md` (hapus `.md` ganda jika ada).
2.  **Upload:** Jalankan perintah berikut di terminal VS Code Anda:
    ```bash
    git add README.md
    git commit -m "docs: update professional README with workflow and local AI features"
    git push origin main
    ```

Setelah ini, buka repositori GitHub Anda. File `README.md` Anda sekarang akan tampil dengan **sangat profesional**, lengkap dengan fitur, alur kerja, dan instruksi yang jelas bagi siapa pun yang melihatnya. 

Apakah ada bagian lain dari portofolio ini yang ingin Anda poles agar lebih menarik?
