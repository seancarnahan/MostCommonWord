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

    top_dict_words = determine_top_words(dict_words)

    display_output(top_dict_words)





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

def determine_top_words(dict_words) -> dict:
    top_dict_entries = {}

    



    #return top_dict_entries










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



def display_output(top_dict_words, num_of_words):
    #sort() lowest to highest
    # 3 conditions:
    """
    1. print from highest to lowest
    2. if repeated same number of times then go alphabetically
    3. if num_of_words is greater than the amount of unique words then print all words

    """
    list_of_keys = top_dict_words.keys()

    for i in range(num_of_words):
        print("The following words appeared", top_dict_words[i], "times each: ")



if __name__ == "__main__":
    #main()
    #print(gt_clean_word("   $%^&*foo,.   "))
    print(determine_top_words({"foo": 5, "charlie" : 6}))
