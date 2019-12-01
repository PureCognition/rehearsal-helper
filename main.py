import sys
import pprint
import json
import pyttsx3

pp = pprint.PrettyPrinter(indent=4)
engine = pyttsx3.init()

readmode = True
checkmode = False

if len(sys.argv) > 1:
    mode = sys.argv[1]
    if mode.upper() == "READ" and mode.upper() != "CHECK":
        readmode = True
        checkmode = False
    elif mode.upper() != "READ" and mode.upper() == "CHECK":
        readmode = False
        checkmode = True

with open('thestar-thaddeus.json') as json_file:
    data = json.load(json_file)

title = data['title']
actor = data['actor']
character = data['character']

welcome_text = f'Welcome to {title} with {actor} as {character}'

print(welcome_text)
engine.say(welcome_text)
engine.runAndWait()

for scene in data['scenes']:
    scene_number = scene['number']
    scene_title = scene['title']

    scene_text = f'Scene {scene_number}: {scene_title}'
    print(scene_text)
    engine.say(scene_text)
    engine.runAndWait()

    for part in sorted(scene['parts'], key=lambda x: x['number']):
        part_number = part['number']

        for line in sorted(part['lines'], key=lambda x: x['number']):
            line_number = line['number']
            line_character = ""
            my_character = True
            if "character" in line:
                line_character = line['character']
                my_character = False
            else:
                line_character = f'{character}'
            line_content = line['content']

            if my_character:
                print()
                if readmode:
                    print(f'*{line_character}: {line_content}')
                    print()
                    input("Say line and then press Enter")
                if checkmode:
                    input("Say line and then press Enter")
                    print()
                    print(f'*{line_character}: {line_content}')
                    print()
                    input("Check line and then press Enter")
                print()
            else:
                print(f'{line_character}: {line_content}')
                engine.say(line_content)
                engine.runAndWait()
