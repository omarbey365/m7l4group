# Kullanıcı Yönetim Sistemi

Python ile gerçekleştirilmiş basit bir kullanıcı yönetim sistemi. Bu sistem, kullanıcı verilerini depolamak için SQLite kullanır. Program, yeni kullanıcı ekleme, mevcut kullanıcıları doğrulama ve kayıtlı tüm kullanıcıların listesini görüntüleme işlevlerini sunar.

## Özellikler

- **Yeni kullanıcı ekleme**: Uygulama, yeni kullanıcıların giriş bilgilerini veri tabanına kaydeder.
- **Kullanıcı doğrulama**: Uygulama, kullanıcı kimlik bilgilerini doğruladıktan sonra giriş yapmalarına izin verir.
- **Kullanıcı listesini görüntüleme**: Uygulama, tüm kullanıcıların (şifreler hariç) verileriyle birlikte listesini gösterir.

## Programı Çalıştırma

Bu programı kullanabilmek için bilgisayarınızda Python 3.6 veya daha üst bir sürümünün ve SQLite eklentisinin kurulu olması gerekir.

### Kurulum

1. Depoyu bilgisayarınıza klonlayın:
    ```bash
    git clone depo_yolu
    ```
2. Proje dizinine gidin:
    ```bash
    cd User_Management_System_DB
    ```

### Kullanım

Programı çalıştırmak için terminalde aşağıdaki komutu yazın:
```bash
python registration.py
```
Kullanıcıları yönetmek için ekranda gösterilen talimatları izleyin.

### Test Etme

Program, pytest kütüphanesi kullanılarak yazılmış birim testlerini içerir. Testleri çalıştırmak için pytest kurulu olmalıdır (gerekirse pip ile yükleyin):
```bash
pip install pytest
```

Testleri projenin kök dizininden şu komutla çalıştırabilirsiniz:
```bash
pytest
```
## Yazar

Kodland
