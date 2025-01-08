from modules.config.format_config import FORMAT_OPTION


def stats():
    directory = 'scores/scores.'

    separeter_md = '</br>'
    separeter_txt = '\n'
    separeter = separeter_md if FORMAT_OPTION == 'md' else separeter_txt
    index = 0

    scores = {}
    scores_count = []

    results = f'🏆================================🏆{separeter}'

    with open(f'{directory}{FORMAT_OPTION}', 'r', encoding='utf-8') as file:
        saved = file.read()

    saved_list = saved.split(separeter)
    passed = sum(1 for mark in saved.split(' ') if "✔️" in mark)
    failed = sum(1 for mark in saved.split(' ') if "❌" in mark)

    for i, word in enumerate(saved_list):
        if '👑' in word:
            index = i
        if 'Ваш счёт:' in word:
            score = int(word.split(' ')[2])
            scores_count.append(score)

    if scores_count:
        scores['max'] = max(scores_count)
        scores['avg'] = round(sum(scores_count) / len(scores_count))
        scores['min'] = min(scores_count)
        scores['percent'] = str(round(((passed / (failed + passed)) * 100), 1)) + '%'
    else:
        scores['max'] = 0
        scores['avg'] = 0.0
        scores['min'] = 0
        scores['percent'] = '0'

    del saved_list[0:index + 1]

    results += f'Максимальное количество очков: {scores['max']}{separeter}'
    results += f'Среднее количество очков: {scores['avg']}{separeter}'
    results += f'Минимальное количество очков: {scores['min']}{separeter}'
    results += f'Количество попыток: {len(scores_count)}{separeter}'
    results += f'Процент правильных: {scores['percent']}{separeter}'

    results += f'🏆================================🏆👑{separeter}'

    with open(f'{directory}{FORMAT_OPTION}', 'w', encoding='utf-8') as file:
        file.write(f'{results + separeter.join(saved_list)}')
