import random
import time
import os

# Check whether the mp3 file exists
required_files = [
    "storage/downloads/intro.mp3",
    "storage/downloads/roll.mp3",
    "storage/downloads/winner.mp3",
    "storage/downloads/lose.mp3"
]

for file in required_files:
    if not os.path.exists(file):
        print(f"Music file not found: {file}\nPlease download and place it in the appropriate folder.")
        exit()

semboller = ["🫐", "🍎", "🍏", "🦄", "🍋"]

def temizle():
    os.system("cls" if os.name == "nt" else "clear")

def play_sound(path):
    os.system(f"mpv --no-video --quiet '{path}' &")

skor = 0
maksimum_tur = 5
tur = 0

# Start intro.mp3
play_sound("storage/downloads/intro.mp3")
time.sleep(3)  # Give a little pause
input("Şans Slot Makinesi'ne hoş geldin! Başlamak için ENTER'a bas...")

while tur < maksimum_tur:
    temizle()
    print(f"Şans Slot Makinesi - Tur: {tur + 1}/{maksimum_tur} | Skor: {skor} (Maksimum: 30 | 2 eşleşme: +5, 3 eşleşme: +10)")
    input("Döndürmek için ENTER'a bas...")

    # Start roll.mp3
    play_sound("storage/downloads/roll.mp3")

    # Loop animation slot during ±12 second
    durasi_roll = 12
    jumlah_loop = 40
    delay_per_loop = durasi_roll / jumlah_loop

    for _ in range(jumlah_loop):
        a, b, c = random.choices(semboller, k=3)
        temizle()
        print(f"| {a} | {b} | {c} |")
        time.sleep(delay_per_loop)

    print("\nSonuç geldi!")

    if a == b == c:
        play_sound("storage/downloads/winner.mp3")
        print("🏆 JACKPOT! Harikasın!")
        skor += 10
        time.sleep(5)
    elif a == b or b == c or a == c:
        play_sound("storage/downloads/winner.mp3")
        print("Güzel! İki eşleşme var.")
        skor += 5
        time.sleep(5)
    else:
        play_sound("storage/downloads/lose.mp3")
        print("Şansını tekrar dene.")
        time.sleep(5)

    tur += 1

temizle()
print(f"Oyun bitti! Toplam skorun: {skor}")
