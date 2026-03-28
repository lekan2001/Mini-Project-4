import math as guru
class MonsterClassificationAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        self.fctotrsThatDfineAMonstre = {
            #I will defnemy params and diff valuus dfine what a msonter is
            'size': ['tiny', 'small', 'medium', 'large', 'huge'],
            'color': ['black', 'white', 'brown', 'gray', 'red', 'yellow',
                       'blue', 'green', 'orange', 'purple'],
            'covering': ['fur', 'feathers', 'scales', 'skin'],
            'foot-type': ['paw', 'hoof', 'talon', 'foot', 'none'],
            'leg-count': [0, 1, 2, 3, 4, 5, 6, 7, 8],
            'arm-count': [0, 1, 2, 3, 4, 5, 6, 7, 8],
            'eye-count': [0, 1, 2, 3, 4, 5, 6, 7, 8],
            'horn-count': [0, 1, 2],
            'lays-eggs': [True, False],
            'has-wings': [True, False],
            'has-gills': [True, False],
            'has-tail': [True, False]
        }
        self.paraAmMs = list(self.fctotrsThatDfineAMonstre.keys())
        

    def solve(self, samples, new_monster):

        muPArams = self.paraAmMs

        for x, y in samples:
            is_A_Mnos_match = True
            for a in muPArams:
                if x[a] != new_monster[a]:
                    is_A_Mnos_match = False
                    break
            if is_A_Mnos_match:
                return y
            
        goDPoSSsamops = []
        badDNeGGSamps = []

        if len(goDPoSSsamops) == 0:
            return False
        if len(badDNeGGSamps) == 0:
            return True
        
        for x, y in samples:
            if y:
                goDPoSSsamops.append(x)
            else:
                badDNeGGSamps.append(x)
        
        comP_ofValsues4Posts = {}
        for x in muPArams:
            psramss_4Valss = set()
            for y in goDPoSSsamops:
                psramss_4Valss.add(y[x])
            comP_ofValsues4Posts[x] = psramss_4Valss

        logicALLYExcldedDatDFier = {}
        for x in muPArams:
            logicALLYExcldedDatDFier[x] = set()

        for y_Neggs in badDNeGGSamps:
            differnTnPAramss = []
            for z in muPArams:
                if y_Neggs[z] not in comP_ofValsues4Posts[z]:
                    differnTnPAramss.append(z)
            if len(differnTnPAramss) == 1:
                exClddedPrams = differnTnPAramss[0]
                xCludedDValss = y_Neggs[exClddedPrams]
                logicALLYExcldedDatDFier[exClddedPrams].add(xCludedDValss)
        
        a = 0.5
        numOfPoss = len(goDPoSSsamops)
        numOFFNegss = len(badDNeGGSamps)
        toTTNUmsS = numOfPoss + numOFFNegss

        fndLogOFPrevPosProbsss = guru.log(numOfPoss / toTTNUmsS)
        fndLoggofnegatvePrevProbabilttes = guru.log(numOFFNegss / toTTNUmsS)

        for my_P in muPArams:
            vls = new_monster[my_P]
            Monsfctors_Size = len(self.fctotrsThatDfineAMonstre[my_P])


            if vls in logicALLYExcldedDatDFier[my_P]:
                fndLogOFPrevPosProbsss = fndLogOFPrevPosProbsss + guru.log(0.001)

                cnts_OFNegss = 0

                for x in badDNeGGSamps:
                    if x[my_P] == vls:
                        cnts_OFNegss = cnts_OFNegss + 1

                neg_PRobsn = (cnts_OFNegss + a) / (numOFFNegss + a * Monsfctors_Size)
                fndLoggofnegatvePrevProbabilttes = fndLoggofnegatvePrevProbabilttes + guru.log(neg_PRobsn)
                continue
            cnTOFPsotveExamples = 0

            for x_PosMons in goDPoSSsamops:
                if x_PosMons[my_P] == vls:
                    cnTOFPsotveExamples = cnTOFPsotveExamples + 1

            cont_0FNeg = 0
            for x in badDNeGGSamps:
                if x[my_P] == vls:
                    cont_0FNeg = cont_0FNeg + 1
            """Fnd the pssosbile likehoos orf bth positive and negs"""
            p0sLiklih00dnes = (cnTOFPsotveExamples + a) / (numOfPoss + a * Monsfctors_Size)
            likL1h00dnessOFNegs = (cont_0FNeg + a) / (numOFFNegss + a * Monsfctors_Size)

            """get lograthmic likelih00dnesso postives and negatves"""

            fndLogOFPrevPosProbsss = fndLogOFPrevPosProbsss + guru.log(p0sLiklih00dnes)
            fndLoggofnegatvePrevProbabilttes = fndLoggofnegatvePrevProbabilttes + guru.log(likL1h00dnessOFNegs)
        
        if fndLogOFPrevPosProbsss >= fndLoggofnegatvePrevProbabilttes:
            return True
        else:
            return False













        

        #Add your code here!
        #
        #The first parameter to this method will be a labeled list of samples in the form of
        #a list of 2-tuples. The first item in each 2-tuple will be a dictionary representing
        #the parameters of a particular monster. The second item in each 2-tuple will be a
        #boolean indicating whether this is an example of this species or not.
        #
        #The second parameter will be a dictionary representing a newly observed monster.
        #
        #Your function should return True or False as a guess as to whether or not this new
        #monster is an instance of the same species as that represented by the list.
    