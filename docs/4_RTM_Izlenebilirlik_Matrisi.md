# 📊 RTM - Requirement Traceability Matrix

Bu matris, İş Gereksinimlerinin (BRS), Teknik Gereksinimlere (SRS) ve Test Kodlarına (Test Cases) dönüşümünü takip eder. Projenin eksiksiz olduğunu kanıtlar.

| İş Gereksinimi (BRS) | Yazılım Gereksinimi (SRS) | İlgili Dosya/Modül | Test Durumu (Test Case) | Durum |
| :--- | :--- | :--- | :--- | :--- |
| **BR-01** (Üye Kaydı) | FR-AUTH-01 | `routes/auth.py` | `test_register_user` | ✅ Tamamlandı |
| **BR-02** (Masa Ekleme) | FR-DESK-01 | `routes/desk.py` | `test_create_desk_admin` | ✅ Tamamlandı |
| **BR-02** (Masa Ekleme) | FR-DESK-02 | `models/desk.py` | `test_duplicate_desk` | ✅ Tamamlandı |
| **BR-03** (Masa Listeleme)| FR-DESK-03 | `routes/desk.py` | `test_get_desks` | ✅ Tamamlandı |
| **BR-04** (Çakışma Kontrol)| FR-BOOK-01 | `routes/booking.py` | `test_booking_conflict` | ⏳ Geliştiriliyor |
| **BR-05** (Raporlama) | FR-BOOK-04 | `routes/admin.py` | `test_get_all_bookings` | ⏳ Planlandı |

---
**Durum Açıklaması:**
* ✅ Tamamlandı: Kod yazıldı ve test edildi.
* ⏳ Geliştiriliyor: Kodlama aşamasında.
* ⏳ Planlandı: Sonraki sprintte yapılacak.
