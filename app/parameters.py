class parameters(object):
    def __init__(self):
        self.dic = {}
        self.dic['mymedialite'] = False
        self.dic['file_train'] = None
        self.dic['file_test'] = None
        self.dic['file_feature'] = None
        self.dic['file_recommender'] = None
        self.dic['folder_output'] = None
        self.dic['feature_extraction'] = False
        self.dic['feature_users'] = False
        self.dic['feature_items'] = False
        self.dic['quality_analysis'] = False
        self.dic['mae_mse_accuracy'] = False
        self.dic['precision_recall'] = False
        self.dic['diversity_novelty'] = False
        self.dic['genre_coverage'] = False
        self.dic['catalog_coverage'] = False
        self.dic['serendipity'] = False

    def __getitem__(self, key):
        return self.dic[key]
