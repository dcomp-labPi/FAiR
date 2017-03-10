class CalcLoader:
    def __init__(self, window):
        count_weight = 0
        self.loader_window = window.loader_window

        if window.parameters.dic['file_train']:
            count_weight += 1
        if window.parameters['file_test'] and (window.parameters.dic['quality_analysis']
                                               or window.parameters.dic['catalog_coverage']):
            count_weight += 1
        if window.parameters.dic['feature_extraction'] or (window.parameters.dic['quality_analysis']
                                                       or window.parameters.dic['catalog_coverage']
                                                       or window.parameters.dic['genre_coverage']):
            count_weight += 2

        # for all recommendations
        if window.parameters.dic['file_recommender'] and (window.parameters.dic['quality_analysis']
                                                      or window.parameters.dic['catalog_coverage']
                                                      or window.parameters.dic['serendipity']
                                                      or window.parameters.dic['genre_coverage']):
            for j in range(len(window.parameters.dic['file_recommender'])):
                count_weight += 1
                if window.parameters.dic['quality_analysis']:
                    count_weight += 3
                if window.parameters.dic['diversity_novelty']:
                    count_weight += 3
                if window.parameters.dic['genre_coverage']:
                    count_weight += 2
                if window.parameters.dic['catalog_coverage']:
                    count_weight += 2
                if window.parameters.dic['serendipity']:
                    count_weight += 3

        self.value = (100 / float(count_weight)) / float(100)

    def set_process(self, weight, text):
        if self.loader_window.getStatus() < 0.25:
            self.loader_window.setStatus(weight * self.value)
        else:
            self.loader_window.setStatus((weight * self.value) - 0.05)
        self.loader_window.setText(text)

    def finish_process(self):
        self.loader_window.setStatus(1)
        self.loader_window.setText('Finish Him')
