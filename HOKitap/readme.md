#HOKitap Nedir?
*For english go down*

HOKitap, * sesli kitap platformuna toplu kitap yükleme işlemini kolaylaştıran bir scripttir.

"Kitap Adı - Yazar İsmi" formundaki klasörlerde, ses parçaları olarak bulunan kitapları, sistemin tanıyacağı şekilde belirli bir başlangıç değerine sahip ID'leri itere ederek isimlendirir. Platformun diğer kanallardan da erişilebilirliği için dosyaların .wav formatına dönüştürülmesini de sağlayarak, kitap isimlerini, ID'leri ve ses dosyası sayılarını bir dosyada tutar.

Kullanımı;

```
ho_kitap(AnaKlasor, baslama_degeri)
```

AnaKlasor: (string) kitap klasörlerini içeren ana klasörün yolu

baslama_degeri: (integer) klasörleri id'lemek için verilen başlangış değeri

##Nasıl Çalışır
1. İsim değiştirme işmeleri için ```os``` üzerinden ```mv```komutunu kullanır.
1. dosya formatı değişimi için ```ffmpeg``` üzerinden *pcm_u8* codec'ini ve _10.000 bit rate_'ini kullanır.


#What is HOKitap?
HOKitap, is a script to help upload batch audio books to * audio book platform.

Script renames, audio files and files' folders of books, which is in the form of "Book Name - Writer Name" by iterating ID's which has a known initial value will be supported by the system.

It, provide a mp3-wav convert process to allow accesses from another channels. And after renaming, script keep the id's and part numbers of books in a text file.

Usage;

```
ho_kitap(MainFolder, initial_value)
```

MainFolder: (string) The path of the folder which is parent of book folders

initial_value: (integer) initial value to rename the folder as id and beginning of iteration

##HOw it work?
1. Uses ```mv``` over ```os``` for rename tasks
1. Uses *pcm_u8* codec and _10.000 bit rate_ over ```ffmpeg``` for converting files