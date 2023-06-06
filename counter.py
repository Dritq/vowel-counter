input1 = input("word: ")
vowels = ['a',
          'e',
          'i',
          'o',
          'u']



def count(word, char):
    a = sum(char == vowels[0] for char in input1)
    e = sum(char == vowels[1] for char in input1)
    i = sum(char == vowels[2] for char in input1)
    o = sum(char == vowels[3] for char in input1)
    u = sum(char == vowels[4] for char in input1)
    vwl = a + e + i + o + u
    
    
    print("\n there are " + str(a) + " a's in " + input1)
    print("\n there are " + str(e) + " e's in " + input1)
    print("\n there are " + str(i) + " i's in " + input1)
    print("\n there are " + str(o) + " o's in " + input1)
    print("\n there are " + str(u) + " u's in " + input1)
    print("\n there are " + str(vwl) + " vowels in " + input1)
count(input1, vowels)
        