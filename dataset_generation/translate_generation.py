import csv
import re
from random import randrange
from typing import List

templates: List[str] = [
    "can you tell me how i would normally say [{phrase}](phrase) as a [{lang}](lang) person",
    "can you tell me how i would say '[{phrase}](phrase)' in [{lang}](lang)",
    "can you tell me how to say '[{phrase}](phrase)' in [{lang}](lang)",
    "can you translate [{phrase}](phrase) into [{lang}](lang) for me",
    "could you translate [{phrase}](phrase) into [{lang}](lang)",
    "could you translate [{phrase}](phrase) into [{lang}](lang) for me",
    "do you know how to say [{phrase}](phrase) in [{lang}](lang)",
    "english to [{lang}](lang) for [{phrase}](phrase)",
    "how can i say [{phrase}](phrase) in [{lang}](lang)",
    "how can i [{phrase}](phrase) in [{lang}](lang)",
    "how could i say [{phrase}](phrase) in [{lang}](lang)",
    "how does one say [{phrase}](phrase) in [{lang}](lang)",
    "how do i say '[{phrase}](phrase)' in [{lang}](lang)",
    "how do i say [{phrase}](phrase) in [{lang}](lang)",
    "how do i say [{phrase}](phrase) in [{lang}](lang)",
    "how do i [{phrase}](phrase) in [{lang}](lang)",
    "how do [{lang}](lang) people say [{phrase}](phrase)",
    "how do [{lang}](lang) say [{phrase}](phrase)",
    "how do they say [{phrase}](phrase) in brazil(lang)",
    "how do they say [{phrase}](phrase) in [{lang}](lang)",
    "how do they say [{phrase}](phrase) in [{lang}](lang)",
    "how do you say [{phrase}](phrase) in [{lang}](lang)",
    "how do you say [{phrase}](phrase) in spanish(lang)",
    "how is [{phrase}](phrase) said in [{lang}](lang)",
    "how might i say [{phrase}](phrase) if i were [{lang}](lang)",
    "how should i say [{phrase}](phrase) in [{lang}](lang)",
    "how would i say if i were [{lang}](lang) [{phrase}](phrase)",
    "how would i say [{phrase}](phrase) if i were [{lang}](lang)",
    "how would i say '[{phrase}](phrase)' in [{lang}](lang)",
    "how would i say [{phrase}](phrase) in [{lang}](lang)",
    "how would one say [{phrase}](phrase) in [{lang}](lang)",
    "how would they say say [{phrase}](phrase) in [{lang}](lang)",
    "how would they say [{phrase}](phrase) in [{lang}](lang)",
    "how would you say [{phrase}](phrase) in [{lang}](lang)",
    "if i were [{lang}](lang) how would i say [{phrase}](phrase)",
    "if i were [{lang}](lang) how would i say that [{phrase}](phrase)",
    "i must know how to say [{phrase}](phrase) in [{lang}](lang)",
    "i need to know how to say [{phrase}](phrase) in [{lang}](lang)",
    "i need you to translate the sentence '[{phrase}](phrase)' into [{lang}](lang)",
    "in [{lang}](lang) how can I say [{phrase}](phrase)?",
    "in [{lang}](lang) how do i say [{phrase}](phrase)",
    "in [{lang}](lang) how do they say [{phrase}](phrase)",
    "in [{lang}](lang) [{phrase}](phrase) is said how",
    "i want to know how to say [{phrase}](phrase) in [{lang}](lang)",
    "i would i say [{phrase}](phrase) if i were [{lang}](lang)",
    "i would like to know how to say [{phrase}](phrase) in [{lang}](lang)",
    "i would like to know the proper way to [{phrase}](phrase) in [{lang}](lang)",
    "please tell me how to [{phrase}](phrase) in [{lang}](lang)",
    "please translate [{phrase}](phrase) into [{lang}](lang) for me",
    # "[{phrase}](phrase) in [{lang}](lang)",
    "tell me how the [{lang}](lang) say [{phrase}](phrase)",
    "tell me how to say '[{phrase}](phrase)' in [{lang}](lang)",
    "tell me how to say [{phrase}](phrase) in [{lang}](lang)",
    "translate english to [{lang}](lang) [{phrase}](phrase)",
    "translate for me [{phrase}](phrase) into [{lang}](lang)",
    "translate [{phrase}](phrase) in [{lang}](lang)",
    "translate [{phrase}](phrase) into [{lang}](lang) for me",
    "translate [{phrase}](phrase) to [{lang}](lang)",
    "translate [{phrase}](phrase) to [{lang}](lang)",
    "what do i say for [{phrase}](phrase) in [{lang}](lang)",
    "what do [{lang}](lang) people say for the word [{phrase}](phrase)",
    "what do you [{phrase}](phrase) if you were [{lang}](lang)",
    "what expression would i use to say [{phrase}](phrase) if i were an [{lang}](lang)",
    "what is [{lang}](lang) for [{phrase}](phrase)",
    "what is [{phrase}](phrase) in [{lang}](lang)",
    "what is the correct way to say '[{phrase}](phrase)' in [{lang}](lang)",
    "what is the equivalent of '[{phrase}](phrase)' in [{lang}](lang)",
    "what is the right way to say [{phrase}](phrase) in [{lang}](lang)",
    "what is the way to say [{phrase}](phrase) in [{lang}](lang)",
    "what is the word for [{phrase}](phrase) [{lang}](lang)",
    "what phrase means [{phrase}](phrase) in [{lang}](lang)",
    "what [{lang}](lang) word means [{phrase}](phrase)",
    "what's local slang for [{phrase}](phrase) in [{lang}](lang)",
    "what's the [{lang}](lang) word for [{phrase}](phrase)",
    "what's the [{lang}](lang) word you use for [{phrase}](phrase)",
    "what's the word for [{phrase}](phrase) in [{lang}](lang)",
    "what words would i use to [{phrase}](phrase) if i were [{lang}](lang)",
    "what would the word for [{phrase}](phrase) be in [{lang}](lang)",
    "would you tell me how to say [{phrase}](phrase) in [{lang}](lang)",
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
                    sentence = sentence.replace('{phrase}', line.lower()[:-1]).replace('{lang}', lang).lower()
                    final_phrases.append(sentence)

    with open('dataset_generation/final_phrases.txt', 'w') as file:
        for phrase in final_phrases:
            file.write(f'- {phrase}\n')


if __name__ == '__main__':
    generate()
    # xalala = 'Hello Word'
    # xalala = xalala.replace('H', 'CU')[:-1]
    # print(xalala)
