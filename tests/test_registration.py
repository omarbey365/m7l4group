import pytest
import sqlite3
import os
from registration.registration import create_db, add_user, authenticate_user, display_users


@pytest.fixture(scope="module")
def setup_database():
    """Testlerden önce veri tabanını oluşturmak ve testlerden sonra temizlemek için kullanılan test düzeneği."""
    create_db()
    yield
    try:
        os.remove('users.db')
    except PermissionError:
        pass


@pytest.fixture
def connection():
    """Test sırasında veri tabanı bağlantısı oluşturur ve testten sonra bağlantıyı kapatır."""
    conn = sqlite3.connect('users.db')
    yield conn
    conn.close()


def test_create_db(setup_database, connection):
    """Veri tabanı ve 'users' tablosunun oluşturulmasını test eder."""
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    table_exists = cursor.fetchone()
    assert table_exists, "'users' tablosu veri tabanında bulunmalıdır."


def test_add_new_user(setup_database, connection):
    """Yeni bir kullanıcının eklenmesini test eder."""
    add_user('testuser', 'testuser@example.com', 'password123')

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username='testuser';")
    user = cursor.fetchone()

    assert user, "Kullanıcı veri tabanına eklenmiş olmalıdır."


def test_add_existing_user(setup_database):
    """Var olan bir kullanıcı adıyla tekrar kullanıcı eklenemediğini test eder."""
    add_user(
        "user1",
        "user1@example.com",
        "password1"
    )

    result = add_user(
        "user1",
        "different@example.com",
        "password2"
    )

    assert result is False


def test_successful_authentication(setup_database):
    """Doğru kullanıcı adı ve şifreyle başarılı doğrulamayı test eder."""
    add_user(
        "user2",
        "user2@example.com",
        "password1"
    )

    result = authenticate_user(
        "user2",
        "password1"
    )

    assert result is True


def test_authentication_nonexistent_user(setup_database):
    """Var olmayan bir kullanıcıyla doğrulamanın başarısız olduğunu test eder."""
    result = authenticate_user(
        "olmayan_kullanici",
        "password1"
    )

    assert result is False


def test_authentication_wrong_password(setup_database):
    """Yanlış şifreyle doğrulamanın başarısız olduğunu test eder."""
    add_user(
        "user3",
        "user3@example.com",
        "password1"
    )

    result = authenticate_user(
        "user3",
        "yanlis_sifre"
    )

    assert result is False


def test_display_users(setup_database, capsys):
    """Kullanıcı listesinin doğru şekilde görüntülendiğini test eder."""
    add_user(
        "user4",
        "user4@example.com",
        "password4"
    )

    add_user(
        "user5",
        "user5@example.com",
        "password5"
    )

    display_users()

    captured = capsys.readouterr()

    assert "Kullanıcı adı: user4, E-posta: user4@example.com" in captured.out
    assert "Kullanıcı adı: user5, E-posta: user5@example.com" in captured.out

# İşte yazabileceğiniz bazı testler:
"""
Var olan bir kullanıcı adıyla kullanıcı eklemeye çalışmayı test etme.
Başarılı kullanıcı doğrulamasını test etme.
Var olmayan bir kullanıcıyla doğrulama yapmayı test etme.
Yanlış şifreyle doğrulama yapmayı test etme.
Kullanıcı listesinin doğru şekilde görüntülenmesini test etme.
"""