# Inisialisasi data kontak
kontak = {}

# Fungsi untuk menampilkan daftar kontak
def tampilkan_daftar():
    print("Daftar Kontak:")
    for nama, no_hp in kontak.items():
        print(f"{nama}: {no_hp}")
    print()

# Fungsi untuk menambahkan kontak
def tambahkan_kontak():
    nama = input("Masukkan nama kontak: ")
    no_hp = input("Masukkan nomor HP kontak: ")
    kontak[nama] = no_hp
    print("Kontak berhasil ditambahkan!\n")

# Fungsi untuk menghapus kontak
def hapus_kontak():
    no_hp = input("Masukkan nomor HP yang ingin dihapus: ")
    for nama, hp in kontak.items():
        if hp == no_hp:
            del kontak[nama]
            print("Kontak berhasil dihapus!\n")
            return
    print("Nomor HP tidak ditemukan.\n")

# Fungsi untuk mencari kontak
def cari_kontak():
    nama = input("Masukkan nama kontak yang ingin dicari: ")
    if nama in kontak:
        print(f"Kontak ditemukan: {nama}: {kontak[nama]}\n")
    else:
        print("Kontak tidak ditemukan.\n")

# Program utama
while True:
    print("Menu:")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("5. Keluar Program")

    pilihan = input("Masukkan pilihan (1-5): ")

    if pilihan == '1':
        tampilkan_daftar()
    elif pilihan == '2':
        tambahkan_kontak()
    elif pilihan == '3':
        hapus_kontak()
    elif pilihan == '4':
        cari_kontak()
    elif pilihan == '5':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1-5.\n")


