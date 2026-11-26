class TenagaMedis:
    def __init__(self, id_pegawai: str, nama: str, shift: str, status_aktif: str = "Aktif"):
        self.__id_pegawai = id_pegawai
        self.__nama = nama
        self.__shift = shift
        self.__status_aktif = status_aktif

    # Getter
    def get_id_pegawai(self) -> str:
        return self.__id_pegawai

    def get_nama(self) -> str:
        return self.__nama

    def get_shift(self) -> str:
        return self.__shift

    def get_status_aktif(self) -> str:
        return self.__status_aktif

    # Setter untuk ubah data
    def set_shift(self, shift_baru: str):
        self.__shift = shift_baru

    def set_status_aktif(self, status_baru: str):
        self.__status_aktif = status_baru

    # Method tambahan 1: Cek ketersediaan bertugas
    def bisa_melayani(self) -> bool:
        return self.__status_aktif.lower() == "aktif"

    # Method tambahan 2: Ringkasan info tenaga medis
    def info_tenaga_medis(self) -> str:
        return (
            f"[{self.__id_pegawai}] {self.__nama} | Shift: {self.__shift} "
            f"| Status: {self.__status_aktif}"
        )

    