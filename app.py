#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import dotenv
from src import InstaBot

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))

location_ids = [{'location_id': '1280110728803296', 'name': 'Paquetá, Rio de Janeiro, Brasil'},
{'location_id': '199463547260199', 'name': 'Freguesia (Ilha), Rio de Janeiro, Brasil'},
{'location_id': '552578381419600', 'name': 'Bancários, Rio de Janeiro, Brasil'},
{'location_id': '394850810', 'name': 'Galeão, Rio de Janeiro, Brasil'},
{'location_id': '1229728087178808', 'name': 'Tauá, Rio de Janeiro, Brasil'},
{'location_id': '975591165', 'name': 'Portuguesa, Rio de Janeiro, Brasil'},
{'location_id': '547663022385107', 'name': 'Moneró, Rio de Janeiro, Brasil'},
{'location_id': '336848326891981', 'name': 'Campo Grande, Rio de Janeiro, Brasil'},
{'location_id': '15679401', 'name': 'Vigário Geral, Rio de Janeiro, Brasil'},
{'location_id': '261264416', 'name': 'Cocotá, Rio de Janeiro, Brasil'},
{'location_id': '261766101', 'name': 'Jardim América, Rio de Janeiro, Brasil'},
{'location_id': '401705473372965', 'name': 'Jardim Carioca, Rio de Janeiro, Brasil'},
{'location_id': '220220275', 'name': 'Pavuna, Rio de Janeiro, Brasil'},
{'location_id': '234646201', 'name': 'Cordovil, Rio de Janeiro, Brasil'},
{'location_id': '204536280154055', 'name': 'Jardim Guanabara, Rio de Janeiro, Brasil'},
{'location_id': '235688406', 'name': 'Parada de Lucas, Rio de Janeiro, Brasil'},
{'location_id': '221030215', 'name': 'Parque Colúmbia, Rio de Janeiro, Brasil'},
{'location_id': '479236189105784', 'name': 'Praia da Bandeira, Rio de Janeiro, Brasil'},
{'location_id': '216766657', 'name': 'Penha Circular, Rio de Janeiro, Brasil'},
{'location_id': '213456388', 'name': 'Bangu, Rio de Janeiro, Brasil'},
{'location_id': '542835105893696', 'name': 'Cacuia, Rio de Janeiro, Brasil'},
{'location_id': '213719191', 'name': 'Irajá, Rio de Janeiro, Brasil'},
{'location_id': '223372926', 'name': 'Anchieta, Rio de Janeiro, Brasil'},
{'location_id': '248373894', 'name': 'Acari, Rio de Janeiro, Brasil'},
{'location_id': '301916146619591', 'name': 'Pitangueiras, Rio de Janeiro, Brasil'},
{'location_id': '237995086', 'name': 'Costa Barros, Rio de Janeiro, Brasil'},
{'location_id': '788901977928887', 'name': 'Braz de Pina, Rio de Janeiro, Brasil'},
{'location_id': '230234308', 'name': 'Penha, Rio de Janeiro, Brasil'},
{'location_id': '11510042', 'name': 'Zumbi, Rio de Janeiro, Brasil'},
{'location_id': '280193904', 'name': 'Ribeira, Rio de Janeiro, Brasil'},
{'location_id': '216781015', 'name': 'Coelho Neto, Rio de Janeiro, Brasil'},
{'location_id': '224470892', 'name': 'Guadalupe, Rio de Janeiro, Brasil'},
{'location_id': '947557395409369', 'name': 'Parque Anchieta, Rio de Janeiro, Brasil'},
{'location_id': '239025759', 'name': 'Barros Filho, Rio de Janeiro, Brasil'},
{'location_id': '267012193', 'name': 'Vista Alegre, Rio de Janeiro, Brasil'},
{'location_id': 'ricardodealbuquerque', 'name': 'Ricardo de Albuquerque, Rio de Janeiro, Brasil'},
{'location_id': '872698813', 'name': 'Colégio, Rio de Janeiro, Brasil'},
{'location_id': '236573243', 'name': 'Honório Gurgel, Rio de Janeiro, Brasil'},
{'location_id': '316914492106397', 'name': 'Olaria, Rio de Janeiro, Brasil'},
{'location_id': '230234308', 'name': 'Vila da Penha, Rio de Janeiro, Brasil'},
{'location_id': '313730442', 'name': 'Maré, Rio de Janeiro, Brasil'},
{'location_id': '227192698', 'name': 'Vila Militar, Rio de Janeiro, Brasil'},
{'location_id': 'cidadeuniversit%C3%A1ria', 'name': 'Cidade Universitária, Rio de Janeiro, Brasil'},
{'location_id': '224350441', 'name': 'Rocha Miranda, Rio de Janeiro, Brasil'},
{'location_id': '235004466', 'name': 'Ramos, Rio de Janeiro, Brasil'},
{'location_id': '227478062', 'name': 'Realengo, Rio de Janeiro, Brasil'},]


if __name__ == '__main__':

    tata_bot = InstaBot(
        login=os.environ.get('LOGIN', ''),
        password=os.environ.get('PASSWORD', ''),
        like_per_day=1400,
        comments_per_day=0,
        tag_list=['l:' + id['location_id'] for id in location_ids][::-2],
        user_blacklist={},
        max_like_for_one_tag=250,
        follow_per_day=0,
        follow_time=1 * 60,
        unfollow_per_day=0,
        unfollow_break_min=15,
        unfollow_break_max=30,
        log_mod=0,
        proxy='',
        database_name='follows_db.db',
        # List of list of words, each of which will be used to generate comment
        # For example: "This shot feels wow!"
        comment_list=[["this", "the", "your"],
                      ["photo", "picture", "pic", "shot", "snapshot"],
                      ["is", "looks", "feels", "is really"],
                      ["great", "super", "good", "very good", "good", "wow",
                       "WOW", "cool", "GREAT", "magnificent", "magical",
                       "very cool", "stylish", "beautiful", "so beautiful",
                       "so stylish", "so professional", "lovely",
                       "so lovely", "very lovely", "glorious", "so glorious",
                       "very glorious", "adorable", "excellent", "amazing"],
                      [".", "..", "...", "!", "!!", "!!!"]],
        # Use unwanted_username_list to block usernames containing a string
        ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
        ### 'free_followers' will be blocked because it contains 'free'
        unwanted_username_list=[
            'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
            'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
            'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
            'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
            'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
            'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
            'follow', 'follower', 'gain', '.id', '_id', 'bags'
        ],
        unfollow_whitelist=['example_user_1', 'example_user_2'])
#    bot.locations()

    while True:

        mode = 0

        if mode == 0:
            tata_bot.auto_mod()
