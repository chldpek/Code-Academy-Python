#Section 6.3
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")

#Section 6.4
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")
if len(original)>0:
    print original
else:
    print "empty"

#Section 6.5
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")
if len(original)>0 and original.isalpha():
    print original
else:
    print "empty"

#Section 6.6
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")
if len(original)>0 and original.isalpha():
    print original
else:
    print "empty"

#Section 6.8
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = original[0]
    print original
else:
    print 'empty'

#Section 6.9
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = original[0]
    new_word = word + first + pyg
    print original
else:
    print 'empty'

#Section 6.10
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = original[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print original
    print new_word
else:
    print 'empty'

#Section 6.11
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = original[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'
