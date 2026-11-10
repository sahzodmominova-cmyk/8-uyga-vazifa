import requests

formatlar = [".mp3", ".mp4", ".pdf", ".png", ".jpg", ".jpeg", ".webp"]

url = input("Fayl havolasini kiriting: ")

fayl_nomi = url.split("/")[-1].split("?")[0]

if "." not in fayl_nomi:
    print("Xatolik: Fayl kengaytmasi topilmadi!")

else:
    kengaytma = "." + fayl_nomi.split(".")[-1].lower()

    if kengaytma not in formatlar:
        print("Xatolik: Bu fayl formati qo'llab-quvvatlanmaydi!")
        print("Ruxsat etilgan formatlar: mp3, mp4, pdf, png, jpg, jpeg, webp")

    else:
        print(f"Fayl turi: {kengaytma[1:].upper()}")

        try:
            print("Yuklab olinmoqda...")

            response = requests.get(url, timeout=30)
            response.raise_for_status()

            if response.content:
                with open("downloads/"+fayl_nomi, "wb") as fayl:
                    fayl.write(response.content)

                print("Fayl muvaffaqiyatli yuklandi!")
                print("Saqlangan fayl:", fayl_nomi)

            else:
                print("Faylni yuklab bo'lmadi!")

        except requests.exceptions.RequestException:
            print("Faylni yuklab bo'lmadi!")
            print("URL manzilni tekshiring.")
