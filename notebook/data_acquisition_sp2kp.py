import requests
import pandas as pd
from datetime import date, timedelta
import time

# ==============================================================================
# BAGIAN 1: SETUP REQUEST (Ini adalah kode dari cURLconverter Anda)
# ==============================================================================

# Headers ini kita ambil langsung dari hasil konversi cURL Anda.
# Ini meniru browser Anda secara persis, sehingga lebih kuat.
headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9,id;q=0.8',
    'Connection': 'keep-alive',
    # 'Content-Type' tidak perlu didefinisikan di sini, karena library requests
    # akan membuatnya secara otomatis saat Anda menggunakan parameter 'files'.
    'DNT': '1',
    'Origin': 'https://sp2kp.kemendag.go.id',
    'Referer': 'https://sp2kp.kemendag.go.id/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

# URL endpoint API
url = 'https://api-sp2kp.kemendag.go.id/report/api/average-price/generate-perbandingan-harga'


# ==============================================================================
# BAGIAN 2: PROSES LOOPING DAN PENYIMPANAN DATA
# ==============================================================================

# Tentukan rentang tanggal yang Anda inginkan
start_date = date(2025, 2, 1)
end_date = date(2025, 10, 31) # Contoh sampai hari ini
delta = timedelta(days=1)

all_data_rows = []

current_date = start_date
while current_date <= end_date:
    tanggal_str = current_date.strftime("%Y-%m-%d")     
    print(f"Mengambil data untuk tanggal: {tanggal_str}...")

    # --- INI BAGIAN UTAMA YANG DIMODIFIKASI ---
    # Membuat dictionary 'files' di dalam loop agar tanggalnya dinamis
    files_payload = {
        'tanggal': (None, tanggal_str),
        'tanggal_pembanding': (None, '2024-02-01'), # Tanggal pembanding bisa dibuat tetap atau dinamis
        'kode_provinsi': (None, '35'), # Kode Provinsi Jawa Timur
        'kode_kab_kota': (None, '3573'), # Kode Kota Malang
    }

    try:
        # Kirim request POST menggunakan 'headers' dan 'files' yang sudah kita definisikan
        response = requests.post(
            url,
            headers=headers,
            files=files_payload,
            timeout=30 # Tambahkan timeout untuk mencegah script hang
        )
        
        # Periksa apakah request berhasil (status code 200)
        if response.status_code == 200:
            data = response.json()
            
            # Cek apakah ada data di dalam response JSON
            if data and data.get('data'):
                # Ambil list data harga
                list_harga = data['data']
                # Tambahkan kolom tanggal ke setiap baris data
                for item in list_harga:
                    item['tanggal_data'] = tanggal_str
                
                # Masukkan semua baris ke list utama
                all_data_rows.extend(list_harga)
                print(f"-> Sukses: {len(list_harga)} data komoditas ditemukan.")
            else:
                print("-> Sukses, namun tidak ada data harga untuk tanggal ini.")

        else:
            print(f"-> Gagal dengan status code: {response.status_code}")
            print("   Response:", response.text)

    except requests.exceptions.RequestException as e:
        print(f"-> Terjadi error saat request: {e}")

    # Pindah ke hari berikutnya
    current_date += delta
    # Beri jeda 1 detik antar request agar tidak membebani server
    time.sleep(1) 

# Setelah loop selesai, konversi semua data yang terkumpul menjadi DataFrame
if all_data_rows:
    df = pd.DataFrame(all_data_rows)
    
    # Simpan DataFrame ke file CSV
    nama_file = "dataset_raw.csv"
    df.to_csv(nama_file, index=False, encoding='utf-8-sig')
    print(f"\nProses selesai! Dataset telah disimpan ke file '{nama_file}'")
else:
    print("\nProses selesai, namun tidak ada data yang berhasil dikumpulkan.")
