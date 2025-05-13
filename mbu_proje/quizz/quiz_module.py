import random

class Quiz:
    def __init__(self):
        self.questions = []
    
    def create_quiz(self, question, options, correct_option):
        quiz_item = {"question": question, "options": options, "correct_option": correct_option}
        self.questions.append(quiz_item)

    def take_quiz(self):
        score = 0
        if not self.questions:  # Eğer soru yoksa
            print("Test için sorular oluşturulamadı.")
            return
        for q in self.questions:
            print(q["question"])
            for i, option in enumerate(q["options"], 1):
                print(f"{i}. {option}")
            try:
                answer = int(input("Cevap (1-4): "))
                if q["options"][answer - 1] == q["correct_option"]:
                    score += 1
            except ValueError:
                print("Geçersiz bir cevap girdiniz.")
        print(f"Test Sonucu: {score}/{len(self.questions)}")

    def create_custom_quiz(self, vocabulary):
        """Kullanıcı kelimeleriyle özel bir quiz oluşturur."""
        if not vocabulary:
            print("Kelime listesi boş.")
            return
        
        for word in vocabulary:
            turkish = word['turkish']
            english = word['english']

            # Türkçe -> İngilizce sorusu
            question = f"{turkish} kelimesinin İngilizcesi nedir?"
            options = [english, "apple", "computer", "cloud"]  # örnek yanlış seçenekler
            random.shuffle(options)  # Seçenekleri karıştırıyoruz
            correct_option = english
            self.create_quiz(question, options, correct_option)
            
            # İngilizce -> Türkçe sorusu
            question = f"{english} kelimesinin Türkçesi nedir?"
            options = [turkish, "kitap", "masa", "telefon"]  # örnek yanlış seçenekler
            random.shuffle(options)
            correct_option = turkish
            self.create_quiz(question, options, correct_option)


# start_quiz fonksiyonu burada dışarıda tanımlanmalıdır
def start_quiz(user):
    if not user.vocabulary:
        print("Uyarı: Henüz kelime yüklenmedi. Kelimeler yükleniyor...")
        from vocabulary.vocabulary_module import list_words
        list_words(user)

    quizz = Quiz()

    if not user.vocabulary:
        print("Kelimeler eklenmeden test başlatılamaz.")
        return

    quizz.create_custom_quiz(user.vocabulary)
    quizz.take_quiz()

