import random
from colorama import Fore, Style, init

init(autoreset=True)

def create_files():
    male_names = open("male_names_rus.txt", "r", encoding="utf-8").read().splitlines()
    female_names = (
        open("female_names_rus.txt", "r", encoding="utf-8").read().splitlines()
    )
    names = male_names + female_names

    names = list(map(lambda x: x.lower(), names))

    with open(r'names.txt', 'w', encoding="utf-8") as fp:
        for item in names:
            # write each item on a new line
            fp.write("%s\n" % item)
        print(Fore.GREEN + Style.BRIGHT + "создан файл names.txt")

    # random.shuffle(names)

    train_data = names[:int(len(names)/2)]
    test_data = names[int(len(names)/2):]

    with open(r'names_train.txt', 'w', encoding="utf-8") as fp:
        for item in train_data:
            # write each item on a new line
            fp.write("%s\n" % item)
        print(Fore.GREEN + Style.BRIGHT + "создан файл names_train.txt")

    with open(r'names_test.txt', 'w', encoding="utf-8") as fp:
        for item in test_data:
            # write each item on a new line
            fp.write("%s\n" % item)
        print(Fore.GREEN + Style.BRIGHT + "создан файл names_test.txt")

    return names

create_files()