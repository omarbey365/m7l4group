import sqlite3

DB_NAME = 'users.db'

def create_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

def add_user(username, email, password):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
            conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def authenticate_user(username, password):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        return cursor.fetchone() is not None

def display_users():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT username, email FROM users')
        for user in cursor.fetchall():
            print(f"Kullanıcı adı: {user[0]}, E-posta: {user[1]}")


def user_choice():
    print("\n1.  Giriş yap")
    print("2. Kayıt ol")
    choice = input("Lütfen seçiminizi girin (1/2): ")
    return choice

def main():
    create_db()
    display_users()  # Kullanıcı listesi, işlem seçmeden önce gösterilir
    choice = user_choice()

    if choice == '1':
        username = input("Kullanıcı adınızı girin: ")
        password = input("Şifrenizi girin: ")
        if authenticate_user(username, password):
            print("Doğrulama başarılı.")
        else:
            print("Kullanıcı adı veya şifre hatalı.")
    elif choice == '2':
        username = input("Yeni kullanıcı için kullanıcı adı girin: ")
        email = input("Yeni kullanıcı için e-posta adresi girin: ")
        password = input("Yeni kullanıcı için şifre girin: ")
        add_user(username, email, password)
    else:
        print("Geçersiz giriş. Lütfen giriş yapmak için 1, kayıt olmak için 2 girin.")

if __name__ == "__main__":
    main()
