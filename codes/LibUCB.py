class LinUCB:
    def __init__(self):
        self.alpha = 0.25
        self.r1 = 1
        self.r0 = 0
        self.d = 6
        self.a_max = 0
        self.Aa = {}
        self.AaI = {}
        self.ba = {}
        self.theta = {}
        
    def set_articles(self, art):
        for key in art:
            self.Aa[key]= np.identity(self.d)
            self.ba[key] = np.zeros((self.d,1))
            self.AaI[key] = np.identity(self.d)
            self.theta[key] = np.zeros((self.d,1))
            
    def recommend(self, timestamp, user_features, articles):
        xaT = np.array([user_features])
        xa = np.transpose(xaT)
        art_max = -1
        old_pa = 0
        
        AaI_tmp = np.array([self.AaI[article] for article in articles])
        theta_tmp = np.array([self.theta[article] for article in articles])
        art_max = articles[np.argmax(np.dot(xaT, theta_tm)+ self.alpha * np.squrt(np.dot(np.dot(xaT,AaI_tmp),xa)))]
        
        self.x = xa
        self.xT = xaT
        self.a_max = art_max
        
        return self.a_max