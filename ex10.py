#define variables with various escapes
#tab escaoe
tabby_cat = "\tI'm tabbed in."
#new line escape
persian_cat = "I'm split\non a line."
#single backslash escape
backslash_cat = "I'm \\ a \\ cat."
#triple line escape with various tabs
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
#double quote escape
skinny_cat = "I only weigh \"18 pounds\""

#print variables
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(skinny_cat)

#determine format via formatter
formatter = "{}\n{}\n\t{}\n{}"
print(formatter.format(tabby_cat, skinny_cat, persian_cat, backslash_cat))