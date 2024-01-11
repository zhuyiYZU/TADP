This is the procedure for adding scrambling to text:

1.First put the dataset to be processed under the textdata file.

2.Load the appropriate dataset using loaddata.py.

3.Using Terminal Commands:

#python train.py --data [0-7] --model [modelname]  ### Train the models that can be used in further attack(train model)


--data [0-7] #select which data to use 

--model [simplernn, bilstm, charcnn] #select the model type to train. 
 



#python attack.py --data [0-7] --model [modelname] --modelpath [modelpath] --power [power] --scoring [algorithm] (attack)

--transformer [algorithm] --maxbatches [batches=20] --batchsize [batchsize=128] ### Generate DeepWordBug adversarial samples

--modelpath [modelpath] #Model path, stored by train.py

--scoring [combined, temporal, tail, replaceone, random, grad] # Scoring algorithm
--transformer [swap, flip, insert, remove, homoglyph] # transformer algorithm

--power [power] # Attack power(integer, in (0,30]) which is number of modified tokens, i.e., the edit distance

--maxbatches [batches=20] # Number of batches of adversarial samples generated, samples are selected randomly. 

For more specific deepwordbug algorithms see https://github.com/QData/deepWordBug.
