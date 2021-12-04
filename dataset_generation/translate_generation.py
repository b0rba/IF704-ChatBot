import csv
import re
from random import randrange
from typing import List

templates: List[str] = [
    "can you tell me how i would normally [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "can you tell me how i would [say](begin_translate) '[{phrase}](phrase)' [in](end_translate) [{lang}](lang)",
    "can you tell me how to [say](begin_translate) '[{phrase}](phrase)' [in](end_translate) [{lang}](lang)",
    "can you [translate](begin_translate) [{phrase}](phrase) [into](end_translate) [{lang}](lang) for me",
    "could you [translate](begin_translate) [{phrase}](phrase) [into](end_translate) [{lang}](lang)",
    "could you [translate](begin_translate) [{phrase}](phrase) [into](end_translate) [{lang}](lang) for me",
    "do you know how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how can i [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how could i [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how does one [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how do i [say](begin_translate) '[{phrase}](phrase)' [in](end_translate) [{lang}](lang)",
    "how do i [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how do i [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how do they [say](begin_translate) [{phrase}](phrase) [in](end_translate) brazil(lang)",
    "how do they [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how do they [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how do you [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how do you [say](begin_translate) [{phrase}](phrase) [in](end_translate) spanish(lang)",
    "how should i [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how would i [say](begin_translate) '[{phrase}](phrase)' [in](end_translate) [{lang}](lang)",
    "how would i [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how would one [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how would they [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how would you [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "i must know how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "i need to know how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "i need you to [translate](begin_translate) '[{phrase}](phrase)' [into](end_translate) [{lang}](lang)",
    "i would like to know how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "i would like to know the proper way to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "please tell me how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "please [translate](begin_translate) [{phrase}](phrase) [into](end_translate) [{lang}](lang) for me",
    "tell me how to [say](begin_translate) '[{phrase}](phrase)' [in](end_translate) [{lang}](lang)",
    "tell me how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "[translate](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "[translate](begin_translate) [{phrase}](phrase) [into](end_translate) [{lang}](lang) for me",
    "[translate](begin_translate) [{phrase}](phrase) [to](end_translate) [{lang}(lang)",
    "[translate](begin_translate) [{phrase}](phrase) [to](end_translate) [{lang}(lang)",
    "what do you [say](begin_translate) [{phrase}](phrase) if you [were](end_translate) [{lang}](lang)",
    "would you tell me how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
]

languages: List[str] = ["portuguese", "french", "italian", "spanish", "chinese", "hindi", "arabic", "bengali",
                        "russian", "japanese"]


def normalize_string(input_: str):
    pattern = re.compile(r'[^\w]')
    return pattern.sub('', input_.lower()[:-1])


def generate():
    final_phrases: List[str] = []
    csv_lines: List[str] = []
    with open('dataset_generation/sentences.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            csv_lines.append(row[0])

    break_point = 0
    max_iterations = 500
    for line in list(reversed(csv_lines)):
        if break_point >= max_iterations:
            break

        if randrange(10) == 0:
            break_point += 1
            for template in templates:
                for lang in languages:
                    sentence = template
                    sentence = sentence.replace('{phrase}', normalize_string(line)).replace('{lang}', lang).lower()
                    final_phrases.append(sentence)

    with open('dataset_generation/final_phrases.txt', 'w') as file:
        for phrase in final_phrases:
            file.write(f'- {phrase}\n')


if __name__ == '__main__':
    generate()
