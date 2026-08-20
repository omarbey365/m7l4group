# Kullanıcı Yönetim Sistemi

Bu proje, **Python** ve **SQLite** kullanılarak geliştirilmiş basit bir kullanıcı yönetim sistemidir. Projenin temel amacı kullanıcıların sisteme kaydedilmesi, kayıtlı kullanıcıların doğrulanması ve kullanıcı bilgilerinin bir SQLite veri tabanında saklanmasıdır.

Proje ayrıca **pytest** kullanılarak hazırlanmış birim testleri içerir. Bu testler sayesinde kullanıcı yönetim sistemindeki temel fonksiyonların beklendiği şekilde çalışıp çalışmadığı otomatik olarak kontrol edilebilir.

---

## Özellikler

Program aşağıdaki temel işlevleri sunar:

- **Yeni kullanıcı ekleme:** Kullanıcı adı, e-posta adresi ve şifre veri tabanına kaydedilir.
- **Aynı kullanıcı adını engelleme:** Daha önce kayıtlı olan bir kullanıcı adıyla ikinci kez kayıt oluşturulmasına izin verilmez.
- **Kullanıcı doğrulama:** Kullanıcı adı ve şifre veri tabanındaki bilgilerle karşılaştırılır.
- **Hatalı giriş kontrolü:** Yanlış kullanıcı adı veya şifreyle giriş yapılması engellenir.
- **Kullanıcı listesini görüntüleme:** Kayıtlı kullanıcıların kullanıcı adları ve e-posta adresleri görüntülenir.
- **Şifre gizliliği:** Kullanıcı listesi görüntülenirken şifreler ekrana yazdırılmaz.
- **SQLite veri tabanı:** Kullanıcı bilgileri `users.db` isimli SQLite veri tabanında saklanır.
- **Otomatik testler:** Programın temel fonksiyonları `pytest` ile test edilebilir.
- **HTML test raporu:** Test sonuçları tarayıcıda görüntülenebilecek bir HTML raporuna dönüştürülebilir.
- **Test kapsamı (coverage):** Kodun hangi bölümlerinin testler tarafından çalıştırıldığı ölçülebilir.

---

# Kullanılan Teknolojiler

Projede temel olarak aşağıdaki teknolojiler kullanılmaktadır:

| Teknoloji | Kullanım amacı |
|---|---|
| Python | Programın geliştirilmesi |
| SQLite | Kullanıcı bilgilerinin saklanması |
| pytest | Birim testlerinin çalıştırılması |
| pytest-html | Test sonuçlarının HTML raporuna dönüştürülmesi |
| pytest-cov | Test kapsamının ölçülmesi |
| coverage.py | Kod kapsamı raporlarının oluşturulması |

SQLite, Python ile birlikte gelen `sqlite3` modülü üzerinden kullanılmaktadır. Bu nedenle normal şartlarda SQLite için ayrıca bir Python paketi yüklemek gerekmez.

---

# Proje Yapısı

Proje genel olarak aşağıdaki yapıya sahiptir:

```text
proje-klasoru/
│
├── registration/
│   ├── __init__.py
│   └── registration.py
│
├── tests/
│   ├── __init__.py
│   └── test_registration.py
│
├── pytest.ini
├── users.db
└── README.md
```

Dosyaların görevleri:

### `registration/registration.py`

Programın temel fonksiyonlarının bulunduğu dosyadır.

Burada;

- veri tabanı oluşturulur,
- kullanıcı eklenir,
- kullanıcı doğrulanır,
- kullanıcılar görüntülenir,
- kullanıcıdan giriş veya kayıt seçimi alınır.

### `tests/test_registration.py`

Programın doğru çalışıp çalışmadığını kontrol eden otomatik testlerin bulunduğu dosyadır.

### `users.db`

SQLite veri tabanı dosyasıdır. Kayıtlı kullanıcı bilgileri burada tutulur.

### `pytest.ini`

`pytest` çalıştırılırken kullanılacak bazı proje ayarlarını içerebilir.

---

# Gereksinimler

Programı çalıştırabilmek için bilgisayarınızda **Python 3** bulunmalıdır.

Python'ın kurulu olup olmadığını kontrol etmek için Windows PowerShell veya Komut İstemi'ni açarak şu komutu yazabilirsiniz:

```bash
python --version
```

Örneğin:

```text
Python 3.11.1
```

gibi bir sonuç görüyorsanız Python bilgisayarınızda kuruludur.

---

# Kurulum

## 1. Projeyi bilgisayara indirin

GitHub üzerinden klonlanacaksa:

```bash
git clone depo_yolu
```

Ardından proje klasörüne girin:

```bash
cd proje-klasoru
```

Projeyi ZIP olarak indirdiyseniz ZIP dosyasını çıkartıp terminali çıkartılan proje klasöründe açmanız yeterlidir.

---

## 2. Gerekli test paketlerini yükleyin

Temel testleri çalıştırmak için:

```bash
pip install pytest
```

HTML test raporu oluşturmak için:

```bash
pip install pytest-html
```

Test kapsamını ölçmek için:

```bash
pip install pytest-cov
```

Hepsini tek komutla da yükleyebilirsiniz:

```bash
pip install pytest pytest-html pytest-cov
```

---

# Programın Çalıştırılması

Programı çalıştırmak için terminali proje klasöründe açın.

Proje yapısına bağlı olarak ana program şu şekilde çalıştırılabilir:

```bash
python registration/registration.py
```

Program açıldığında kullanıcıya temel olarak iki seçenek sunulur:

```text
1. Giriş yap
2. Kayıt ol
```

Kullanıcı yapmak istediği işlemin numarasını girer.

---

# Kayıt Olma

Kullanıcı:

```text
2
```

seçeneğini seçtiğinde program sırasıyla;

1. kullanıcı adı,
2. e-posta adresi,
3. şifre

bilgilerini ister.

Bu bilgiler SQLite veri tabanındaki `users` tablosuna kaydedilir.

Tablonun temel yapısı şöyledir:

```text
users
├── username
├── email
└── password
```

`username` alanı birincil anahtar (`PRIMARY KEY`) olarak tanımlandığı için aynı kullanıcı adıyla birden fazla kullanıcı oluşturulamaz.

---

# Giriş Yapma

Kullanıcı:

```text
1
```

seçeneğini seçtiğinde kullanıcı adı ve şifre istenir.

Girilen bilgiler veri tabanındaki kayıtlarla eşleşirse:

```text
Doğrulama başarılı.
```

mesajı görüntülenir.

Bilgiler eşleşmezse:

```text
Kullanıcı adı veya şifre hatalı.
```

mesajı görüntülenir.

---

# Kullanıcıların Görüntülenmesi

Program kayıtlı kullanıcıları görüntüleyebilir.

Örneğin:

```text
Kullanıcı adı: user1, E-posta: user1@example.com
Kullanıcı adı: user2, E-posta: user2@example.com
```

Kullanıcıların şifreleri bu listede gösterilmez.

---

# Birim Test Nedir?

**Birim testi (unit test)**, programdaki küçük ve bağımsız işlevlerin beklenen sonucu üretip üretmediğini otomatik olarak kontrol eden testtir.

Örneğin programda:

```python
add_user(...)
```

isimli bir fonksiyon olduğunu düşünelim.

Bu fonksiyonun görevi yeni kullanıcı eklemektir. Programı her değiştirdiğimizde elle kullanıcı oluşturup veri tabanını kontrol etmek yerine bir test yazabiliriz.

Test otomatik olarak:

1. kullanıcı ekler,
2. veri tabanını kontrol eder,
3. kullanıcının gerçekten eklenip eklenmediğini belirler,
4. sonuç beklenen gibi değilse testi başarısız olarak işaretler.

Bu yöntem özellikle proje büyüdükçe önem kazanır.

---

# Neden Birim Test Kullanıyoruz?

Bir programın çalışıyor görünmesi, bütün fonksiyonlarının doğru çalıştığı anlamına gelmez.

Örneğin yeni kullanıcı ekleme çalışırken;

- aynı kullanıcıyı ikinci kez ekleme,
- yanlış şifreyle giriş,
- bulunmayan kullanıcıyla giriş,
- kullanıcı listesini görüntüleme

gibi durumlarda hata oluşabilir.

Birim testleri bu senaryoların her birini ayrı ayrı kontrol eder.

---

# Bu Projede Kullanılan Testler

Projede toplam **7 temel test** bulunmaktadır.

## 1. Veri tabanı oluşturma testi

```text
test_create_db
```

Bu test, program çalıştırıldığında SQLite veri tabanının ve `users` tablosunun oluşturulup oluşturulmadığını kontrol eder.

Beklenen sonuç:

```text
users tablosu mevcut olmalıdır.
```

---

## 2. Yeni kullanıcı ekleme testi

```text
test_add_new_user
```

Bu test yeni bir kullanıcı oluşturur ve ardından veri tabanını sorgular.

Amaç, eklenen kullanıcının gerçekten veri tabanına kaydedildiğini doğrulamaktır.

Örneğin:

```text
Kullanıcı adı: testuser
E-posta: testuser@example.com
Şifre: password123
```

bilgileriyle kullanıcı oluşturulduktan sonra `users` tablosunda `testuser` aranır.

---

## 3. Aynı kullanıcı adını tekrar ekleme testi

```text
test_add_existing_user
```

Önce bir kullanıcı oluşturulur.

Ardından aynı kullanıcı adıyla ikinci bir kayıt yapılmaya çalışılır.

Örneğin:

```text
İlk kayıt:
user1 / user1@example.com

İkinci kayıt:
user1 / different@example.com
```

Kullanıcı adları aynı olduğu için ikinci işlemin başarısız olması beklenir.

Test şu davranışı doğrular:

```python
assert result is False
```

---

## 4. Başarılı kullanıcı doğrulama testi

```text
test_successful_authentication
```

Önce bir kullanıcı oluşturulur.

Daha sonra aynı kullanıcı adı ve doğru şifreyle giriş yapılmaya çalışılır.

Bilgiler doğruysa:

```python
authenticate_user(...)
```

fonksiyonunun `True` döndürmesi beklenir.

---

## 5. Var olmayan kullanıcı testi

```text
test_authentication_nonexistent_user
```

Bu test veri tabanında bulunmayan bir kullanıcı adıyla giriş yapmaya çalışır.

Örneğin:

```text
Kullanıcı adı: olmayan_kullanici
Şifre: password1
```

Böyle bir kullanıcı olmadığı için doğrulamanın başarısız olması gerekir.

Beklenen sonuç:

```python
False
```

---

## 6. Yanlış şifre testi

```text
test_authentication_wrong_password
```

Bu testte kullanıcı veri tabanında bulunmaktadır fakat giriş sırasında yanlış şifre kullanılır.

Örneğin gerçek şifre:

```text
password1
```

iken:

```text
yanlis_sifre
```

ile giriş yapılmaya çalışılır.

Doğrulamanın başarısız olması beklenir.

---

## 7. Kullanıcı listesini görüntüleme testi

```text
test_display_users
```

Bu test kullanıcıların ekrana doğru biçimde yazdırılıp yazdırılmadığını kontrol eder.

Örneğin:

```text
Kullanıcı adı: user4, E-posta: user4@example.com
Kullanıcı adı: user5, E-posta: user5@example.com
```

ifadelerinin program çıktısında bulunması beklenir.

`pytest` tarafından sağlanan `capsys` özelliği kullanılarak programın terminale yazdırdığı metin yakalanabilir ve beklenen sonuçla karşılaştırılabilir.

---

# Testleri Çalıştırma

Terminali proje klasöründe açın ve:

```bash
pytest
```

komutunu çalıştırın.

`pytest`, `tests` klasöründeki testleri otomatik olarak bulur ve çalıştırır.

Testlerin tamamı başarılıysa buna benzer bir sonuç görülür:

```text
collected 7 items

test_create_db PASSED
test_add_new_user PASSED
test_add_existing_user PASSED
test_successful_authentication PASSED
test_authentication_nonexistent_user PASSED
test_authentication_wrong_password PASSED
test_display_users PASSED

7 passed
```

Buradaki:

```text
PASSED
```

testin başarıyla tamamlandığını ifade eder.

---

# PASSED, FAILED ve ERROR Ne Anlama Gelir?

### PASSED

```text
PASSED
```

Test çalıştırılmış ve beklenen sonuç elde edilmiştir.

### FAILED

```text
FAILED
```

Test çalışmıştır fakat elde edilen sonuç beklenen sonuçla uyuşmamıştır.

Örneğin test:

```python
assert result is False
```

beklerken fonksiyon `True` döndürmüş olabilir.

Bu durumda programın davranışı ile testte tanımlanan beklenen davranış uyuşmamaktadır.

### ERROR

```text
ERROR
```

Test normal şekilde tamamlanamamıştır.

Örneğin:

- modül bulunamaması,
- fixture bulunamaması,
- veri tabanı bağlantı problemi,
- Python hatası

gibi durumlarda görülebilir.

`FAILED` ile `ERROR` bu nedenle aynı şey değildir.

---

# Fixture Nedir?

Bu projede `pytest` fixture'ları da kullanılmaktadır.

Örneğin:

```python
@pytest.fixture(scope="module")
def setup_database():
```

fixture'ı testlerden önce gerekli veri tabanı ortamını hazırlar.

Bunun avantajı aynı hazırlık kodunu her testin içerisinde tekrar tekrar yazmak zorunda kalmamaktır.

Bir başka fixture:

```python
@pytest.fixture
def connection():
```

test sırasında SQLite veri tabanına bağlantı oluşturur ve test tamamlandıktan sonra bağlantıyı kapatır.

---

# Assertion Nedir?

Testlerde sık sık:

```python
assert
```

ifadesi görülür.

`assert`, testin beklediği koşulu belirtir.

Örneğin:

```python
assert result is True
```

şu anlama gelir:

> `result` değerinin `True` olmasını bekliyorum.

Eğer gerçekten `True` ise test geçer.

Değer `False` ise test başarısız olur.

Başka bir örnek:

```python
assert user
```

Bu ifade kullanıcı sorgusundan geçerli bir sonuç dönmesini bekler.

---

# HTML Test Raporu Oluşturma

Terminal çıktısı yerine test sonuçlarını tarayıcıda daha düzenli görüntülemek için HTML raporu oluşturulabilir.

Önce gerekli paket yüklenir:

```bash
pip install pytest-html
```

Ardından:

```bash
pytest --html=test_raporu.html --self-contained-html
```

komutu çalıştırılır.

Testler tamamlandıktan sonra proje klasöründe:

```text
test_raporu.html
```

dosyası oluşur.

Bu dosyaya çift tıklayarak Google Chrome, Microsoft Edge veya başka bir internet tarayıcısıyla açabilirsiniz.

HTML raporunda testlerin;

- isimleri,
- başarılı veya başarısız olma durumları,
- çalışma süreleri,
- hata bilgileri

görüntülenebilir.

---

# Test Coverage Nedir?

Birim testlerinin başarılı olması önemli olmakla birlikte başka bir soru daha vardır:

> Testler program kodunun ne kadarını gerçekten çalıştırıyor?

Bu sorunun cevabı **code coverage**, yani **kod kapsamı** ile ölçülür.

Örneğin:

```text
100%
```

coverage değeri, ölçüme dahil edilen çalıştırılabilir kod satırlarının test sırasında kapsandığını gösterir.

Ancak önemli bir ayrım vardır:

**%100 coverage, programda kesinlikle hata bulunmadığı anlamına gelmez.**

Coverage temel olarak hangi kod bölümlerinin test sırasında çalıştırıldığını gösterir. Testlerin doğru senaryoları ve doğru sonuçları kontrol edip etmediği ayrıca değerlendirilmelidir.

Bu nedenle iyi bir test sistemi hem yüksek kapsamı hem de anlamlı test senaryolarını hedeflemelidir.

---

# Coverage Raporu Oluşturma

Gerekli paket:

```bash
pip install pytest-cov
```

Daha sonra testleri coverage ile çalıştırabilirsiniz:

```bash
pytest --cov=registration
```

Terminalde kapsam yüzdesi görüntülenir.

---

# HTML Coverage Raporu

Coverage sonuçlarını HTML biçiminde görmek için:

```bash
pytest --cov=registration --cov-report=html
```

komutunu kullanabilirsiniz.

Bu işlem sonunda:

```text
htmlcov/
```

klasörü oluşturulur.

Klasörün içerisindeki:

```text
htmlcov/index.html
```

dosyasını tarayıcıda açarak ayrıntılı coverage raporunu inceleyebilirsiniz.

Burada hangi satırların testler tarafından çalıştırıldığı ve hangi satırların test kapsamı dışında kaldığı görülebilir.

---

# Test ve Coverage Raporunu Birlikte Oluşturma

Hem test sonuçlarını hem de coverage sonuçlarını oluşturmak için:

```bash
pytest --cov=registration --cov-report=html --html=test_raporu.html --self-contained-html
```

komutu kullanılabilir.

Bu işlem sonucunda iki farklı rapor elde edilir:

```text
test_raporu.html
htmlcov/index.html
```

Bunların görevleri farklıdır.

### `test_raporu.html`

Testlerin geçip geçmediğini gösterir.

Örneğin:

```text
7 Passed
0 Failed
```

### `htmlcov/index.html`

Program kodunun testler tarafından ne ölçüde kapsandığını gösterir.

Dolayısıyla:

**Test raporu = Testler başarılı mı?**

**Coverage raporu = Testler kodun ne kadarını çalıştırdı?**

sorularına cevap verir.

---

# Testlerin Önemi

Bu projedeki testler sayesinde programda daha sonra bir değişiklik yapıldığında mevcut özelliklerin bozulup bozulmadığı hızlı biçimde kontrol edilebilir.

Örneğin `add_user()` fonksiyonunda değişiklik yapıldıktan sonra:

```bash
pytest
```

çalıştırılarak kullanıcı ekleme veya mevcut kullanıcı kontrolünün bozulup bozulmadığı görülebilir.

Bu yaklaşım yazılım geliştirmede **regression testing** açısından da önemlidir. Daha önce çalışan bir özelliğin yapılan yeni bir değişiklik nedeniyle bozulması testler sayesinde daha kolay fark edilir.

---

# Önemli Güvenlik Notu

Bu proje eğitim amacıyla hazırlanmış basit bir kullanıcı yönetim sistemi olduğundan şifreler mevcut uygulamada doğrudan veri tabanında saklanmaktadır.

Gerçek bir kullanıcı yönetim sisteminde şifrelerin bu şekilde saklanması **güvenli değildir**.

Gerçek uygulamalarda şifreler uygun bir parola hash mekanizması kullanılarak saklanmalıdır. Ayrıca giriş doğrulaması, veri doğrulama, hata yönetimi ve veri tabanı güvenliği gibi ek önlemler uygulanmalıdır.

Bu nedenle proje mevcut haliyle gerçek kullanıcı bilgilerinin saklanacağı üretim ortamlarında kullanılmamalıdır.

---

# Özet

Bu proje ile temel olarak aşağıdaki konular uygulanmaktadır:

- Python fonksiyonları
- SQLite veri tabanı kullanımı
- SQL sorguları
- Kullanıcı kaydı
- Kullanıcı doğrulama
- Veri tabanından veri okuma
- `pytest` ile birim testi
- Fixture kullanımı
- Assertion kullanımı
- Hatalı durumların test edilmesi
- HTML test raporu oluşturma
- Test coverage ölçümü
- HTML coverage raporu oluşturma

---

# Yazar

**Ömer** Türk Malı 
