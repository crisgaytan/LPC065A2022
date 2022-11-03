import requests

url_api = 'http://pokeapi.co/api/v2/pokemon/'

def main():
	pokemon_name = input("Dame el nombre de un pokemon:")
	pokemon_data_url = url_api + pokemon_name

	data = get_pokemon_data(pokemon_data_url)
	
	print(data)
	

def get_pokemon_data(url_pokemon=''):
	pokemon_data = {
		"name": '',
		"height": '',
		"abilities": "",
		"types": "",
		"weight": "",
	}

	response = requests.get(url_pokemon)
	data = response.json()

	pokemon_data['name'] = data['name']
	pokemon_data['height'] = data['height']
	pokemon_data['abilities'] = data['abilities']
	pokemon_data['types'] = data['types']
	pokemon_data['weight'] = data['weight']
	
	return pokemon_data

if __name__ == '__main__':
	main()
