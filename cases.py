import frameworks

class DefaultTest(frameworks.PNGs):
    def equality(self):
        pass

class MyTest1(frameworks.PNGs):
    def histogram_cmp_corr(self):
        pass

    def equality(self):
        pass

class MyTest2(frameworks.PNGs):
    def histogram_cmp_bhatta(self):
        pass

