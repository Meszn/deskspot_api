# 🎬 Use Cases - Kullanım Senaryoları

Bu doküman, kullanıcıların sistemle etkileşim senaryolarını detaylandırır.

---

## UC-01: Yeni Rezervasyon Oluşturma

**Aktör:** Standart Kullanıcı (User)  
**Ön Koşul:** Kullanıcı giriş yapmış ve geçerli bir JWT Token almıştır.

### Temel Akış (Main Flow)
1.  Kullanıcı, `POST /api/bookings` adresine masa ID'si ve tarih aralığı gönderir.
2.  Sistem, kullanıcının Token'ını doğrular.
3.  Sistem, belirtilen tarihlerde masanın boş olup olmadığını kontrol eder.
4.  Sistem, rezervasyonu veritabanına kaydeder.
5.  Sistem, kullanıcıya `201 Created` ve rezervasyon detaylarını döner.

### Alternatif Akışlar (Alternative Flows)
* **3a. Masa Doluysa:**
    * Sistem, `409 Conflict` hatası döner. Mesaj: "Seçilen saatlerde masa dolu."
* **2a. Token Geçersizse:**
    * Sistem, `401 Unauthorized` hatası döner.

---

## UC-02: Masa Ekleme (Yönetici)

**Aktör:** Yönetici (Admin)  
**Ön Koşul:** Kullanıcı `is_admin=True` yetkisine sahiptir.

### Temel Akış
1.  Admin, `POST /api/desks` adresine masa ismi ve konumu gönderir.
2.  Sistem, admin yetkisini kontrol eder.
3.  Sistem, masayı oluşturur ve `201 Created` döner.

### Hata Durumu
* **1a. Aynı İsimde Masa Varsa:**
    * Sistem `400 Bad Request` döner. Mesaj: "Bu isimde bir masa zaten var."
