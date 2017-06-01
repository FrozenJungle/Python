#!/usr/bin/python3
# -*- coding: utf-8 -*-

import gensim

model = gensim.models.Word2Vec.load('/Users/zzhsmac/Downloads/vector.bin')

print(model.similar_by_word('笑'))