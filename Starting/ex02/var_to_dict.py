def data():
	d = [
		('Hendrix' , '1942'),
		('Allman' , '1946'),
		('King' , '1925'),
		('Clapton' , '1945'),
		('Johnson' , '1911'),
		('Berry' , '1926'),
		('Vaughan' , '1954'),
		('Cooder' , '1947'),
		('Page' , '1944'),
		('Richards' , '1943'),
		('Hammett' , '1962'),
		('Cobain' , '1967'),
		('Garcia' , '1942'),
		('Beck' , '1944'),
		('Santana' , '1947'),
		('Ramone' , '1948'),
		('White' , '1975'),
		('Frusciante', '1970'),
		('Thompson' , '1949'),
		('Burton' , '1939')
	]
	return d

def transfer_tuple_from_dict(tuple):
    myDict = {}
    for artist, year in tuple:
        if year in myDict:
            myDict[year].append(artist)
        else:
            myDict[year] = [artist]
    return myDict

def get_dictionary(myDict):
    for year, artists in myDict.items():
        print(f"{year} : {' '.join(artists)}")

if __name__ == '__main__':
    get_dictionary(transfer_tuple_from_dict(data()))
