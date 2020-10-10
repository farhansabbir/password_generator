# password_generator
This is a complex password generator written in pure python.
The character classes are ASCII characters of:
- UPPER case [A-Z]
- lower case [a-z]
- special characters [!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]
- numbers [0-9]

Length of classes depend on two factors:
- length_determiner, which is default to 3. Hence Upper case characters are 1/3 or entire password length
- length of all previous characters out of total length supplied

Its pretty fast (so are many other libraries). The only speciality between this and other libraries is, this one has configurability to change the 
char class lengths and follows pretty strong password complexity, i.e. patternless and as much random as possible. :)
