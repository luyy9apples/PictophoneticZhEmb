# Tutorial

This repository contains the implementation for two Chinese word embedding learning methods using semantic and phonetic components, i.e., rPCWE and rsp2vec.



## 0. Environment

- Linux
- gcc
- cmake
- gensim==4.0.0



## 1. Download the dataset

The processed Chinese wikipedia dataset can be downloaded [here](https://drive.google.com/drive/folders/1S6kYAq3BklvxJTh_SaUzHHzsLMlHIt01?usp=drive_link). 

Please unzip the downloaded data under the folder `data/`.



## 2. Train

### rPCWE

To train the rPCWE model, run the following commands under the `rPCWE/src/` folder.

```bash
$ chmod 777 -R .
$ bash run.sh
```



### rsp2vec

To train the rsp2vec model, run the following commands under the `rsp2vec/` folder.

```bash
$ chmod 777 -R .
$ bash run.sh
```



## 3. Evaluate

Evaluate the performance of the trained embeddings on the relevance and analogy tasks by running the following commands:

```shell
$ python eval.py rPCWE/src/word_vec-3-win7-size150-it75.txt
$ python eval.py rsp2vec/rsp-150.vec
```

