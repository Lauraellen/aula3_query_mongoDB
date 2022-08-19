from db.pokedex import Pokedex
from helper.WriteAJson import writeAJson

pokedex = Pokedex()

pokemonWithSpaw = pokedex.getPokemonWithSpaw(3)
writeAJson(pokemonWithSpaw, "Pokemon With Spaw")

weaknesses = pokedex.getWeaknesses("Butterfree")
writeAJson(weaknesses, "Fraquezas")

pokemonByWeaknesses = pokedex.getPokemonsByWeaknesses(["Fire", "Flying"])
writeAJson(pokemonByWeaknesses, "Pokemons by weakenesses")

pokemonByEvolution = pokedex.getPokemonsByEvolution("Venusaur")
writeAJson(pokemonByEvolution, "Pokemons by evolution")

PokemonsByWeakenessAndWithoutEvolution = pokedex.getPokemonsByWeakenessAndWithoutEvolution(["Fire"])
writeAJson(PokemonsByWeakenessAndWithoutEvolution, "Pokemons by weakenesses and without evolutions")