import sys
import traceback

data_kedutaan = {
    "jepang" : {
        "nama" : "KBRI Tokyo",
        "alamat" : "Tokyo",
        "jam kerja" : "senin - jumat, 9:00 - 17:00"
    },

    "singapura" : {
        "nama" : "KBRI Singapura",
        "alamat" : "Singapura",
        "jam kerja" : "senin - jumat, 9:00 - 18:00"
    },

    "amerika" : {
        "nama" : "KBRI Washington DC",
        "alamat" : "DC",
        "jam kerja" : "senin - jumat, 9:00 - 18:00"
    }
}

def cari_kedutaan(negara):
    key = negara.lower()

    if key in data_kedutaan:
        data = data_kedutaan[key]
        print("{}".format(data["nama"].upper()))
        print("- alamat: {}".format(data["alamat"]))
        print("- jam kerja: {}".format(data["jam kerja"]))

    else:
        print("maaf, data belum tersedia")

def main():
    print("============ SISTEM INFORMASI KEDUTAAN RI ==================")

    try:
        user_input = input("masukkan nama negara: ").strip()
        if not user_input :
            print ("negara tidak boleh kosong")
        else:
            return cari_kedutaan(negara=user_input)


    except exception as e :
        # a/0
        print("error message: {}".format(e))
        traceback.print_exc()
        print("exit.")
        sys.exit()

if __name__ == "__main__":
    main()