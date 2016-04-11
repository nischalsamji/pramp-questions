import string
def readFile():
    input_file = open("sherlock.txt","r")
    input_file_lines = input_file.readlines()
    exclude = set(string.punctuation)
    wordcount_dict = {}
    for each_line in input_file_lines:
        words = each_line.split(" ")
        for each_word in words:
            each_word = ''.join(ch for ch in each_word if ch not in exclude)
            if(each_word.lower() in wordcount_dict.keys()):
                wordcount_dict[each_word.lower()] += 1
            else:
                wordcount_dict[each_word.lower()] = 1
    print wordcount_dict
if __name__ == "__main__":
    readFile()
