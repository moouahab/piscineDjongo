#!/usr/bin/env python3
import sys

def	is_state(state, dict_value):
	return state in dict_value

def is_city(city, dict_value):
	return city in dict_value.values()

def capital_city(state, dict_city, dict_state):
	if state in dict_state :
		return dict_city[dict_state[state]]
	
def state(capital_city, dict_state, dict_city):
	if capital_city in dict_city.values():
		for abbr, city in dict_city.items():
			if city == capital_city:
				for state_name, state_abbr in dict_state.items():
					if state_abbr == abbr:
						return state_name


if __name__ == '__main__':
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
	if len(sys.argv) != 2:
		sys.exit(1)

	input_data = sys.argv[1]
	cleaned_input = ' '.join(input_data.split())
	tab = cleaned_input.split(",")
	
	for e in tab:
		e = e.title().strip()
		if is_state(e, states):
			print(f"{capital_city(e, capital_cities, states)} is the capital of {e}")
		elif is_city(e, capital_cities):
			print(f"{e} is the capital of {state(e, states, capital_cities)}")
		elif e == "":
			continue
		else:
			print(f"{e} y is neither a capital city nor a state")