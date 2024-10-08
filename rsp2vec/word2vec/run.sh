
path_input=./sample
path_output=.

./word2vec/bin/word2vec substotune -input ../data/wikisimplecor_used.txt -infeature ${path_input}/rst.txt -output rsp-150 -lr 0.025 -dim 150 -ws 7 -epoch 50 -minCount 10 -neg 5 -loss ns -minn 3 -maxn 12 -thread 8 -t 1e-4 -lrUpdateRate 100;