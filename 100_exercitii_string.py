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

#ex61
text = "Python is easy to learn."
print(text.upper().lower())

#ex62
text = "hello"
print(text.rjust(10, '-'))

#ex63
text = "Python programming is fun!"
print(text.center(30, '_'))

#ex64
text = "python"
print(text.ljust(10, '*'))

#ex65
number = "42"
print(number.zfill(5))

#ex66
text = "Is it safe?"
print(text.replace("fun", "safe"))

#ex67
text = "110101011"
print(int(text, 2))

#ex68
text = "ABCDEF"
print(int(text,16))

#ex69
text = "Python"
print(list(enumerate(text)))

#ex70
text = "Python"
print(' '.join(char * 2 for char in text))

#ex71
text = "Python programming is fun!"
print(text.split()[-1])

#ex72
text = "May the Force be with you."
print(text[:10])

#ex73
text = "You talking to me?"
print(text[:11] if len(text)>11 else text)

#ex74
text = "May the Force be with you."
print(" ".join(text.split()[:3]))

#ex75
text = "!emosewa si nohtyP"
print(text[::-1])

#ex76
text = "I'm gonna make him an offer he can't refuse."
print(' '.join(word[::-1] for word in text.split()))

#ex77
text = "Why don't scientists trust atoms? Because they make up everything!"
print(' '.join(reversed(text.split())))

#ex78
days = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"
print(", ".join(sorted(days.split(", "))))

#ex79
text = "Python is awesome"
reply = "Yes, it is" if text.isalpha() else "no, it's not"
print(reply)

#ex80
text = "Python is easy; python is powerful; python is versatile."
print(text.lower().split().count("Python".lower()))

#ex81
text = "Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh / Caught in a bad romance..."
print(any(char.istitle() for char in text))

#ex82
text = "Python"
print(any(char.isdigit() for char in text))

#ex83
text = "area 51"
print("".join(word for word in text if word.isalpha()))

#ex84
text = ""
print(any(char.isalnum() for char in text))

#ex85
text = "Let s loose them &*"
print(all(char.isalpha() or char.isdigit() for char in text))

#ex86
text = "Python https://www.python.org/ is powerful."
print(any([word.startswith("http") and "." in word for word in text.split()]))

#ex87
text = "Python is easy."
print(sum(1 for char in text if char.lower() in "aeiou"))

#ex88
text = "to be or not to be that is the question"
print(" ".join([word.title() for word in text.split()]))

#ex89
text = "to be or not to be that is the question"
print({word: text.split().count(word) for word in set(text.split())})

#ex90
text = "the cat chased the dog"
print(text.replace("cat", "***").replace("dog", "cat").replace('***', "dog"))

