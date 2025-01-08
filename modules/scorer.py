from datetime import datetime
from modules.config.format_config import FORMAT_OPTION


def save_scores(words_dict, start_time):
    finish_time = datetime.now()
    time = str(finish_time - start_time).split('.')[0]
    scores = sum(1 for mark in words_dict if "✔️" in mark)
    separeter_md = '</br>'
    separeter_txt = '\n'
    separeter = separeter_md if FORMAT_OPTION == 'md' else separeter_txt

    results = f'================================{separeter}'
    results += f'Дата попытки: {start_time.strftime("%Y-%m-%d %H:%M:%S")}{separeter}'
    results += f'Длительность попытки: {time}{separeter}'
    results += f'Ваш счёт: {scores}{separeter}'

    results += f'Вот история ответов:{separeter}'
    for word in words_dict:
        results += f'{word}{separeter}'

    results += f'================================{separeter}'

    with open(f'scores/scores.{FORMAT_OPTION}', 'a', encoding='utf-8') as file:
        file.write(f'{separeter}{separeter}{results}')
