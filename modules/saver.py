from modules.from_md_to_txt import to_txt
from modules.phrases import Phrase
from modules.config.autosave_config import IS_AUTOSAVE

phrase = Phrase()


def is_autosave(is_autosave_enable):
    if is_autosave_enable:
        with open(f'modules/config/autosave_config.py', 'w', encoding='utf-8') as file:
            file.write(f'IS_AUTOSAVE = False')
    else:
        with open(f'modules/config/autosave_config.py', 'w', encoding='utf-8') as file:
            file.write(f'IS_AUTOSAVE = True')


def save_config():
    phrase.saved_options(IS_AUTOSAVE)

    variant = input('Выберите номер опции: ')

    if variant == '1':
        phrase.format_of()

        read_option = input('Выберите номер опции: ')
        format_of = ''
        file_path = 'scores/scores.'

        if read_option == '1':
            format_of = 'md'
        elif read_option == '2':
            format_of = 'txt'

        file_path += format_of

        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            print(to_txt(file_contents))

    elif variant == '2':
        phrase.format_of()

        format_option = input('Выберите номер опции: ')
        if format_option == '1':
            with open(f'modules/format_config.py', 'w', encoding='utf-8') as file:
                file.write(f'FORMAT_OPTION = "md"')
        elif format_option == '2':
            with open(f'modules/format_config.py', 'w', encoding='utf-8') as file:
                file.write(f'FORMAT_OPTION = "txt"')
    elif variant == '3':
        phrase.format_of_delete()

        delete_option = input('Выберите номер опции: ')

        if delete_option == '1':
            with open(f'scores/scores.md', 'w', encoding='utf-8') as file:
                file.write(f'')
        elif delete_option == '2':
            with open(f'scores/scores.txt', 'w', encoding='utf-8') as file:
                file.write(f'')
        elif delete_option == '3':
            with open(f'scores/scores.txt', 'w', encoding='utf-8') as file:
                file.write(f'')
            with open(f'scores/scores.md', 'w', encoding='utf-8') as file:
                file.write(f'')
        elif delete_option == '4':
            return
    elif variant == '4':
        is_autosave(IS_AUTOSAVE)
