class Phrase:
    @staticmethod
    def dictionary_select():
        print()
        print('================================')
        print('📚Выберете словарь📚')
        print('1.Verbs')
        print('================================')
        print()

    @staticmethod
    def verbs_level():
        print()
        print('================================')
        print('👷Выберете уровень глаголов👨‍🎓')
        print('1. A1 | 2. A2 | 3. B1 | 4. B2 | 5. C1 | 6. 🛠️test🛠️')
        print('================================')
        print()

    @staticmethod
    def verbs_selection():
        print()
        print('================================')
        print('⬆️Выберете тип подбора слов⬇️')
        print('1. Только слова уровня | 2. Слова уровня и уровней ниже')
        print('================================')
        print()

    @staticmethod
    def how_translate(translate_word):
        print()
        print('================================')
        print(f'🎓Как переводится "{translate_word}"?🎓')
        print('================================')
        print()

    @staticmethod
    def correct_answer(translate_word, english_word):
        print()
        print('================================')
        print('✔️Верно!✔️')
        print(f'"{translate_word}" переводиться как "{english_word}"')
        print('================================')
        print()


    @staticmethod
    def stop_answer(english_word):
        print()
        print('================================')
        print(f'Правильный ответ был {english_word}')
        print('================================')
        print()


    @staticmethod
    def incorrect_answer_with_translation(answer, english_word, dictionary):
        print()
        print('================================')
        print('❌Не верно!❌')
        print(f'Ваш ответ: "{answer}" переводиться как "{dictionary[answer]}"')
        print(f'Правильный ответ: "{english_word}"')
        print('================================')
        print()


    @staticmethod
    def incorrect_answer_without_translation(answer, english_word):
        print()
        print('================================')
        print('❌Не верно!❌')
        print(f'Ваш ответ: "{answer}"')
        print(f'Правильный ответ: "{english_word}"')
        print('================================')
        print()


    @staticmethod
    def one_more_time():
        print()
        print('================================')
        print('🎉Ты ответил на все вопросы правильно!🎉')
        print('♻️Ещё раз?♻️')
        print('1. ✔️Да | 2. ❌Нет')
        print('================================')
        print()

    @staticmethod
    def choose_program():
        print()
        print('================================')
        print('Выбери какую программу запустить')
        print('1. Перевод | 2. Cохранения | 3. 🛠️Отладка словаря🛠️')
        print('================================')
        print()

    @staticmethod
    def option_not_identify(option):
        print()
        print('================================')
        print(f'❌Опция "{option}" не найдена❌')
        print('Повторите запрос')
        print('================================')
        print()

    @staticmethod
    def save_scores():
        print()
        print('================================')
        print('Сохранить очки?')
        print('1. Да | 2.  Нет')
        print('================================')
        print()

    @staticmethod
    def format_of():
        print()
        print('================================')
        print(f'1. .md | 2. .txt')
        print('================================')
        print()

    @staticmethod
    def format_of_delete():
        print()
        print('================================')
        print(f'1. .md | 2. .txt | 3. Всё | 4. Отмена')
        print('================================')
        print()

    @staticmethod
    def saved_options(is_autosave):
        save = 'Вкл.' if is_autosave else 'Выкл.'

        print()
        print('================================')
        print(f'1. Прочитать сохранения | 2. Формат файла для сохранений | 3. Удаление сохранений | 4. Автосохранения: {save}')
        print('================================')
        print()

    @staticmethod
    def is_saved(format):
        print()
        print('================================')
        print(f'Данные автоматически сохранены в scores.{format}')
        print('================================')
        print()