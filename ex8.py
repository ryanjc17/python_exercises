#defining the formatter "format"
formatter = "{} {} {} {}"

#listing the text or integers that should fall within the brackets by using .format()
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(formatter, formatter, formatter, formatter))
#Got an index error the first time I ran this. I had the commas withint he parentheses by mistake.
print(formatter.format(
	"It's beginning to look a lot like Christmas",
	"Everywhere we go.",
	"Ha.",
	"Severus Snape."
))