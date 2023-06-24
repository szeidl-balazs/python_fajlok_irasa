#Opens target file, asks for input, writes input to a file:
def write_favorite_characters_into_a_file(file_name):
    favorit = input('Who is your favorite movie character? ')
    target_file = open(file_name, 'a')
    target_file.write(favorit + '\n')
    target_file.close()

write_favorite_characters_into_a_file('characters.txt')

#Opens the target file and prints its content:
def character_display(opened_file):
    display_target = open(opened_file)
    content = display_target.read()
    print(content)
    display_target.close()

character_display('characters.txt')