import json
import os

class User:
    def __init__(self, username, password, email="", vocabulary=None):
        self.username = username
        self.password = password
        self.email = email
        self.vocabulary = vocabulary if vocabulary is not None else []

    def login(self):
        if self.username and self.password:
            print(f"kullanıcı {self.username} girişi başarılı!")
        else:
            print("Giriş hatalı. Kullanıcı adı ve şifreyi kontrol ediniz.")

    def save_data(self):
        all_data = {}

        if os.path.exists("all_users_report.json"):
            with open("all_users_report.json", "r", encoding="utf-8") as f:
                try:
                    all_data = json.load(f)
                except json.JSONDecodeError:
                    all_data = {}

        all_data[self.username] = {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "vocabulary": self.vocabulary
        }

        with open("all_users_report.json", "w", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, indent=4)

    def load_data(self):
        filename = "all_users_report.json"
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                all_data = json.load(f)
                user_data = all_data.get(self.username)
                if user_data:
                    self.password = user_data.get("password", self.password)
                    self.email = user_data.get("email", self.email)
                    self.vocabulary = user_data.get("vocabulary", [])
        else:
            print("Kayıtlı kullanıcı verisi bulunamadı.")
