#ex1

text1 = "Hello"
text2 = "World"
print(text1+text2)
    
#ex2
text = " all right "
print(text * 3)

#ex3
text = "10" + "0" * 3
print(text)

#ex4
text = "3.1415"
number = 3.1415
print(text == number)

#ex5
text1 = "not all strings are create equal"
text2 = '''not all strings are create equal'''
print(text1 == text2)

#ex6

text1 = """strings are awesome"""
text2 = "strings are awesorne"
print(text1 != text2)

#ex7
text1 = """awesome"""
text2 = "awesome"
print(text1 is text2)

#ex8 
text = "hello"
print("L" in text)

#ex9
text = " Python is great."
print("python" not in text)

#ex10
adjective = "Awesome"
print(not adjective)
      
#ex11
text = 'good' or 'bad'
print(text)

#ex12
text = 'good' and ' bad'
print(text)

#ex13
text = 'Houston, we have a problem.'
print(len(text))

#ex14
text = "caiac"
print(list(text))

#ex15
text = "caiac"
print(set(text))
print(list(set(text)))   #pentru a lista elementele unice

#ex16
city1 = "Barcelona"
city2 = "Berlin"
print(city1 < city2)

#ex17
text = "python"
print(text[2])

#ex18
text = "python"
print(text[-2:])

#ex19
word = "python"
print(word[::-1])

#ex20
text = '{} {} {}'.format('Take', 'Ianke', 'Cadr')
print(text)

#ex21
movie = "The Godfather"
character = "Don Vito Corleone"
quote = "I'm gonna make him an offer he cant't refuse."
print(f"In the movie '{movie}', {character} say: '{quote}'")

#ex22
nr = 123111456
print(f'{nr:,}')

#ex23
text = '1_111'
print(int(text))

#ex24
text = "python programming"
print(text.title())

#ex25
text = "python"
print(text.istitle())

#ex26
text = "I love Python"
print(text.capitalize())

#ex27
text = "It's ALIVE! It's ALIVE!"
print(text.swapcase())

#ex27
text = "Python is powerful."
print(text.endswith("."))

#ex29
name = "John Doe"
print(name.startswith('John'))

#ex30
word = "banana"
print(word.count("a"))

#ex31
text = "the good, the bad, the ugly"
print(text.find("the"))

#ex32
text = 'My name is Bond, James Bond'
print(text.rfind("Bond"))

#ex33
text = "the good, the bad, the ugly"
print(text.index("the"))

#ex34
text = "Python is powerful."
print(text.partition("is"))

#ex35
text = "Python is powerful."
print(text.rpartition("is"))

#ex36
text="Hasta la vista, baby."
print(text.replace("baby","honey"))

#ex37
text = "   Hit the road, Jack   "
print(text.strip())

#ex38
text = "   What a wonderful world.   "
print(text.rstrip())

#ex39
sentence = "May the Force be with you"
print(sentence.split())

#ex40
email = "user@example.com"
print(email.split('@')[1])

#ex41
phrase ="  Spaces around  "
print(len(phrase.strip().split()))

#ex42
text = "Hello, how are you?"
print([len(word) for word in text.split()])

#ex43
text = "123"
new_text = "1".join(text)
print(new_text)

#ex44
sentence = "This is a sentence."
print('-'.join(sentence.split()))

#ex45
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(" I believe I can fly\n".join(days))

#ex46
text = "Python is fun"
print(" ".join(text.split()[::-1]))

#ex47
text =  """Monday
    Tuesday
        Wednesday
            Thursday
                Friday
                    Saturday
                        Sunday
                            learn
                                Python"""
print([linie.strip() for linie in text.splitlines()])

#ex48
text = "python"
print(text[2::2])

#ex49
text = "Imagination is more important thank knowledge"
print(text.removeprefix("Imagination"))

#ex50
text = "Be the change that you wish to see in the world."
print(text.removesuffix("in the world."))

#ex51
text = "abc123"
print(text.isalnum())

#ex52
text = "abc123"
print(text.isalpha())

#ex53
text = "123 "
print(text.isnumeric())

#ex54
text = "10o0"
print(text.isdecimal())

#ex55
text = " 12345 "
print(text.isdigit())

#ex56
text = "python"
print(text.isspace())

#ex57
text = "I\'m king of \the world"
print(text)

#ex58
text = "My #1 favorite is you? \n"
print(text.isprintable())

#ex59
text = "Hello\tWorld"
print(text.expandtabs(4))

#ex60
text = "python"
print(text.isupper())



