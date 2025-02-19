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

