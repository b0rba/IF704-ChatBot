import csv
import re
from random import randrange
from typing import List

templates: List[str] = [
    "can you tell me how i would normally [say](begin_translate) [{phrase}](phrase) as [a](end_translate) [{lang}](lang) person",
    "can you tell me how i would [say](begin_translate) '[{phrase}](phrase)' [in](end_translate) [{lang}](lang)",
    "can you tell me how to [say](begin_translate) '[{phrase}](phrase)' [in](end_translate) [{lang}](lang)",
    "can you [translate](begin_translate) [{phrase}](phrase) [into](end_translate) [{lang}](lang) for me",
    "could you [translate](begin_translate) [{phrase}](phrase) [into](end_translate) [{lang}](lang)",
    "could you [translate](begin_translate) [{phrase}](phrase) [into](end_translate) [{lang}](lang) for me",
    "do you know how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    # "english [to](end_translate) [{lang}(lang) for [{phrase}](phrase)",
    "how can i [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how could i [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how does one [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how do i [say](begin_translate) '[{phrase}](phrase)' [in](end_translate) [{lang}](lang)",
    "how do i [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how do i [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    # "how do [{lang}](lang) people [say](begin_translate) [{phrase}](phrase)",
    # "how do [{lang}](lang) [say](begin_translate) [{phrase}](phrase)",
    "how do they [say](begin_translate) [{phrase}](phrase) [in](end_translate) brazil(lang)",
    "how do they [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how do they [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how do you [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how do you [say](begin_translate) [{phrase}](phrase) [in](end_translate) spanish(lang)",
    # "how is [{phrase}](phrase) said [in](end_translate) [{lang}](lang)",
    "how might i [say](begin_translate) [{phrase}](phrase) if i [were](end_translate) [{lang}](lang)",
    "how should i [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    # "how would i [say](begin_translate) if i [were](end_translate) [{lang}](lang) [{phrase}](phrase)",
    "how would i [say](begin_translate) [{phrase}](phrase) if i [were](end_translate) [{lang}](lang)",
    "how would i [say](begin_translate) '[{phrase}](phrase)' [in](end_translate) [{lang}](lang)",
    "how would i [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how would one [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how would they [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "how would you [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    # "if i [were](end_translate) [{lang}](lang) how would i [say](begin_translate) [{phrase}](phrase)",
    # "if i [were](end_translate) [{lang}](lang) how would i [say](begin_translate) that [{phrase}](phrase)",
    "i must know how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "i need to know how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "i need you to [translate](begin_translate) '[{phrase}](phrase)' [into](end_translate) [{lang}](lang)",
    # "in [{lang}](lang) how can I [say](begin_translate) [{phrase}](phrase)?",
    # "in [{lang}](lang) how do i [say](begin_translate) [{phrase}](phrase)",
    # "in [{lang}](lang) how do they [say](begin_translate) [{phrase}](phrase)",
    # "in [{lang}](lang) [{phrase}](phrase) is said how",
    "i want to know how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "i would i [say](begin_translate) [{phrase}](phrase) if i [were](end_translate) [{lang}](lang)",
    "i would like to know how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "i would like to know the proper way to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "please tell me how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "please [translate](begin_translate) [{phrase}](phrase) [into](end_translate) [{lang}](lang) for me",
    # "[{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    # "tell me how the [{lang}](lang) [say](begin_translate) [{phrase}](phrase)",
    "tell me how to [say](begin_translate) '[{phrase}](phrase)' [in](end_translate) [{lang}](lang)",
    "tell me how to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    # "translate english [to](end_translate) [{lang}(lang) [{phrase}](phrase)",
    # "translate for me [{phrase}](phrase) [into](end_translate) [{lang}](lang)",
    "[translate](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    "[translate](begin_translate) [{phrase}](phrase) [into](end_translate) [{lang}](lang) for me",
    "[translate](begin_translate) [{phrase}](phrase) [to](end_translate) [{lang}(lang)",
    "[translate](begin_translate) [{phrase}](phrase) [to](end_translate) [{lang}(lang)",
    "what do i [say](begin_translate) for [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    # "what do [{lang}](lang) people [say](begin_translate) for the word [{phrase}](phrase)",
    "what do you [say](begin_translate) [{phrase}](phrase) if you [were](end_translate) [{lang}](lang)",
    # "what expression would i use to [say](begin_translate) [{phrase}](phrase) if i were an [{lang}](lang)",
    # "what is [{lang}](lang) for [{phrase}](phrase)",
    # "what is [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    # "what is the correct way to [say](begin_translate) '[{phrase}](phrase)' [in](end_translate) [{lang}](lang)",
    # "what is the equivalent of '[{phrase}](phrase)' [in](end_translate) [{lang}](lang)",
    # "what is the right way to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    # "what is the way to [say](begin_translate) [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    # "what is the word for [{phrase}](phrase) [{lang}](lang)",
    # "what phrase means [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    # "what [{lang}](lang) word means [{phrase}](phrase)",
    # "what's local slang for [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    # "what's the [{lang}](lang) word for [{phrase}](phrase)",
    # "what's the [{lang}](lang) word you use for [{phrase}](phrase)",
    # "what's the word for [{phrase}](phrase) [in](end_translate) [{lang}](lang)",
    # "what words would i use to [{phrase}](phrase) if i [were](end_translate) [{lang}](lang)",
    # "what would the word for [{phrase}](phrase) be [in](end_translate) [{lang}](lang)",
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
    with open('dataset_generation/deutsche.csv') as csv_file:
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
    # xalala = 'Hello Word'
    # xalala = xalala.replace('H', 'CU')[:-1]
    # print(xalala)
