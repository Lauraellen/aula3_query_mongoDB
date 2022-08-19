from db.database import Database


class Pokedex:
    def __init__(self):
        self.db = Database(database="pokedex", collection="pokemons")
        self.db.resetDatabase()
        self.collection = self.db.collection

    def find(self, filters: dict):
        response = self.collection.find(filters)
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getAllPokemons(self):
        response = self.collection.find({}, {"name": 1, "_id": 0})
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getPokemonByName(self, name: str):
        response = self.collection.find({"name": name},
                                        {"_id": 0, "name": 1,
                                         "next_evolution": 1, "prev_evolution": 1,
                                         "type": 1, "weaknesses": 1})
        result = {}
        for pokemon in response:
            result = pokemon
        return result

    def getPokemonsByType(self, type: list):
        response = self.collection.find({"type": {"$all": type}}, {
            "_id": 0, "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result

    def getPokemonEvolutionsByName(self, name: str):
        pokemon = self.getPokemonByName(name)

        evolutions = [pokemon['name']]
        hasNextEvolutions = ('next_evolution' in pokemon)
        hasPrevEvolutions = ('prev_evolution' in pokemon)

        if hasNextEvolutions:
            nextEvolutions = list(pokemon['next_evolution'])
            for evolution in nextEvolutions:
                evolution = self.getPokemonByName(evolution['name'])
                evolutions.append(evolution['name'])

        if hasPrevEvolutions:
            previousEvolutions = list(pokemon['prev_evolution'])
            for evolution in previousEvolutions:
                evolution = self.getPokemonByName(evolution['name'])
                evolutions.append(evolution['name'])

        return evolutions

    #retorna o pokemon com o chance_spaw maior que o valor inserido
    def getPokemonWithSpaw(self, spaw: int):
        pokemon = self.collection.find({"spawn_chance": {"$gte": spaw}},
            {"_id": 0, "spawn_chance": 1, "name": 1});

        result = []
        for pokemon in pokemon:
            result.append(pokemon)
        return result

    #retorna a lista de fraquezas do pokemon inserido
    def getWeaknesses(self, name: str):
        pokemon = self.getPokemonByName(name)
        data = pokemon['weaknesses']

        return data

    #retorna os pokemons que possuem a lista de fraquezas inseridas
    def getPokemonsByWeaknesses(self, weakenesses: list):

        response = self.collection.find({"weaknesses": {"$all": weakenesses}}, {
            "_id": 0, "name": 1, "weaknesses": 1, "spawn_chance": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result

    #retorna os pokemons que possuem o nome inserido como próxima evolução
    def getPokemonsByEvolution(self, name: str):
        response = self.collection.find({"next_evolution.name": {"$eq": name}}, {
            "_id": 0, "name": 1, "img": 1, "next_evolution": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result

    #retorna o pokemon com a fraqueza inserida e que não tenha next_evolution
    def getPokemonsByWeakenessAndWithoutEvolution(self, weaknesses: list):
        response = self.collection.find({"weaknesses": {"$all": weaknesses}, "next_evolution": {"$exists": False}, "prev_evolution": {"$exists": False}}, {"_id": 0})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result