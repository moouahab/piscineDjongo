#!/usr/bin/env python3

import sys

def state(capital_city):
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	if capital_city in capital_cities.values():
		for abbr, city in capital_cities.items():
			if city == capital_city:
				for state_name, state_abbr in states.items():
					if state_abbr == abbr:
						print(state_name)
	else:
		print("Unknown state")


if __name__ == '__main__':
	if len(sys.argv) != 2: sys.exit(1)
	state(' '.join(sys.argv[1].title().split()))
	