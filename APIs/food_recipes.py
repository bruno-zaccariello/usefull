my_id = 'a8f0a160'
my_key = '757c599ff766be917054f3e2ef450a56'


'''
    *str q = query text
    *str r = recipe id
    str app_id = id
    str app_key = key
    int from = first result index
    int to = last result index
    int ingr = maximum ingredients
    enum diet = “balanced”, “high-protein”, “high-fiber”, “low-fat”, “low-carb”, “low-sodium”
    enum health =
    range calories = MIN-MAX
     
'''

import requests as r

class food_search():
    def __init__(self,
                 app_id,
                 app_key,
                 q=False,           # str
                 r=False,           # str
                 from_=False,       # int
                 to=False,          # int
                 ingr=False,        # int
                 calories=False,    # range MIN-MAX
                 ):

        self.diet = {
            'balanced':0,
            'high-fiber':0,
            'high-protein':0,
            'low-carb':0,
            'low-fat':0,
            'low-sodium':0,
            }

        self.health = {
            'alcohol-free':0,
            'celery-free':0,
            'crustacean-free':0,
            'dairy-free':0,
            'egg-free':0,
            'fish-free':0,
            'gluten-free':0,
            'kidney-friendly':0,
            'kosher':0,
            'low-potassium':0,
            'lupine-free':0,
            'mustard-free':0,
            'No-oil-added':0,
            'low-sugar':0,
            'paleo':0,
            'peanut-free':0,
            'pescatarian':0,
            'pork-free':0,
            'red-meat-free':0,
            'sesame-free':0,
            'shellfish-free':0,
            'soy-free':0,
            'sugar-conscious':0,
            'tree-nut-free':0,
            'vegan':0,
            'vegetarian':0,
            'wheat-free':0,
            }


        self.app_id = app_id
        self.app_key = app_key

        self.clean_url = f'https://api.edamam.com/search?app_id={app_id}&app_key={app_key}&'

        if r:
            self.url = self.clean_url + f'r={r}&'
        else:
            self.url = self.clean_url + f'q={q}&'

        self.url += f'from={from_}&' if from_ else ''
        self.url += f'to={to}&' if to else ''
        self.url += f'ingr={ingr}&' if ingr else ''
        self.url += f'calories={calories}&' if calories else ''

    def add_diet(self, diet):
        opts = dict(self.diet)
        if diet in opts.keys() and 1 not in opts.values():
            self.diet[diet] = 1
        return self

    def remove_diet(self):
        for item in self.diet:
            item = 0
        return self

    def add_health(self, health):
        opts = dict(self.health)
        if health in opts.keys() and 1 not in opts.values():
            self.health[health] = 1
        return self

    def remove_health(self):
        for item in self.health:
            item = 0
        return self

    def get_result(self):
        url = self.url
        for k, v in self.diet.items():
            if v == 1:
                url += f'diet={k}&'
        for k, v in self.health.items():
            if v == 1:
                url += f'health={k}&'
        result = r.get(url).json()
        hits = result.get('hits')
        for hit in hits:
            print(f'''
            Recipe Name: {hit["recipe"]["label"]}
            Made by: {hit["recipe"]["source"]}
            Ingredients:
                {hit["recipe"]["ingredientLines"]}
            \n
            ''')
        return result