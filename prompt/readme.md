Here's the code for defence using prompt：

Firstly install OpenPrompt https://github.com/thunlp/OpenPrompt
Then copy prompts/knowledgeable_verbalizer.py to Openprompt/openprompt/prompts/knowledgeable_verbalizer.py

Specific use steps:

1.Firstly put your dataset in the TextClassification folder under the datasets folder in the format of the acl dataset in it. Meanwhile, configure the corresponding template and verbalizer in TextClassification in the scripts file.(The pre-disturbance data is placed in train.py and the post-disturbance data is placed in test.py)

2.Next, configure the hyperparameters under fwshot.py.

3.Finally the training is performed under the final_train.py file.