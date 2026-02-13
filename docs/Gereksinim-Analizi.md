# 📘 Yazılım Mühendisliğinde Gereksinim Analizi ve Yönetimi Rehberi

![Software Engineering](https://img.shields.io/badge/Discipline-Software%20Engineering-blue)
![Level](https://img.shields.io/badge/Level-Beginner%20%7C%20Intermediate-green)
![Standard](https://img.shields.io/badge/Standard-IEEE%20830-orange)

Bu doküman, yazılım projelerinin başarısındaki en kritik faktör olan **Gereksinim Analizi** sürecini, teorik temelleri ve pratik uygulama yöntemleriyle ele almak için hazırlanmıştır. 

> **Yazar Notu:** "Kod yazmak, inşaatın tuğlalarını örmektir. Gereksinim analizi ise binanın mimari planını çizmektir. Plansız bir gökdelen inşa edemezsiniz."

---

## 📑 İçindekiler

1. [Gereksinim Analizi Nedir?](#1-gereksinim-analizi-nedir)
2. [Neden Önemlidir? (Maliyet ve Risk)](#2-neden-önemlidir)
3. [Gereksinim Türleri](#3-gereksinim-türleri)
4. [Gereksinim Toplama Teknikleri](#4-gereksinim-toplama-teknikleri)
5. [SRS (Yazılım Gereksinim Spesifikasyonu)](#5-srs-nedir)
6. [Metodolojiler: Agile vs Waterfall](#6-agile-ve-waterfall-farkı)
7. [Doğrulama ve Geçerleme (V&V)](#7-doğrulama-ve-geçerleme)
8. [Örnek Vaka: Kampüs Yemekhane Sistemi](#8-örnek-vaka-kampüs-yemekhane-sistemi)

---

## 1. Gereksinim Analizi Nedir?

Gereksinim analizi (Requirement Analysis); bir yazılım projesinde paydaşların (müşteri, kullanıcı, yönetici vb.) ihtiyaçlarını belirleme, bu ihtiyaçları teknik bir dille ifade etme, çelişkileri giderme ve belgeleme sürecidir.

Basitçe; **"Ne yapacağız?"** sorusuna, **"Nasıl yapacağız?"** aşamasına geçmeden önce verilen net cevaptır.

### Temel Süreç Adımları
1.  **Elicitation (Çıkarım):** İhtiyaçların ham haliyle toplanması.
2.  **Analysis (Analiz):** İhtiyaçların sınıflandırılması ve tutarsızlıkların giderilmesi.
3.  **Specification (Belgeleme):** Standartlara uygun (SRS) dokümantasyon.
4.  **Validation (Doğrulama):** Paydaş onayı.

---

## 2. Neden Önemlidir?

Boehm'in maliyet eğrisine göre; gereksinim aşamasında tespit edilen bir hatayı düzeltmenin maliyeti **1 birim** ise, bu hata ürün canlıya alındıktan (maintenance) sonra düzeltilirse maliyeti **100 birim** olabilir.

**Kötü Gereksinim Analizinin Sonuçları:**
* **Kapsam Kayması (Scope Creep):** Projenin sürekli genişlemesi ve bitmemesi.
* **Bütçe Aşımı:** Gereksiz özellikler için harcanan efor.
* **Tatmin Olmayan Müşteri:** "Ben bunu istememiştim" cümlesi.

---

## 3. Gereksinim Türleri

Yazılım gereksinimleri hiyerarşik bir yapıda ele alınır.

### A. Seviyesine Göre
| Tür | Açıklama | Örnek |
| :--- | :--- | :--- |
| **İş Gereksinimleri (Business Req.)** | Kurumun ulaşmak istediği üst seviye hedeftir. | "Yemekhane kuyruklarını %30 azaltmak." |
| **Kullanıcı Gereksinimleri (User Req.)** | Kullanıcının sistemle ne yapmak istediğidir. | "Öğrenci olarak, bakiye yüklemek istiyorum." |
| **Sistem Gereksinimleri (System Req.)** | Sistemin ne yapması gerektiğinin teknik tanımıdır. | "Sistem, QR kod üretip veritabanına kaydetmelidir." |

### B. İşlevselliğine Göre (En Kritik Ayrım)

#### 1. Fonksiyonel Gereksinimler (Functional Requirements - FR)
Sistemin **ne yapması** gerektiğini belirtir. Girdi, davranış ve çıktı ile ilgilidir.
* "Sistem, kullanıcıya şifre sıfırlama e-postası göndermelidir."
* "Sepetteki ürünlerin toplam fiyatı otomatik hesaplanmalıdır."

#### 2. Fonksiyonel Olmayan Gereksinimler (Non-Functional Requirements - NFR)
Sistemin **nasıl çalışması** gerektiğini (kalite niteliklerini) belirtir.
* **Performans:** "Sayfa yüklenme süresi 2 saniyenin altında olmalıdır."
* **Güvenlik:** "Tüm veriler 256-bit SSL ile şifrelenmelidir."
* **Kullanılabilirlik:** "Arayüz renkleri renk körü kullanıcılar için uygun olmalıdır."
* **Ölçeklenebilirlik:** "Sistem aynı anda 10.000 kullanıcıyı desteklemelidir."

---

## 4. Gereksinim Toplama Teknikleri

Doğru bilgiye ulaşmak için tek bir yöntem yetmez. Duruma göre aşağıdaki teknikler harmanlanmalıdır:

* **Mülakatlar (Interviews):** Paydaşlarla birebir görüşmeler. (Derinlemesine bilgi sağlar).
* **Anketler (Surveys):** Çok sayıda kullanıcıdan veri toplamak için kullanılır.
* **Beyin Fırtınası (Brainstorming):** Yeni fikirler üretmek için grup çalışması.
* **Prototipleme (Prototyping):** Kullanıcıya çalışan basit bir taslak gösterip geri bildirim alma. (En etkili yöntemlerden biridir).
* **Doküman Analizi:** Mevcut sistemin raporlarını ve eski prosedürleri inceleme.
* **Gözlem (Observation):** Kullanıcıyı işini yaparken izleme ("Sözlü olmayan" ihtiyaçları görmek için).

---

## 5. SRS (Yazılım Gereksinim Spesifikasyonu) Nedir?

SRS (*Software Requirements Specification*), geliştirilecek yazılımın anayasasıdır. Genellikle **IEEE 830** standardı referans alınır.

**İyi bir SRS'in özellikleri:**
1.  **Doğru (Correct):** İsteneni tam yansıtmalı.
2.  **Açık (Unambiguous):** "Hızlı", "Güzel", "Kullanışlı" gibi yoruma açık kelimeler içermemeli. (Örn: "Hızlı" yerine "500ms altında" denmeli).
3.  **Tam (Complete):** Hiçbir senaryo eksik bırakılmamalı.
4.  **Test Edilebilir (Verifiable):** Her gereksinimin bir test senaryosu yazılabilmeli.

---

## 6. Agile ve Waterfall Farkı

Gereksinim süreci, kullanılan proje yönetim metodolojisine göre değişir.

### 🌊 Waterfall (Şelale) Modeli
* Gereksinimler projenin **en başında** detaylıca toplanır ve dondurulur.
* SRS dokümanı imzalanır ve değişiklik yapmak zordur (Change Request süreci gerekir).
* **Risk:** Müşteri ürünü en sonda görür, gereksinim hatası varsa proje çöp olabilir.

### 🏃 Agile (Çevik) Modeli (Scrum/Kanban)
* Gereksinimler **User Story (Kullanıcı Hikayesi)** formatında tutulur.
* Gereksinimler "Product Backlog"ta yaşar ve sürekli değişebilir/gelişebilir.
* Detaylar, geliştirme sprint'i başlamadan hemen önce netleştirilir.
* **Format:** `As a <rol>, I want to <işlev>, so that <fayda>.`

---

## 7. Doğrulama ve Geçerleme

Bu iki kavram sıkça karıştırılır ancak farklıdır:

* **Doğrulama (Verification):** "Ürünü doğru mu inşa ediyoruz?" (Are we building the product right?). SRS'e uygun mu? Kod standartlara uyuyor mu?
* **Geçerleme (Validation):** "Doğru ürünü mü inşa ediyoruz?" (Are we building the right product?). Müşterinin ihtiyacını gerçekten karşılıyor mu?

---

## 8. Örnek Vaka: Kampüs Yemekhane Sistemi

**Senaryo:** Üniversite kampüsünde yemekhane kuyruklarını azaltmak için bir QR kodlu rezervasyon ve ödeme sistemi geliştirilecektir.

### 📌 Fonksiyonel Gereksinimler (SRS Formatı)

| ID | Tanım | Öncelik |
| :--- | :--- | :--- |
| **FR-01** | Sistem, öğrencilerin üniversite e-posta adresleri (@edu.tr) ile kayıt olmasına izin vermelidir. | Yüksek |
| **FR-02** | Kullanıcılar, haftalık yemek menüsünü görüntüleyebilmelidir. | Orta |
| **FR-03** | Kullanıcı, bakiye yüklemek için kredi kartı bilgilerini girebilmelidir. | Yüksek |
| **FR-04** | Sistem, ödeme başarılı olduğunda 24 saat geçerli bir QR kod üretmelidir. | Yüksek |
| **FR-05** | Turnike sistemi, okutulan QR kodun daha önce kullanılıp kullanılmadığını kontrol etmelidir. | Kritik |

### 📌 Fonksiyonel Olmayan Gereksinimler (NFR)

* **NFR-Performance:** QR kod üretim süresi 1 saniyenin altında olmalıdır.
* **NFR-Reliability:** Sistem, öğle yemeği saatlerinde (12:00-13:30) %99.99 erişilebilir olmalıdır.
* **NFR-Security:** Kullanıcı şifreleri veritabanında SHA-256 algoritması ile hashlenerek saklanmalıdır.

### 📌 Agile User Story Örneği

```text
Title: Bakiye Yükleme

As a (Olarak): Öğrenci
I want to (İstiyorum ki): Hesabıma kredi kartımla anında para yükleyebileyim
So that (Böylece): Yemekhaneye gittiğimde nakit para ile uğraşmadan hızlıca geçebileyim.

Acceptance Criteria (Kabul Kriterleri):
- Sanal POS entegrasyonu çalışmalı.
- Minimum yükleme tutarı 20 TL olmalı.
- İşlem sonunda dijital dekont e-posta atılmalı.
