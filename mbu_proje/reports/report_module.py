import json
import os

def generate_report(user, new_word):
    report_filename = "all_users_report.json"

    # Dosya varsa oku, yoksa boş veri oluştur
    if os.path.exists(report_filename):
        with open(report_filename, 'r') as file:
            report_data = json.load(file)
    else:
        report_data = []

    # Kullanıcı zaten kayıtlı mı kontrol et
    user_found = False
    for entry in report_data:
        if entry["username"] == user.username:
            user_found = True
            # Yeni kelime sözlük olarak ekleniyor
            if new_word and new_word not in entry["vocabulary"]:
                entry["vocabulary"].append(new_word)
            break

    # Eğer kullanıcı yoksa yeni kullanıcı olarak ekle
    if not user_found:
        new_entry = {
            "username": user.username,
            "vocabulary": [new_word] if new_word else []
        }
        report_data.append(new_entry)

    # Dosyayı tekrar yaz
    with open(report_filename, 'w') as file:
        json.dump(report_data, file, indent=4)

    print(f"Rapor güncellendi: {report_filename}")
