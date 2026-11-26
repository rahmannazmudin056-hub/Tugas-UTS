from dokter import Dokter
from perawat import Perawat
from kunjungan_pasien import KunjunganPasien


def main():
    daftar_petugas = [
        Dokter("DK01", "dr. Andi Wijaya, Sp.PD", "Pagi", "Penyakit Dalam", "STR-112233", 150000, "Aktif"),
        Dokter("DK02", "dr. Sinta Lestari", "Siang", "Umum", "STR-445566", 75000, "Cuti"),
        Perawat("PR01", "Ns. Rina Kusuma, S.Kep", "Pagi", "Rawat Jalan", "Ners", 6, "Aktif"),
        Perawat("PR02", "Budi Santoso, A.Md.Kep", "Malam", "IGD", "Vokasi", 2, "Aktif"),
    ]
    daftar_kunjungan = []

    while True:
        print("\n=== SISTEM INFORMASI KLINIK ===")
        print("1. Tambah Data (Dokter / Perawat / Kunjungan Pasien)")
        print("2. Tampilkan Data (Tenaga Medis & Kunjungan Pasien)")
        print("3. Cari Data (Berdasarkan ID atau Nama Tenaga Medis)")
        print("4. Ubah Data (Shift / Status Aktif / Tarif Dokter)")
        print("5. Cek Status Data (Status Bertugas & Status Kunjungan)")
        print("6. Keluar dari Program")

        pilihan = input("Pilih menu (1-6): ").strip()

        # 1. TAMBAH DATA
        if pilihan == "1":
            print("\n--- TAMBAH DATA ---")
            print("a. Tambah Dokter")
            print("b. Tambah Perawat")
            print("c. Tambah Kunjungan Pasien")
            sub = input("Pilih jenis data (a/b/c): ").strip().lower()

            if sub == "a":
                id_p = input("ID Dokter (misal DK03): ").strip().upper()
                nama = input("Nama Dokter: ").strip()
                shift = input("Shift (Pagi/Siang/Malam): ").strip()
                spesialisasi = input("Spesialisasi: ").strip()
                str_no = input("Nomor STR: ").strip()
                tarif = float(input("Tarif Konsultasi (Rp): "))
                dokter_baru = Dokter(id_p, nama, shift, spesialisasi, str_no, tarif, "Aktif")
                daftar_petugas.append(dokter_baru)
                print("Data dokter berhasil ditambahkan!")

            elif sub == "b":
                id_p = input("ID Perawat (misal PR03): ").strip().upper()
                nama = input("Nama Perawat: ").strip()
                shift = input("Shift (Pagi/Siang/Malam): ").strip()
                unit = input("Unit Kerja (IGD/Rawat Jalan/Rawat Inap): ").strip()
                level = input("Level Perawat (Ners/Vokasi): ").strip()
                pengalaman = int(input("Pengalaman Kerja (tahun): "))
                perawat_baru = Perawat(id_p, nama, shift, unit, level, pengalaman, "Aktif")
                daftar_petugas.append(perawat_baru)
                print("Data perawat berhasil ditambahkan!")

            elif sub == "c":
                if not daftar_petugas:
                    print("Belum ada tenaga medis terdaftar.")
                    continue
                kode_k = f"KUN-{len(daftar_kunjungan) + 1:03d}"
                pasien = input("Nama Pasien: ").strip()
                keluhan = input("Keluhan Pasien: ").strip()

                print("\nDaftar Tenaga Medis:")
                for p in daftar_petugas:
                    print(" -", p.info_tenaga_medis())

                id_pilih = input("Masukkan ID Tenaga Medis yang menangani: ").strip().upper()
                petugas_dipilih = next(
                    (p for p in daftar_petugas if p.get_id_pegawai() == id_pilih), None
                )
                if petugas_dipilih:
                    if petugas_dipilih.bisa_melayani():
                        kunjungan_baru = KunjunganPasien(kode_k, pasien, keluhan, petugas_dipilih)
                        daftar_kunjungan.append(kunjungan_baru)
                        print("Data kunjungan pasien berhasil dicatat!")
                    else:
                        print("Tenaga medis sedang tidak aktif/cuti. Pilih petugas lain.")
                else:
                    print("ID tenaga medis tidak ditemukan.")
            else:
                print("Pilihan tidak valid.")

        # 2. TAMPILKAN DATA
        elif pilihan == "2":
            print("\n--- DAFTAR TENAGA MEDIS ---")
            for p in daftar_petugas:
                print(p.info_tenaga_medis())

            print("\n--- DAFTAR KUNJUNGAN PASIEN ---")
            if not daftar_kunjungan:
                print("Belum ada kunjungan pasien.")
            else:
                for k in daftar_kunjungan:
                    print(k.info_kunjungan())

        # 3. CARI DATA
        elif pilihan == "3":
            kata = input("\nMasukkan ID atau Nama Tenaga Medis: ").strip().lower()
            hasil = [
                p
                for p in daftar_petugas
                if kata in p.get_id_pegawai().lower() or kata in p.get_nama().lower()
            ]
            if hasil:
                print(f"\nDitemukan {len(hasil)} data:")
                for p in hasil:
                    print(" ->", p.info_tenaga_medis())
            else:
                print("Data tidak ditemukan.")

        # 4. UBAH DATA
        elif pilihan == "4":
            print("\n--- UBAH DATA ---")
            print("a. Ubah Data Tenaga Medis")
            print("b. Ubah Status Kunjungan Pasien")
            sub_ubah = input("Pilih (a/b): ").strip().lower()

            if sub_ubah == "a":
                id_ubah = input("Masukkan ID Tenaga Medis: ").strip().upper()
                target = next(
                    (p for p in daftar_petugas if p.get_id_pegawai() == id_ubah), None
                )
                if target:
                    print("Data saat ini:", target.info_tenaga_medis())
                    shift_baru = input("Shift Baru (Pagi/Siang/Malam): ").strip()
                    status_baru = input("Status Baru (Aktif/Cuti): ").strip()
                    target.set_shift(shift_baru)
                    target.set_status_aktif(status_baru)
                    if isinstance(target, Dokter):
                        tarif_baru = float(input("Tarif Konsultasi Baru (Rp): "))
                        target.set_tarif_konsultasi(tarif_baru)
                    print("Data tenaga medis berhasil diperbarui!")
                else:
                    print("ID tidak ditemukan.")

            elif sub_ubah == "b":
                kode_ubah = input("Masukkan Kode Kunjungan (misal KUN-001): ").strip().upper()
                k_target = next(
                    (k for k in daftar_kunjungan if k.get_kode_kunjungan() == kode_ubah), None
                )
                if k_target:
                    print("Kunjungan saat ini:", k_target.info_kunjungan())
                    status_k = input("Status Baru (Menunggu/Sedang Ditangani/Selesai): ").strip()
                    k_target.ubah_status_kunjungan(status_k)
                    print("Status kunjungan diperbarui!")
                else:
                    print("Kode kunjungan tidak ditemukan.")

        # 5. CEK STATUS DATA
        elif pilihan == "5":
            print("\n--- CEK STATUS TENAGA MEDIS ---")
            for p in daftar_petugas:
                layak = "Siap Melayani" if p.bisa_melayani() else "Tidak Tersedia"
                print(f"[{p.get_id_pegawai()}] {p.get_nama()} -> {p.get_status_aktif()} ({layak})")

            print("\n--- CEK STATUS KUNJUNGAN PASIEN ---")
            if not daftar_kunjungan:
                print("Belum ada data kunjungan.")
            else:
                for k in daftar_kunjungan:
                    print(
                        f"[{k.get_kode_kunjungan()}] Pasien: {k.get_nama_pasien()} -> {k.get_status_kunjungan()}"
                    )

        # 6. KELUAR
        elif pilihan == "6":
            print("Terima kasih telah menggunakan Sistem Informasi Klinik!")
            break

        else:
            print("Pilihan tidak valid, silakan masukkan angka 1-6.")


if __name__ == "__main__":
    main()