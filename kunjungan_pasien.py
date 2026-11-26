from tenaga_medis import TenagaMedis


class KunjunganPasien:
    def __init__(
        self,
        kode_kunjungan: str,
        nama_pasien: str,
        keluhan: str,
        petugas: TenagaMedis,
    ):
        self.__kode_kunjungan = kode_kunjungan
        self.__nama_pasien = nama_pasien
        self.__keluhan = keluhan
        self.__petugas = petugas  # Relasi Association dengan objek TenagaMedis
        self.__status_kunjungan = "Menunggu"

    # Getter
    def get_kode_kunjungan(self) -> str:
        return self.__kode_kunjungan

    def get_nama_pasien(self) -> str:
        return self.__nama_pasien

    def get_keluhan(self) -> str:
        return self.__keluhan

    def get_petugas(self) -> TenagaMedis:
        return self.__petugas

    def get_status_kunjungan(self) -> str:
        return self.__status_kunjungan

    # Method tambahan 1: Perbarui status kunjungan
    def ubah_status_kunjungan(self, status_baru: str):
        self.__status_kunjungan = status_baru

    # Method tambahan 2: Ringkasan data kunjungan
    def info_kunjungan(self) -> str:
        return (
            f"[{self.__kode_kunjungan}] Pasien: {self.__nama_pasien} | Keluhan: {self.__keluhan} "
            f"| Petugas: {self.__petugas.get_nama()} ({self.__petugas.get_id_pegawai()}) "
            f"| Status: {self.__status_kunjungan}"
        )