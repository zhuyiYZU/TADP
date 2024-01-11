# -*- coding: utf-8 -*-
# 这一段是实体概念扩展
import logging
import sys
import subprocess
import time
import os

"""'newsgroups3', 'newsgroups4', 'newsgroups5', 'newsgroups6', 'reuters1', 'reuters3', 'reuters4','amazon_d-e', 'amazon_e-b', 'amazon_e-d', 'amazon_e-k' """
if __name__ == '__main__':
    l = ['newsgroups6']
    for n in l:


        for i in {2}:

            for b in {32}:

                for e in {10}:
                    start_time = time.time()
                    for j in {100, 110, 120, 130, 140}:

                        cmd = "python fewshot.py --result_file support_exp/news6_half.txt --dataset  " + n + " --template_id " + str(i) + \
                              " --seed  " + str(j) + " --shot 20 --verbalizer manual --batch_s " + str(b) + " --max_epochs " + str(e)
                        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        p.communicate()

                        print("train seed {}:preprocess down".format(j))

                    end_time = time.time()
                    run_time = (end_time - start_time) / 5 * 3

                    print('dataset: ' + n + 'template: ' + str(i) + 'seed: 3次 run time: ' + str(run_time))
                    with open('time.csv', 'a+', encoding='utf-8') as t:
                        t.write('dataset: ' + n + ' template: ' + str(i) + ' seed: 3次 run time: ' + str(run_time) + '\n')

                    print("train template {}:preprocess down".format(i))

        print("train dataset {}:preprocess down".format(n))



