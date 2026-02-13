# 🏢 DeskSpot API - Ortak Çalışma Alanı Rezervasyon Sistemi

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=for-the-badge&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)
![Swagger](https://img.shields.io/badge/Swagger-UI-85EA2D?style=for-the-badge&logo=swagger)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**DeskSpot API**, ortak çalışma alanları (coworking spaces) için geliştirilmiş, ölçeklenebilir ve güvenli bir RESTful backend servisidir. Bu proje, modern backend geliştirme prensiplerini, katmanlı mimariyi ve endüstri standardı araçları (Docker, JWT, Swagger) bir araya getirerek gerçek hayat senaryolarına uygun bir çözüm sunar.

---

## Projenin Amacı ve Özellikleri

Bu sistem, kullanıcıların belirli tarihler için çalışma masası rezerve etmesini sağlarken, yöneticilerin (Admin) ofis kaynaklarını yönetmesine olanak tanır.

* **🔐 Güvenli Kimlik Doğrulama (JWT):** Kullanıcı güvenliği için JSON Web Token tabanlı stateless (durumsuz) oturum yönetimi.
* **👤 Rol Tabanlı Erişim Kontrolü (RBAC):** Admin ve Standart Kullanıcı ayrımı. Sadece Admin yetkisine sahip kullanıcılar masa ekleyebilir/düzenleyebilir.
* **🗄️ İlişkisel Veri Modeli (ORM):** SQLAlchemy kullanılarak Kullanıcılar, Masalar ve Rezervasyonlar arasında kurulan güçlü veritabanı ilişkileri.
* **📝 Canlı Dokümantasyon (Swagger UI):** Frontend geliştiricileri için API uç noktalarını tarayıcı üzerinden test etme imkanı.
* **✅ Veri Doğrulama (Validation):** Marshmallow şemaları ile gelen ve giden verilerin tutarlılığının ve doğruluğunun sağlanması.
* **🏗️ Modüler Mimari:** Flask Blueprints ve Application Factory tasarım kalıpları kullanılarak, geliştirilebilir ve bakımı kolay kod yapısı.
* **🐳 Docker Desteği:** Uygulamanın her ortamda aynı şekilde çalışmasını sağlayan konteyner yapısı.

---

## 🛠️ Kullanılan Teknolojiler

| Kategori | Teknoloji | Açıklama |
| :--- | :--- | :--- |
| **Dil** | Python 3.10+ | Ana programlama dili |
| **Framework** | Flask | Web sunucusu ve API yönetimi |
| **Veritabanı** | SQLite / SQLAlchemy | Geliştirme ortamı veritabanı ve ORM |
| **Auth** | Flask-JWT-Extended | Token tabanlı güvenlik |
| **Serialization** | Marshmallow | JSON veri dönüşümü ve doğrulama |
| **Docs** | Flasgger | OpenAPI (Swagger) entegrasyonu |
| **DevOps** | Docker | Konteynerizasyon ve dağıtım |

---

## 📂 Proje Mimarisi

Proje, "Separation of Concerns" (İlgi Alanlarının Ayrımı) prensibine uygun olarak klasörlenmiştir.

```text
deskspot_api/
├── app/
│   ├── models/       # Veritabanı Modelleri (User, Desk, Booking)
│   ├── routes/       # API Endpoint'leri (Controller katmanı)
│   ├── schemas/      # Veri doğrulama ve serileştirme şemaları
│   ├── __init__.py   # Application Factory (Uygulama Fabrikası)
│   ├── config.py     # Ortam yapılandırmaları (Dev/Prod)
│   └── extensions.py # 3. parti eklentiler (DB, JWT, Swagger)
├── migrations/       # Veritabanı versiyon takibi
├── .env              # Gizli ortam değişkenleri
├── Dockerfile        # Docker imaj dosyası
├── requirements.txt  # Proje bağımlılıkları
└── run.py            # Uygulamayı başlatan giriş noktası
```

## http://127.0.0.1:5000/apidocs/ adresinden uygulamaya ulaşabilirsiniz.
