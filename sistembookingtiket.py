print("=== SISTEM BOOKING TIKET BIOSKOP ===")
print("Halo! Selamat datang di sistem pemesanan tiket bioskop.\n")

nama_film = input("Masukkan nama film yang ingin ditonton: ")

jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))

total_harga = 0

for i in range(1, jumlah_tiket + 1):
    print(f"\n--- Tiket ke-{i} ---")

    jenis_tiket = input("Masukkan jenis tiket (Reguler/Premium): ").lower()
    usia = int(input("Masukkan usia penonton: "))

    if jenis_tiket == "reguler":
        if usia >= 13:
            harga = 35000
            kategori = "Dewasa"
        else:
            harga = 25000
            kategori = "Anak-anak"
    elif jenis_tiket == "premium":
        if usia >= 13:
            harga = 50000
            kategori = "Dewasa"
        else:
            harga = 40000
            kategori = "Anak-anak"
    else:
        print("Jenis tiket tidak valid. Gunakan 'Reguler' atau 'Premium'.")
        continue

    print(f"Kategori Penonton : {kategori}")
    print(f"Harga Tiket       : Rp{harga:,}")
    total_harga += harga

print("\n===============================")
print(f"Film yang ditonton : {nama_film}")
print(f"Jumlah tiket       : {jumlah_tiket}")
print(f"Total pembayaran   : Rp{total_harga:,}")
print("===============================")
print("Terima kasih telah memesan tiket di sistem kami!")
print("Selamat menonton!")
