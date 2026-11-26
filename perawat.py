from tenaga_medis import TenagaMedis


class Perawat(TenagaMedis):
    def __init__(
        self,
        id_pegawai: str,
        nama: str,
        shift: str,
        unit_kerja: str,
        level_perawat: str,
        pengalaman_tahun: int,
        status_aktif: str = "Aktif",
    ):
        super().__init__(id_pegawai, nama, shift, status_aktif)
        self.__unit_kerja = unit_kerja
        self.__level_perawat = level_perawat
        self.__pengalaman_tahun = pengalaman_tahun

    # Getter
    def get_unit_kerja(self) -> str:
        return self.__unit_kerja

    def get_level_perawat(self) -> str:
        return self.__level_perawat

    def get_pengalaman_tahun(self) -> int:
        return self.__pengalaman_tahun

    # Method tambahan 1: Evaluasi kategori pengalaman
    def kategori_pengalaman(self) -> str:
        if self.__pengalaman_tahun >= 5:
            return "Senior"
        elif self.__pengalaman_tahun >= 2:
            return "Menengah"
        return "Junior"

    # Method tambahan 2 (Override): Tampilkan detail perawat
    def info_tenaga_medis(self) -> str:
        return (
            f"{super().info_tenaga_medis()} | Peran: Perawat ({self.__unit_kerja}) "
            f"| Level: {self.__level_perawat} | Pengalaman: {self.__pengalaman_tahun} thn"
        )