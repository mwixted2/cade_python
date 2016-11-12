#start off with a story to fill in
story = '''
{}. But! {} only if ye be {} of valor!
For {} is guarded by a {} so {},
so {}, that no {} yet has {}
with it...and {}!
'''
#main method to get the information from the user for the mad lib
def main():
	command = raw_input('Enter a command (i.e., Eat): ')
	plural_noun = raw_input('Enter a plural noun (i.e., trees): ')
	animal = raw_input('Enter an animal (i.e., cow): ')
	location = raw_input('Enter a location (i.e., Florida OR the playground): ')
	singular_noun = raw_input('Enter a singular noun (i.e., tree): ')

	adjectives = []
	adjectives.append(raw_input('Enter an adjective (i.e., big): '))
	adjectives.append(raw_input('Enter another adjective: '))

	past_participles = []
	past_participles.append(raw_input('Enter a past participle (i.e., played): '))
	past_participles.append(raw_input('Enter another past participle: '))

	#this is how the user input gets added into the story
	mad_lib = story.format(command,
							command,
							plural_noun,
							location,
							animal,
							adjectives[0],
							adjectives[1],
							singular_noun,
							past_participles[0],
							past_participles[1])
	print(mad_lib)

main()