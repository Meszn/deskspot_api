# 📈 BRS - İş Gereksinimleri Spesifikasyonu

**Proje Adı:** DeskSpot API - Ortak Çalışma Alanı Yönetim Sistemi  
**Doküman Sürümü:** 1.0.0  
**Tarih:** Şubat 2026  
**Durum:** Onaylandı

---

## 1. Yönetici Özeti
Ortak çalışma alanlarının (Coworking Spaces) popülaritesinin artmasıyla birlikte, masa ve kaynak yönetiminin manuel yöntemlerle yapılması sürdürülemez hale gelmiştir. **DeskSpot API**, bu süreci dijitalleştirerek yöneticilerin kaynakları verimli yönetmesini ve kullanıcıların 7/24 rezervasyon yapabilmesini sağlayan merkezi bir backend çözümüdür.

## 2. Proje Kapsamı (Scope)
* **Dahil Olanlar (In-Scope):** Kullanıcı Kayıt/Giriş, Rol Tabanlı Yetkilendirme (Admin/User), Masa Envanter Yönetimi, Rezervasyon Oluşturma.
* **Dahil Olmayanlar (Out-of-Scope):** Ödeme Sistemi Entegrasyonu, Mobil Arayüz Tasarımı.

## 3. İş Gereksinimleri Listesi (Business Requirements)

| ID | Gereksinim Tanımı | Başlatan | Öncelik |
| :--- | :--- | :--- | :--- |
| **BR-01** | Potansiyel üye, sisteme e-posta ile kayıt olabilmelidir. | Kullanıcı | Yüksek |
| **BR-02** | Yönetici, ofise yeni masalar ekleyebilmeli ve konumunu girebilmelidir. | Admin | Yüksek |
| **BR-03** | Kullanıcılar, müsait masaları tarih aralığına göre listeleyebilmelidir. | Kullanıcı | Yüksek |
| **BR-04** | Sistem, aynı masanın aynı saatte başkasına verilmesini engellemelidir. | Sistem | Kritik |
| **BR-05** | Yönetici, sistemdeki tüm rezervasyon geçmişini görebilmelidir. | Admin | Orta |

## 4. İş Akış Diyagramı

```mermaid
graph TD
    User((Kullanıcı)) -->|Kayıt/Giriş| System[DeskSpot API]
    System -->|Token Verir| User
    User -->|Masa Arar| System
    System -->|Müsaitlik Kontrolü| DB[(Veritabanı)]
    DB -->|Sonuç| System
    System -->|Rezervasyon Onayı| User
