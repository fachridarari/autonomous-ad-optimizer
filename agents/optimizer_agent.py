import pandas as pd
from langchain_ollama import OllamaLLM

# 1. Gunakan nama model yang persis dengan yang sedang di-download
llm = OllamaLLM(model="llama3.1")

# 2. Load data (Pastikan file ad_data.csv ada di folder yang sama)
try:
    df = pd.read_csv('ad_data.csv', sep=';', on_bad_lines='warn')
    print("[INFO] Data berhasil dimuat.")
except FileNotFoundError:
    print("[ERROR] File ad_data.csv tidak ditemukan!")
    exit()

# 3. Logika Agent
print("\n--- [AGENT] Memulai Analisa Optimasi ---")

for index, row in df.iterrows():
    # Cek apakah ROAS di bawah target (2.0)
    if row['roas'] < 2.0:
        print(f"\n[!] Iklan {row['ad_id']} terdeteksi performa rendah (ROAS: {row['roas']})")
        
        prompt = f"""
        Tugas: Berikan copy iklan baru yang lebih persuasif.
        Konteks: Iklan saat ini adalah '{row['current_copy']}'.
        Tujuan: Meningkatkan ROAS.
        Berikan jawaban singkat dan langsung pada intinya.
        """
        
        # Panggil AI lokal
        print("[AGENT] Sedang berpikir...")
        rekomendasi = llm.invoke(prompt)
        
        print(f"Rekomendasi Copy Baru: {rekomendasi}")
    else:
        print(f"\n[OK] Iklan {row['ad_id']} berkinerja baik (ROAS: {row['roas']}). Tidak perlu tindakan.")