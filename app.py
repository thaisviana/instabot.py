#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))

from src import InstaBot

if __name__ == '__main__':

    bot = InstaBot(
        login=os.environ.get('THAIS_LOGIN', ''),
        password=os.environ.get('THIAS_PASSWORD', ''),
        like_per_day=1400,
        comments_per_day=0,
        tag_list=['iraja','irajá','irajagastro','projetovidanova','irajarj','irajattokas','gabrielzinhodoiraja','irajacity','irajágastrô','irajá555','viladapenha','viladapenharj','viladapenhanews','viladapenhacity','viladapenhacomercial','viladapenhabasquete','viladapenhamaster','viladapenhario','viladapenha_rj','viladapenhadadepressao','vilakosmos','vilakosmosrj','fjuvilakosmos','universalvilakosmos','sdsvilakosmos','pilatesvilakosmos — rua Aiera','madureira,  #naçãomadureira','madureirashopping','joemadureira','nacaomadureira','mercadaodemadureira','admadureira','madureiranewsrj','parquemadureira','viadutodemadureira','vicentedecarvalho','vicentedecarvalhorj','vicentedecarvalhocity, bdnvicentecarvalho','estadioniltonsantos','estádioniltonsantos','estádioníltonsantos','parquedemadureirarj','parquedemadureiraoficial','copacabana(2,483,635)','copacabanabeach','copacabanapalace','fortedecopacabana','brásdepina, brásdepinarj, brásdepinaraiz','duquedecaxias','duquedecaxiasrj','forteduquedecaxias','corridaduquedecaxias','esteticaduquedecaxias','tattooduquedecaxias','clubeduquedecaxias','duquedecaxiastop','duquedecaxiasrjbrasil','duquedecaxiasfc','duquedecaxiasfutebolclube','engenhdarainha','engenhodarainharj','engenhodarainhastation'],
        user_blacklist={},
        max_like_for_one_tag=50,
        follow_per_day=0,
        follow_time=1 * 60,
        unfollow_per_day=0,
        unfollow_break_min=15,
        unfollow_break_max=30,
        log_mod=0,
        proxy='',
        # List of list of words, each of which will be used to generate comment
        # For example: "This shot feels wow!"
        comment_list=[["this", "the", "your"],
                      ["photo", "picture", "pic", "shot", "snapshot"],
                      ["is", "looks", "feels", "is really"],
                      ["great", "super", "good", "very good", "good", "wow",
                       "WOW", "cool", "GREAT","magnificent", "magical",
                       "very cool", "stylish", "beautiful", "so beautiful",
                       "so stylish", "so professional", "lovely",
                       "so lovely", "very lovely", "glorious","so glorious",
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

    mom_bot = InstaBot(
        login=os.environ.get('MOM_LOGIN', ''),
        password=os.environ.get('MOM_PASSWORD', ''),
        like_per_day=1400,
        comments_per_day=0,
        tag_list=['iraja', 'irajá', 'irajagastro', 'projetovidanova', 'irajarj', 'irajattokas', 'gabrielzinhodoiraja',
                  'irajacity', 'irajágastrô', 'irajá555', 'viladapenha', 'viladapenharj', 'viladapenhanews',
                  'viladapenhacity', 'viladapenhacomercial', 'viladapenhabasquete', 'viladapenhamaster',
                  'viladapenhario', 'viladapenha_rj', 'viladapenhadadepressao', 'vilakosmos', 'vilakosmosrj',
                  'fjuvilakosmos', 'universalvilakosmos', 'sdsvilakosmos', 'pilatesvilakosmos — rua Aiera',
                  'madureira,  #naçãomadureira', 'madureirashopping', 'joemadureira', 'nacaomadureira',
                  'mercadaodemadureira', 'admadureira', 'madureiranewsrj', 'parquemadureira', 'viadutodemadureira',
                  'vicentedecarvalho', 'vicentedecarvalhorj',],
        user_blacklist={},
        max_like_for_one_tag=150,
        follow_per_day=0,
        follow_time=0,
        unfollow_per_day=0,
        unfollow_break_min=0,
        unfollow_break_max=0,
        log_mod=0,
        proxy='189.61.107.94:8080',
        comment_list=[[]],
        unwanted_username_list=[],
        unfollow_whitelist=[])

    dad_bot = InstaBot(
        login=os.environ.get('DAD_LOGIN', ''),
        password=os.environ.get('DAD_PASSWORD', ''),
        like_per_day=1400,
        comments_per_day=0,
        tag_list=['vicentedecarvalhocity, bdnvicentecarvalho',
                  'estadioniltonsantos', 'estádioniltonsantos', 'estádioníltonsantos', 'parquedemadureirarj',
                  'parquedemadureiraoficial', 'copacabana(2,483,635)', 'copacabanabeach', 'copacabanapalace',
                  'fortedecopacabana', 'brásdepina, brásdepinarj, brásdepinaraiz', 'duquedecaxias', 'duquedecaxiasrj',
                  'forteduquedecaxias', 'corridaduquedecaxias', 'esteticaduquedecaxias', 'tattooduquedecaxias',
                  'clubeduquedecaxias', 'duquedecaxiastop', 'duquedecaxiasrjbrasil', 'duquedecaxiasfc',
                  'duquedecaxiasfutebolclube', 'engenhdarainha', 'engenhodarainharj', 'engenhodarainhastation'],
        user_blacklist={},
        max_like_for_one_tag=150,
        follow_per_day=0,
        follow_time=0,
        unfollow_per_day=0,
        unfollow_break_min=0,
        unfollow_break_max=0,
        log_mod=0,
        proxy='177.38.181.82:8080',
        comment_list=[[]],
        unwanted_username_list=[],
        unfollow_whitelist=[])
    while True:

        mode = 0

        if mode == 0:
            bot.auto_mod()
