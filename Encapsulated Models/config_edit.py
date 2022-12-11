

class Config():
    def __init__(self):
        self.num_classes = 2
        self.seq_len = 60
        self.hidden_size = 1024
        self.batch_size = 32

        self.embedding_file_path = './Embeddings/wiki_word2vec_50.bin'
        self.embedding_length = 50
        self.binary_embedding_file = True

        self.freq_bound = 5

        self.epochs = 2
        self.learning_rate = 2e-5
        self.dropout = 0.3
        self.padding_char = 'I'

        self.kernel_lower_bound = 2
        self.kernel_upper_bound = 5

        self.train_path = './Dataset/train.txt'
        self.test_path = './Dataset/test.txt'
        self.val_path = './Dataset/validation.txt'
        self.stopwords_path = 'stopwords_baidu.txt'
        self.frequent_path = 'frequent_words.txt'


