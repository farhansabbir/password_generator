
import random
import string
import sys
if len(sys.argv) < 2 or int(sys.argv[1]) < 8:
    print("Need argument or argument must be larger than 8")
    sys.exit(1)
TOTAL_PASSWORD_LENGTH = int(sys.argv[1])
REMAINING = TOTAL_PASSWORD_LENGTH

def getRandomList(length, the_list):
    ret = list()
    for i in range(0,length):
        ret.append(random.choice(the_list))
    return ret

def getCharsetLengths(total_password_length=TOTAL_PASSWORD_LENGTH,previous_charset_length=0):
    global REMAINING 
    length_determiner=3
    length = (REMAINING-previous_charset_length)//length_determiner
    REMAINING = TOTAL_PASSWORD_LENGTH - length
    return length

def generatePassword():
    TOTAL_UPPER_LENGTH = getCharsetLengths()
    TOTAL_LOWER_LENGTH = getCharsetLengths()
    TOTAL_DIGIT_LENGTH = getCharsetLengths()
    TOTAL_SPECIAL_LENGTH = TOTAL_PASSWORD_LENGTH - TOTAL_UPPER_LENGTH - TOTAL_LOWER_LENGTH - TOTAL_DIGIT_LENGTH

    LOWER = list(string.ascii_lowercase)
    UPPER = list(string.ascii_uppercase)
    SPECIALS = list(string.punctuation)
    DIGITS = list(string.digits)

    FINAL = getRandomList(TOTAL_UPPER_LENGTH,UPPER) + \
            getRandomList(TOTAL_LOWER_LENGTH,LOWER) + \
            getRandomList(TOTAL_SPECIAL_LENGTH,SPECIALS) + \
            getRandomList(TOTAL_DIGIT_LENGTH,DIGITS)
    for i in range((int(random.random()*100))):
        random.shuffle(FINAL)
    return "".join(FINAL)

if __name__ == "__main__":
    print(generatePassword())