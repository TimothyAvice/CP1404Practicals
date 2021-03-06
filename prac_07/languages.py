from prac_07.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)

language_list = [ruby, python, visual_basic]

print("The Dynamically types languages are:")
for language in language_list:
    if language.typing == "Dynamic":
        print("{}".format(language.name))