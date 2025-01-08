from dicts.verbs import verbs
from dicts.verbsLevels import verbs_A1, verbs_A2, verbs_B1, verbs_B2, verbs_C1


def check():
    levels = ['A1', 'A2', 'B1', 'B2', 'C1']
    leveled_dicts = [verbs_A1, verbs_A2, verbs_B1, verbs_B2, verbs_C1]
    leveled_verbs = {**verbs_A1, **verbs_B1, **verbs_C1, **verbs_B2, **verbs_A2}
    count_words = {}
    count_level = {}
    count_translations = {}
    count_level_translations = {}

    print("\nКоличество глаголов в словарях:")
    for i in range(len(leveled_dicts)):
        print(f'{levels[i]}: {len(leveled_dicts[i])}')

    print("\nГлаголы, которых нету в словарях уровней:")
    for verb in verbs:
        if verb not in leveled_verbs:
            print(verb)

    for i, dictionary in enumerate(leveled_dicts):
        for word_eng in dictionary:
            if word_eng in count_words:
                count_words[word_eng] += 1
                count_level[word_eng] += f', {levels[i]}'
            else:
                count_words[word_eng] = 1
                count_level[word_eng] = levels[i]

    print("\nГлаголы, встречающиеся более одного раза в словарях уровней:")
    for verb, cnt in count_words.items():
        if cnt > 1:
            print(f'{verb}: {cnt} | {count_level[verb]}')

    for i, dictionary in enumerate(leveled_dicts):
        for word_eng, word_trans in dictionary.items():
            if word_trans in count_translations:
                count_translations[word_trans] += 1
                count_level_translations[word_trans].append(f'{levels[i]}: {word_eng}\n')
            else:
                count_translations[word_trans] = 1
                count_level_translations[word_trans] = [f'{levels[i]}: {word_eng}']

    result = ''
    print("\nПереводы, встречающиеся более одного раза в словарях уровней:")
    for value, cnt in count_translations.items():
        if cnt > 1:
            levels_eng_trans = ', '.join(count_level_translations[value])
            print(f'{value}: {cnt} | {levels_eng_trans}')
