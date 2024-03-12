def hitung_ips(jumlah_matkul):
    total_sks = 0
    total_bobot = 0

    for i in range(jumlah_matkul):
        nilai_huruf = input("Masukkan nilai MK {} : ".format(i+1))
        sks = 3
        if nilai_huruf == 'A':
            bobot = 4
        elif nilai_huruf == 'B':
            bobot = 3
        elif nilai_huruf == 'C':
            bobot = 2
        elif nilai_huruf == 'D':
            bobot = 1
        else:
            print("Format anda salah silahkan gunakan huruf dan harus kapital")
            return

        total_sks = total_sks + sks
        total_bobot = total_bobot + sks * bobot

    ips = total_bobot / total_sks
    return ips

jumlah_matkul = int(input("Berapa jumlah mata kuliah: "))
hasil_ips = hitung_ips(jumlah_matkul)

print("Nilai IPS anda semester ini :", round(hasil_ips,2))