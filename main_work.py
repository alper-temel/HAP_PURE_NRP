class HAP_NRP:
    def __init__(self, performans_data, analiz_data, kullanim_tarzi = str, basamak = int, treshold = float, state = int, nrp_ratio = float, numberOfValue = int):
        self.performans_data = performans_data
        self.analiz_data = analiz_data
        self.kullanim_tarzi = kullanim_tarzi
        self.basamak = basamak
        self.treshold = treshold
        self.state = state
        self.nrp_ratio = nrp_ratio
        self.numberOfValue = numberOfValue
        self.hasar_tutar_analiz = self.analiz_data.columns[len(self.analiz_data.columns) - 1]
        self.hasar_tutar_performans = self.performans_data.columns[len(self.performans_data.columns) - 1]
        self.freq = self.analiz_data.columns[len(self.analiz_data.columns) - 2]
        self.policy_count = self.analiz_data.columns[len(self.analiz_data.columns) - 3]
    def preprocessing_performans(self):
        data = self.performans_data
        if self.kullanim_tarzi == "otomobil":
            data = data.loc[data["ADL_KULLANIM_TARZI"] == "OTOMOBİL"]
        elif self.kullanim_tarzi == "camlıvan":
            data = data.loc[data["ADL_KULLANIM_TARZI"] == "CAMLIVAN"]
        elif self.kullanim_tarzi == "panelvan":
            data = data.loc[data["ADL_KULLANIM_TARZI"] == "PANELVAN"]
        elif self.kullanim_tarzi == "kamyonet":
            data = data.loc[data["ADL_KULLANIM_TARZI"] == "KAMYONET"]
        elif self.kullanim_tarzi == "pick-up":
            data = data.loc[data["ADL_KULLANIM_TARZI"] == "PICK-UP"]
        elif self.kullanim_tarzi == "suv":
            data = data.loc[data["ADL_KULLANIM_TARZI"] == "SUV"]
        data = data.loc[data["BASAMAK"] == self.basamak]
        data = data.drop(["ADL_KULLANIM_TARZI", "BASAMAK"], axis = 1)
        return data
    def preprocessing_analiz(self):
        data = self.analiz_data
        if self.kullanim_tarzi == "otomobil":
            data = data.loc[data["ADL_KULLANIM_TARZI"] == "OTOMOBİL"]
        elif self.kullanim_tarzi == "camlıvan":
            data = data.loc[data["ADL_KULLANIM_TARZI"] == "CAMLIVAN"]
        elif self.kullanim_tarzi == "panelvan":
            data = data.loc[data["ADL_KULLANIM_TARZI"] == "PANELVAN"]
        elif self.kullanim_tarzi == "kamyonet":
            data = data.loc[data["ADL_KULLANIM_TARZI"] == "KAMYONET"]
        elif self.kullanim_tarzi == "pick-up":
            data = data.loc[data["ADL_KULLANIM_TARZI"] == "PICK-UP"]
        elif self.kullanim_tarzi == "suv":
            data = data.loc[data["ADL_KULLANIM_TARZI"] == "SUV"]
        data = data.loc[data["BASAMAK"] == self.basamak]
        data = data.drop(["BASAMAK"], axis = 1)
        data = data.drop(["ADL_KULLANIM_TARZI"], axis = 1)
        return data
    def double_combinations(self):
        """
        ikili combinasyonlar oluştur
        """
        from sklearn.utils import shuffle
        data = HAP_NRP(self.performans_data, self.analiz_data, self.kullanim_tarzi, self.basamak, self.treshold, self.state, self.nrp_ratio).preprocessing_performans()
        cols_all = list(data.columns[0:len(data.columns) - 2])
        cols_all = shuffle(cols_all)
        cols = []
        for i in cols_all:
            if i not in cols:
                cols.append(i)
                if len(cols) >= self.state:
                    break
        combinations = list(itertools.combinations(cols, 2))
        doubles = []
        for i in combinations:
            a = pd.Series(np.unique(data[i[0]]))
            b = pd.Series(np.unique(data[i[1]]))
            doubles.append(list(itertools.product(a, b)))
        doubles_ = []
        rules = []
        for i, combonation in zip(doubles, combinations):
            k = 0
            while True:
                for j in i:
                    doubles_.append(j)
                    rules.append(combonation)
                    k += 1
                if k >= len(i):
                    break
        double_combinations = pd.DataFrame()
        double_combinations["Başlık"] = rules
        double_combinations["Kombinasyon"] = doubles_
        return double_combinations
    def triple_combinations(self):
        """
        üçlü kombinasyonlar oluştur
        """
        from sklearn.utils import shuffle
        data = HAP_NRP(self.performans_data, self.analiz_data, self.kullanim_tarzi, self.basamak, self.treshold, self.state, self.nrp_ratio).preprocessing_performans()
        cols_all = list(data.columns[0:len(data.columns) - 2])
        cols_all = shuffle(cols_all)
        cols = []
        for i in cols_all:
            if i not in cols:
                cols.append(i)
                if len(cols) >= self.state:
                    break
        combinations = list(itertools.combinations(cols, 3))
        triples = []
        for i in combinations:
            a = pd.Series(np.unique(data[i[0]]))
            b = pd.Series(np.unique(data[i[1]]))
            c = pd.Series(np.unique(data[i[2]]))
            triples.append(list(itertools.product(a, b, c)))
        triples_ = []
        rules = []
        for i, combonation in zip(triples, combinations):
            k = 0
            while True:
                for j in i:
                    triples_.append(j)
                    rules.append(combonation)
                    k += 1
                if k >= len(i):
                    break
        triple_combinations = pd.DataFrame()
        triple_combinations["Başlık"] = rules
        triple_combinations["Kombinasyon"] = triples_
        return triple_combinations
    def calculate_nrp(self):
        """
        performans ve analiz verisinden ikili ve üçlü nrp'leri hesapla
        """
        performans_data = HAP_NRP(self.performans_data, self.analiz_data, self.kullanim_tarzi, self.basamak, self.treshold, self.state, self.nrp_ratio).preprocessing_performans()
        analiz_data = HAP_NRP(self.performans_data, self.analiz_data, self.kullanim_tarzi, self.basamak, self.treshold, self.state, self.nrp_ratio).preprocessing_analiz()
        double = HAP_NRP(self.performans_data, self.analiz_data, self.kullanim_tarzi, self.basamak, self.treshold, self.state, self.nrp_ratio).double_combinations()
        triple = HAP_NRP(self.performans_data, self.analiz_data, self.kullanim_tarzi, self.basamak, self.treshold, self.state, self.nrp_ratio).triple_combinations()
        
        # // PERFORMANS NRP'LERİNİ HESAPLAMAK
        
        ikili_nrp_performans = []
        ikili_kaz_adet_performans = []
        for i, j in zip(double["Başlık"], double["Kombinasyon"]):
            try:
                df = performans_data.loc[performans_data[i[0]] == j[0]]
                df = df.loc[df[i[1]] == j[1]]
                df["İlk_Nrp"] = df[self.hasar_tutar_performans] * self.nrp_ratio
                nrp_ = np.ma.average(a = df["İlk_Nrp"], weights = df[self.policy_count])
                ikili_nrp_performans.append(nrp_)
                ikili_kaz_adet_performans.append(self.numberOfValue + 1)
            except:
                ikili_nrp_performans.append(0)
        double["NRP_performans"] = ikili_nrp_performans
        double["Kırılım_Adet"] = ikili_kaz_adet_performans
        
        uclu_nrp_performans = []
        uclu_kaz_adet_performans = []
        for i, j in zip(triple["Başlık"], triple["Kombinasyon"]):
            try:
                df = performans_data.loc[performans_data[i[0]] == j[0]]
                df = df.loc[df[i[1]] == j[1]]
                df = df.loc[df[i[2]] == j[2]]
                df["İlk_Nrp"] = df[self.hasar_tutar_performans] * self.nrp_ratio
                nrp_ = np.ma.average(a = df["İlk_Nrp"], weights = df[self.policy_count])
                uclu_nrp_performans.append(nrp_)
                uclu_kaz_adet_performans.append(self.numberOfValue + 1)
            except:
                uclu_nrp_performans.append(0)
        triple["NRP_performans"] = uclu_nrp_performans
        triple["Kırılım_Adet"] = uclu_kaz_adet_performans
        
        performans_nrp = pd.concat([double, triple], axis = 0)
        
        # // 
        
        # // ANALİZ NRP'LERİNİ HESAPLAMAK
        
        ikili_nrp_analiz = []
        ikili_kaz_adet_analiz = []
        for i, j in zip(double["Başlık"], double["Kombinasyon"]):
            try:
                df = analiz_data.loc[analiz_data[i[0]] == j[0]]
                df = df.loc[df[i[1]] == j[1]]
                nrp_ = df[self.hasar_tutar_analiz].sum() / df[self.policy_count].sum()
                #df["Şiddet"] = df[self.hasar_tutar_analiz] * df[self.freq]
                #nrp_ = np.ma.average(a = df["Şiddet"], weights = df[self.policy_count])
                ikili_nrp_analiz.append(nrp_)
                ikili_kaz_adet_analiz.append(df[self.policy_count].sum())
            except:
                ikili_nrp_analiz.append(0)
        double["NRP_analiz"] = ikili_nrp_analiz
        double["Kırılım_Adet"] = ikili_kaz_adet_analiz
        
        uclu_nrp_analiz = []
        uclu_kaz_adet_analiz = []
        for i, j in zip(triple["Başlık"], triple["Kombinasyon"]):
            try:
                df = analiz_data.loc[analiz_data[i[0]] == j[0]]
                df = df.loc[df[i[1]] == j[1]]
                df = df.loc[df[i[2]] == j[2]]
                nrp_ = df[self.hasar_tutar_analiz].sum() / df[self.policy_count].sum()
                #df["Şiddet"] = df[self.hasar_tutar_analiz] * df[self.freq]
                #nrp_ = np.ma.average(a = df["Şiddet"], weights = df[self.policy_count])
                uclu_nrp_analiz.append(nrp_)
                uclu_kaz_adet_analiz.append(df[self.policy_count].sum())
            except:
                uclu_nrp_analiz.append(0)
        triple["NRP_analiz"] = uclu_nrp_analiz
        triple["Kırılım_Adet"] = uclu_kaz_adet_analiz
        
        analiz_nrp = pd.concat([double, triple], axis = 0)
        
        # //
        
        nrp_df = pd.concat([performans_nrp, analiz_nrp], axis = 0)
        nrp_df = nrp_df.dropna()
        nrp_df["NRP_Fark"] = nrp_df["NRP_performans"] / nrp_df["NRP_analiz"]
        nrp_df = nrp_df.loc[nrp_df["NRP_Fark"] >= self.treshold]
        nrp_df = nrp_df.loc[nrp_df["Kırılım_Adet"] >= self.numberOfValue]
        
        return nrp_df
