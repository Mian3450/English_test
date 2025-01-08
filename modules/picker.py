import random

from modules.stats_creater import stats
from modules.scorer import save_scores
from modules.phrases import Phrase
from datetime import datetime
from modules.config.autosave_config import IS_AUTOSAVE
from modules.config.format_config import FORMAT_OPTION

phrase = Phrase()


def picker(dictionary):
    stop_iterations = ''
    memory = []
    start_time = datetime.now()

    while stop_iterations != '2':
        guessed_words = {}

        while len(dictionary) != len(guessed_words):
            english_word = random.choice(list(dictionary.keys()))

            while english_word in guessed_words:
                english_word = random.choice(list(dictionary.keys()))

            translate_word = dictionary[english_word]

            phrase.how_translate(translate_word)

            start_answer = datetime.now()
            answer = input('Ответ: ').strip().lower()
            finish_answer = datetime.now()

            time_for_answers = str(finish_answer - start_answer).split('.')[0]

            if answer == english_word:
                phrase.correct_answer(translate_word, english_word)
                guessed_words[english_word] = translate_word
                memory.append(f'{english_word} ✔️ \n {time_for_answers}')
            else:
                if answer == 'stop!':
                    phrase.stop_answer(english_word)

                    stop_iterations = '2'
                    break
                elif answer in dictionary:
                    memory.append(f'{english_word} ❌ | Ваш ответ: {answer} \n {time_for_answers}')
                    phrase.incorrect_answer_with_translation(answer, english_word, dictionary)
                else:
                    phrase.incorrect_answer_without_translation(answer, english_word)
                    memory.append(f'{english_word} ❌ | Ваш ответ: {answer if answer != '👑' else ''} \n {time_for_answers}')
        if stop_iterations == '2':
            break

        if len(dictionary) == len(guessed_words):
            phrase.one_more_time()

            stop_iterations = input('Ответ: ')

    if IS_AUTOSAVE:
        phrase.is_saved(FORMAT_OPTION)
        save_scores(memory, start_time)
    else:
        while True:
            phrase.save_scores()

            will_save = input('Выберите номер опции: ')

            if will_save == '1':
                save_scores(memory, start_time)
                stats()
                break
            elif will_save == '2':
                break
            else:
                phrase.option_not_identify(will_save)

    print('Пока!')
