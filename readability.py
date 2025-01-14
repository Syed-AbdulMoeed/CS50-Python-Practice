# get input from user
# index = 0.0588 * L - 0.296 * S - 15.8
# L is the average number of letters per 100 words in the text
# S is the average number of sentences per 100 words
# a way to count 100 words
import re

def count_word(string):
    return string.count(" ") + 1

def count_sentence(string):
    return len(re.findall(r"[?!.]", string))


def count_letters(string):
    return len(re.findall(r"[a-zA-Z]", string))
    

def main():
    string = input("Text: ").strip()
    word_num = count_word(string)  # get word num
    sen_num = count_sentence(string)  # get sen num
    let_num = count_letters(string)  #get letter num

    #Apply Coleman-Liau Readability Formula        
    L = (let_num/word_num)*100
    S = (sen_num/word_num)*100
    index = int(round(0.0588 * L - 0.296 * S - 15.8, 0))

    # choose output
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")


main()
