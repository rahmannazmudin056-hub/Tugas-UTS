from tenaga_medis import TenagaMedis


class Dokter(TenagaMedis):
    def __init__(
        self,
        id_pegawai: str,
        nama: str,
        shift: str,
        spesialisasi: str,
        no_str: str,
        tarif_konsultasi: float,
        status_aktif: str = "Aktif",
):
        super().__init__(id_pegawai, nama, shift, status_aktif)
        self.__spesialisasi = spesialisasi
        self.__no_str = no_str
        self.__tarif_konsultasi = tarif_konsultasi

    # Getter
    def get_spesialisasi(self) -> str:
        return self.__spesialisasi

    def get_no_str(self) -> str:
        return self.__no_str

    def get_tarif_konsultasi(self) -> float:
        return self.__tarif_konsultasi

    # Setter
    def set_tarif_konsultasi(self, tarif_baru: float):
        if tarif_baru >= 0:
            self.__tarif_konsultasi = tarif_baru

    # Method tambahan 1: Hitung biaya layanan dengan administrasi klinik
    def hitung_biaya_layanan(self, biaya_admin: float = 15000.0) -> float:
        return self.__tarif_konsultasi + biaya_admin

    # Method tambahan 2 (Override): Tampilkan detail dokter
    def info_tenaga_medis(self) -> str:
        return (
            f"{super().info_tenaga_medis()} | Peran: Dokter ({self.__spesialisasi}) "
            f"| STR: {self.__no_str} | Tarif: Rp{self.__tarif_konsultasi:,.0f}"
        )