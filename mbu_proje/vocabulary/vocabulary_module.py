import json
from reports.report_module import generate_report

def add_new_word(user):
    turkish_word = input("Türkçe kelimeyi girin: ").strip()
    english_word = input("İngilizce anlamını girin: ").strip()

    if not turkish_word or not english_word:
        print("Uyarı: Her iki alan da boş bırakılamaz.")
        return

    new_word = {"turkish": turkish_word, "english": english_word}

    user.vocabulary.append(new_word)
    print(f"{turkish_word} - {english_word} kelimesi başarıyla eklendi.")

    generate_report(user, new_word)

def list_words(user):
    report_filename = "all_users_report.json"

    try:
        with open(report_filename, 'r') as file:
            report_data = json.load(file)

        for entry in report_data:
            if entry["username"] == user.username:
                print(f"\n{user.username} kullanıcısının kelimeleri:")
                for word in entry["vocabulary"]:
                    print(f'{word["turkish"]}: {word["english"]}')

                user.vocabulary = entry["vocabulary"]
                return

        print(f"{user.username} adlı kullanıcı bulunamadı.")

    except FileNotFoundError:
        print("Rapor dosyası (all_users_report.json) bulunamadı.")

def remove_word(user):
    word_to_delete = input("Silmek istediğiniz Türkçe kelimeyi girin: ").strip()
    report_filename = "all_users_report.json"

    try:
        with open(report_filename, 'r') as file:
            report_data = json.load(file)

        for entry in report_data:
            if entry["username"] == user.username:
                original_length = len(entry["vocabulary"])
                entry["vocabulary"] = [
                    w for w in entry["vocabulary"] if w["turkish"] != word_to_delete
                ]
                if len(entry["vocabulary"]) < original_length:
                    print(f"{word_to_delete} kelimesi başarıyla silindi.")
                else:
                    print(f"{word_to_delete} kelimesi bulunamadı.")
                break

        with open(report_filename, 'w') as file:
            json.dump(report_data, file, indent=4)

        user.vocabulary = [w for w in user.vocabulary if w["turkish"] != word_to_delete]

    except FileNotFoundError:
        print("Rapor dosyası bulunamadı.")


