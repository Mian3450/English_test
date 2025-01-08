from dicts.verbsLevels import verbs_A1, verbs_A2, verbs_B1, verbs_B2, verbs_C1, verbs_test
from modules.phrases import Phrase

phrase = Phrase()


def selected_verbs():
    levels = [verbs_A1, verbs_A2, verbs_B1, verbs_B2, verbs_C1, verbs_test]

    while True:
        phrase.verbs_level()
        selected_level = int(input('Выберите номер опции: '))

        if selected_level <= len(levels):
            break
        else:
            phrase.option_not_identify(selected_level)

    while True:
        if selected_level == 1:
            words = {**levels[int(selected_level) - 1]}
            break

        phrase.verbs_selection()
        selected_type = input('Выберите номер опции: ')

        if selected_type == '1':
            words = {**levels[int(selected_level) - 1]}
            break
        elif selected_type == '2':
            words = {}
            for i in range(int(selected_level)):
                words.update(levels[i])
            break
        else:
            phrase.option_not_identify(selected_type)

    return words


def select_dict():
    while True:
        phrase.dictionary_select()
        selected_type = input('Выберите номер опции: ')

        if selected_type == '1':
            dictionary = selected_verbs()
            break
        else:
            phrase.option_not_identify(selected_type)

    return dictionary

