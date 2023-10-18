from prettytable import PrettyTable
import csv

tabelSiswa = PrettyTable(["No.", "Nomor Induk Siswa", "Nama", "Kelas", "Nilai"])

# Fungsi untuk membaca data dari file CSV
def baca_data():
    no_urut = 1  # Inisialisasi nomor urut
    try:
        with open("data_siswa.csv", mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Lewati baris header
            for row in reader:
                tabelSiswa.add_row([no_urut] + row)
                no_urut += 1  # Increment nomor urut
    except FileNotFoundError:
        print("File data_siswa.csv belum ada. Anda bisa menambahkan data dengan fungsi tambah() terlebih dahulu.")
    
    return no_urut  # Mengembalikan nomor urut terbaru

# Panggil fungsi baca_data() untuk membaca data saat script dijalankan
no_urut = baca_data()

def tampilkan_tabel():
    print(tabelSiswa)
    print("============================")
    print("++++++++++++MENU++++++++++++")
    print("============================")
    print("tambah() => Menambahkan Data")
    print("hapus() => Menghapus Data   ")
    print("============================")

def tambah():
    global no_urut  # Gunakan variabel global untuk nomor urut
    nis = input("Masukan Nis: ")
    nama = input("Masukan Nama: ")
    kelas = input("Masukan Kelas: ")
    nilai = input("Masukan Nilai: ")
    tabelSiswa.add_row([no_urut, nis, nama, kelas, nilai])
    
    # Menyimpan data ke dalam file CSV
    with open("data_siswa.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nis, nama, kelas, nilai])
    
    no_urut += 1  # Increment nomor urut setiap kali menambah data
    
    tampilkan_tabel()  # Tampilkan tabel setelah menambah data

def hapus():
    global no_urut
    nomor_hapus = int(input("Masukkan nomor urut yang ingin dihapus: "))
    
    if 1 <= nomor_hapus <= no_urut:
        # Hapus baris sesuai dengan nomor urut yang dimasukkan
        tabelSiswa.del_row(nomor_hapus - 1)
        no_urut -= 1
        
        # Simpan kembali data ke dalam file CSV
        with open("data_siswa.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nomor Induk Siswa", "Nama", "Kelas", "Nilai"])  # Tulis header
            for row in tabelSiswa:
                data = row.get_string().split()
                writer.writerow(data[1:])  # Tulis data ke file CSV tanpa nomor urut
        
        print(f"Data dengan nomor urut {nomor_hapus} telah dihapus.")
        tampilkan_tabel()  # Tampilkan tabel setelah menghapus data
    else:
        print("Nomor urut tidak valid.")

# Tampilkan tabel saat script pertama kali dijalankan
tampilkan_tabel()

# Panggil fungsi tambah() atau hapus() sesuai kebutuhan
# tambah()
# hapus()
