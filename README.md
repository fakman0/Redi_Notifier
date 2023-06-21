# Redi_Notifier

Gereksinimler
```
python3
praw
flask
keyboard
```

MacOS homebrew kurmak için<br>
```
curl -fsSL https://rawgit.com/kube/42homebrew/master/install.sh | zsh<br>
source $HOME/.brewconfig.zsh<br> 
```

brew aracılığıyla python ve pip kurmak için<br>

```
brew install python # python ve pip paketlerini kuracaktır.
```

PRAW (Python Reddit API Wrapper), keybroad, flaskkurulumu<br>

```
pip install praw keyboard flask
```

<br>
Ubuntu

```
apt update
apt install python3
apt install python3-pip
pip install praw flask keyboard
```

NOT: 
```
keyboard modülünün klavye erişiminin sağlanması için "root" yetkileriyle çalıştırınız.

Docker üzerinde main.py çalışabilmesi için girdi alınması amacıyla
docker run -itp 5000:5000 <img_id> # şeklinde çalıştırılmalıdır.

docker üzerinde main.py dock üzerinde çalıştırılacaksa bir aygıt olmadığından hata verecektir, keyboard fonksiyon ve threadleri yorum satırına alınmalıdır.

Api.py docker aracılığıyla çalıştırıldığında gönderilen isteklerden dönüt alınamazsa UFW veya docker network konfigürasyon ayarlarını kontrol ediniz.
```
