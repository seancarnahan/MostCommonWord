# implement use of a dictionary with (word : value)

def main():
    words = {}


    fil = get_file_name()
    num_of_words = get_num_of_words()

    #return a list of words
    separated_words = read_file(fil)

    list_of_words = get_clean_word(separated_words)
    dict_words = get_blank_dict(list_of_words)

    dict_words = count_words(list_of_words, dict_words)

    top_dict_words = determine_top_words(dict_words, num_of_words)

    display_output(top_dict_words, num_of_words)



def get_num_of_words() -> int:
    num_of_words = input("Enter how many top words you want to see: ")
    num_of_words = int(num_of_words)
    return num_of_words


def get_file_name() -> str:
    fil = input("Enter the name of the file: ")
    return fil

def read_file(file_name) -> list:
    #return a list of words
    #method not completed yet I still have to figure out how I am going to test this
    #this method is not done yet
    #the read function will make the whole file into a string, which is kind of what you want to do
    list_of_words = []

    f = open(file_name, "r")
    line = f.readline()
    words_from_file = line.split(" ")
    return  list_of_words









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

    while True:
        n = 0
        words = []


        values = dict_words.values()
        max_value = max(values)

        for word in dict_words:
            if dict_words[word] == max_value:
                n += 1
                checker -= 1


                words.append(word)


        for word in words:
            del dict_words[word]

        words.sort()

        len_of_words = len(words)

        print("The following words appeared", max_value, "times each: ", end="")


        if n == 1:
            word = ""
            word += words[0]
            print(word, end="")
        else:
            for i in range(len_of_words - 1):
                if i == 0:
                    print(words[i] + ",", end = "")
                else:
                    print(" " + words[i] + ",", end="")
            print(" " + words[-1])

        print("")

        if checker <= 0:
            break


def get_clean_word(words : list) -> list:
    clean_words = []
    strip_chars = [",", ".", ":", ";", "\"", "|", "\\", "!", "@", "$", "%", "^", "&", "*", "()", "_", "+", "-", "=", "[", "]", "{", "}", "<", ">", "?", "/", "~", "`", "\'", "/#"]
    strip_chars_len = len(strip_chars)

    for word in words:
        word = word.strip()

        checker = 0
        while checker <= strip_chars_len:

            for i in strip_chars:
                word = word.strip(i)

            checker += 1
        clean_words.append(word)

    return clean_words


def display_output(top_dict_entries, num_of_words):
    #sort() lowest to highest
    # 3 conditions:
    """
    1. print from highest to lowest
    2. if repeated same number of times then go alphabetically
    3. if num_of_words is greater than the amount of unique words then print all words

    The following words appeared 15 times each: break, fake, hate, play

    """

        #print("The following words appeared", top_dict_entries[entry], "times each: ")


if __name__ == "__main__":
    #main()
    #print(gt_clean_word("   $%^&*foo,.   "))
    determine_top_words({"foo": 5,"mack" : 6, "charlie" : 6,  "taj" : 7, "chris" : 8}, 3)
