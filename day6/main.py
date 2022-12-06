from collections import Counter
def main():
    print(OpenFile('input.txt'))
    print(SearchForSignal(OpenFile('input.txt'), 4))
    print(SearchForSignal(OpenFile('input.txt'), 14))

def OpenFile(input):
    with open(input) as f:
        text = f.readlines()
        text_fixed = [x[0:len(x)-1].split() for x in text]
    return text_fixed[0][0]

def SearchForSignal(text:str,number_of_letters:int):
    for i in range(len(text)):
        c = Counter(text[i:number_of_letters+i])
        if len(c.keys()) == number_of_letters:
            return i + number_of_letters

if __name__ == '__main__':
    main()