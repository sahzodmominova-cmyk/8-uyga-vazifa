import requests
from urllib.parse import urlparse, unquote

formatlar = [".mp3", ".mp4", ".pdf", ".png", ".jpg", ".jpeg", ".webp"]

url = input("Fayl havolasini kiriting: ")

fayl_nomi = unquote(urlparse(url).path.split("/")[-1])

kengaytma = "." + fayl_nomi.split(".")[-1].lower()

if kengaytma not in formatlar:
    print("Xatolik: Bu fayl formati qollab-quvvatlanmaydi!")
    print("Ruxsat etilgan formatlar: mp3, mp4, pdf, png, jpg, jpeg, webp")

else:
    print(f"Fayl turi: {kengaytma[1:].upper()}")

    try:
        print("Yuklab olinmoqda...")

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        if response.content:
            with open("downloads/" + fayl_nomi, "wb") as fayl:
                fayl.write(response.content)

            print("Fayl muvaffaqiyatli yuklandi!")
            print("Saqlangan fayl: downloads/" + fayl_nomi)

        else:
            print("Faylni yuklab bolmadi!")

    except requests.exceptions.RequestException:
        print("Faylni yuklab bolmadi!")
        print("URL manzilni tekshiring yoki fayl mavjud emas.")
