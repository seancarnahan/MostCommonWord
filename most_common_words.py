# implement use of a dictionary with (word : value)
#3. if num_of_words is greater than the amount of unique words then print all words



def main():
    words = {}


    fil = get_file_name()
    num_of_words = get_num_of_words()

    #return a list of words
    separated_words = read_file(fil)

    list_of_words = get_clean_word(separated_words)
    dict_words = get_blank_dict(list_of_words)

    dict_words = count_words(list_of_words, dict_words)

    determine_top_words(dict_words, num_of_words)


def get_num_of_words() -> int:
    num_of_words = input("Enter how many top words you want to see: ")
    num_of_words = int(num_of_words)
    return num_of_words


def get_file_name() -> str:
    fil = input("Enter the name of the file: ")
    return fil

def read_file(file_name) -> list:
    #file_name = "/Users/seancarnahan/PycharmProjects/ECS10/MostCommonWord/check_test_file.txt"
    #file_name = "/Users/seancarnahan/PycharmProjects/ECS10/MostCommonWord/one_more_night.txt"

    with open(file_name, 'r') as myfile:
        data = myfile.read().replace('\n', ' ')

    list_of_words = data.split(" ")
    return  list_of_words

def get_clean_word(words : list) -> list:
    clean_words = []
    strip_chars = [",", ".", ":", ";", "\"", "|", "\\", "!", "@", "$", "%", "^", "&", "*", "()", "_", "+", "-", "=", "[", "]", "{", "}", "<", ">", "?", "/", "~", "`", "\'", "/#"]
    strip_chars_len = len(strip_chars)
    words_to_skip = ["a", "an", "and", "in", "is", "the"]

    for word in words:
        word = word.strip()

        checker = 0
        while checker <= strip_chars_len:

            for i in strip_chars:
                word = word.strip(i)

            checker += 1
        word = word.lower()


        if word in words_to_skip or word == "":
            pass
        else:
            clean_words.append(word)
    return clean_words

def get_blank_dict(words : list) -> dict:
    dict_words = {}
    for word in words:
       dict_words[word] = 0

    return dict_words


def count_words(list_of_words, dict_words) -> dict:
    for word in list_of_words:
        dict_words[word] += 1

    return dict_words


def determine_top_words(dict_words, num_of_words) -> None:
    checker = num_of_words
    len_dict_words = len(dict_words)
    x = 0

    while x < len_dict_words:

        n = 0
        words = []


        values = dict_words.values()
        max_value = max(values)

        for word in dict_words:
            if dict_words[word] == max_value:
                words.append(word)
                n += 1
                x += 1
        checker -= 1


        for word in words:
            del dict_words[word]

        words.sort()

        len_of_words = len(words)

        print("The following words appeared", max_value, "times each: ", end="")


        if n == 1:
            for i in range(len_of_words):
                print(words[0], end="")
        else:
            for i in range(len_of_words - 1):
                if i == 0:
                    print(words[i] + ",", end = "")
                else:
                    print(" " + words[i] + ",", end="")
            print(" " + words[-1], end="")

        print("")



        if checker <= 0:
            break

if __name__ == "__main__":
    main()