# на Русском
letters = [c for c in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЭЮЯ1234567890-/?!']
morse = ['.-', '-...', '.--', '--.', '-..', '.', '...-', '--..', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '.-.', '...', '-', '..-', '..-.', '....', '-.-.', '---.', '----', '--.-', '-..-', '-.--', '..-..', '..--', '.-.-', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----', '-....-', '-..-.', '..--..', '--..--']

work_map = dict(zip(letters, morse))

input_string = input().upper()
output_string = (work_map.get(letter) for letter in input_string if work_map.get(letter))

print(' '.join(output_string))

# на Английском

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
#
# work_map = dict(zip(letters, morse))
#
# input_string = input().upper()
# output_string = (work_map.get(letter) for letter in input_string if work_map.get(letter))
#
# print(' '.join(output_string))