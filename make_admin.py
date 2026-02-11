from app import create_app, db
from app.models.user import User

app = create_app()


def make_user_admin():
    with app.app_context():
        print("--- ADMIN YAPMA SİHİRBAZI ---")
        username = input("Admin yapmak istediğin kullanıcı adını yaz: ")

        user = User.query.filter_by(username=username).first()

        if user:
            user.is_admin = True
            db.session.commit()
            print(f"✅ BAŞARILI! '{username}' kullanıcısı artık bir ADMIN.")
            print("⚠️  ÖNEMLİ: Şimdi Swagger'a gidip TEKRAR GİRİŞ YAPMALISIN.")
        else:
            print(f"❌ HATA: '{username}' adında bir kullanıcı bulunamadı.")


if __name__ == "__main__":
    make_user_admin()