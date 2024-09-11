# Project to select a Anime when one is undecided.

import requests
import random

base_url = "https://api.jikan.moe/v4"

genre_map = {
    'action': 1,            'adventure': 2,
    'avant garde': 5,       'award winning': 46,
    'boys love': 28,        'comedy': 4,
    'drama': 8,             'fantasy': 10,
    'girls love': 26,       'gourmet': 47,
    'horror': 14,           'mystery': 7,
    'romance': 22,          'sci-fi': 24,
    'slice of life': 36,    'sports': 30,
    'supernatural': 37,     'suspense': 41,
    'ecchi': 9,             'erotica': 49,
    'hentai': 12,           'adult cast': 50,
    'anthropomorphic': 51,  'cgdct': 52,
    'childcare': 53,        'combat sports': 54,
    'crossdressing': 81,    'delinquents': 55,
    'detective': 39,        'educational': 56,
    'gag humor': 57,        'gore': 58,
    'harem': 35,            'high stakes game': 59,
    'historical': 13,       'idols (female)': 60,
    'idols (male)': 61,     'isekai': 62,
    'iyashikei': 63,        'love polygon': 64,
    'magical sex shift': 65,'mahou shoujo': 66,
    'martial arts': 17,     'mecha': 18,
    'medical': 67,          'military': 38,
    'music': 19,            'mythology': 6,
    'organized crime': 68,  'otaku culture': 69,
    'parody': 20,           'performing arts': 70,
    'pets': 71,             'psychological': 40,
    'racing': 3,            'reincarnation': 72,
    'reverse harem': 73,    'romantic subtext': 74,
    'samurai': 21,          'school': 23,
    'showbiz': 75,          'space': 29,
    'strategy game': 11,    'super power': 31,
    'survival': 76,         'team sports': 77,
    'time travel': 78,      'vampire': 32,
    'video game': 79,       'visual arts': 80,
    'workplace': 48,        'josei': 43,
    'kids': 15,             'seinen': 42,
    'shoujo': 25,           'shounen': 27
}


class Choice:
    def get_random_anime(self):
        response = requests.get(f"{base_url}/random/anime")
        if response.status_code == 200:
            anime_data = response.json()
            title = anime_data['data']['title']
            return title
        else:
            print("Failed to retrieve random anime.")
            return None
        
    def get_genre_id(self, genre_name):
        """Get the genre ID from a genre name"""
        genre_id = genre_map.get(genre_name)
        if genre_id:
            return genre_id
        else:
            print(f"Genre '{genre_name}' not found.")
            return None
    
    def get_random_anime_by_genre(self):
        # Convert genre name to genre ID
        genre_name = input("Select a specific genre: ").lower() 
        genre_id = self.get_genre_id(genre_name)
        if not genre_id:
            return None
        
        # Fetch a list of anime by genre
        response = requests.get(f"{base_url}/anime?genres={genre_id}&order_by=score")
        if response.status_code == 200:
            anime_data = response.json()
            anime_list = anime_data.get('data', [])
            if anime_list:
                random_anime = random.choice(anime_list)
                title = random_anime['title']
                return title, genre_name  # Return both title and genre_name for the output
            else:
                print(f"No anime found for genre '{genre_name}'.")
                return None
        else:
            print(f"Failed to retrieve anime for genre '{genre_name}'.")
            return None
        

    def get_anime_trailer(self, title):
        pass


if __name__ == "__main__":
    choice_object = Choice()
    
    # Get a completely random anime
    anime = choice_object.get_random_anime()
    if anime:
        print(f"I recommend watching {anime}")
    
    # Get a random anime from a specific genre
    genre_anime = choice_object.get_random_anime_by_genre()
    if genre_anime:
        anime_title, genre_name = genre_anime  # Unpack the tuple returned
        print(f"I recommend watching {anime_title} from the {genre_name.capitalize()} genre!")
