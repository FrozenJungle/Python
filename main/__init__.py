#!/usr/bin/python3
# -*- coding: utf-8 -*-


import nltk
import jieba
import word2vec
import numpy
import gensim
import pickle
import sys
import os
import logging


def wordvector():
    sents = []

    with open('/Users/zzhsmac/Downloads/sourceData.txt', 'r', encoding='utf-8') as fin:
        while 1:  # 逐行读取文件内容，用jieba分词，每行存到words[]里，逐行append到sents[]
            line = fin.readline()
            if not line: break
            words = list(jieba.cut(line, cut_all=False))
            sents.append(words)

    model = gensim.models.Word2Vec(sents, size=400, min_count=1)
    model.save('/Users/zzhsmac/Downloads/vector.bin')
    model.wv.save_word2vec_format('/Users/zzhsmac/Downloads/vector.tsv')
    print(model.most_similar('夏'))


def __main__():
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)

    wordvector()

if __name__ == '__main__':
    __main__()
