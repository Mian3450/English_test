from modules.picker import picker
from modules.selecter import select_dict
from modules.cheker import check
from modules.phrases import Phrase
from modules.saver import save_config

phrase = Phrase()


while True:
    phrase.choose_program()
    programMode = input('Выберите номер опции: ')

    if programMode == '1':
        picker(select_dict())
        break
    elif programMode == '2':
        save_config()
        break
    elif programMode == '3':
        check()
        break
    else:
        phrase.option_not_identify(programMode)
