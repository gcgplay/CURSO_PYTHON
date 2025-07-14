# json.dumps e json.loads com strings + typing.TypedDict

# dumps - jogar pra fora - string
# loads - carregar pra dentro - string

import json
from pprint import pprint
from typing import TypedDict #tipar como dict

class Movie(TypedDict): #tipagem
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float

#object --> dict
string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

filme: Movie = json.loads(string_json) #classe com tipagem - dict

# dump - Python --> JSON
# corrigir problema com os acentos
# print(json.dumps(filme, ensure_ascii=False, indent=2))

json_string = json.dumps(filme, ensure_ascii=False,indent=2)
print(json_string) #str

# pprint(filme)
# print(filme['title'])
# print(filme['characters'][[0]])
# print(file=['year'] + 10)

# print(string_json) #já funciona como doc string no Python
