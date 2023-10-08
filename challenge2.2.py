class Batsman:
    def _init_(self):
        self.strike_rate = 0.0
        self.total_runs = 0
        self.highest_score = 0
        self.batting_rank = 0
    def get_bat(self,sr,tr,hs,br):
        self.strike_rate = sr
        self.total_runs = tr
        self.highest_score = hs
        self.batting_rank = br
    def disp_bat(self):
        print "\nBATTING DATA\n"
        print "Strike Rate:",self.strike_rate
        print "Total Runs:",self.total_runs
        print "Highest Score:",self.highest_score
        print "Batting Rank:",self.batting_rank      

class Bowler:
    def _init_(self):
        self.wickets_taken = 0
        self.economy = 0.0
        self.hattricks = 0
        self.bowling_rank = 0
    def get_bowl(self,wt,ec,ht,bor):
        self.wickets_taken = wt
        self.economy = ec
        self.hattricks = ht
        self.bowling_rank = bor
    def disp_bowl(self):
        print "\nBOWLING DATA\n"
        print "Wickets Taken:",self.wickets_taken
        print "Economy:",self.economy
        print "Hattricks:",self.hattricks
        print "Bowling Rank:",self.bowling_rank

class AllRounder(Batsman,Bowler):
    def _init_(self):
        Batsman._init_(self)
        Bowler._init_(self)
        self.allrounder_rank = 0
    def get_all(self,sr,tr,hs,br,wt,ec,ht,bor,ar):
        Batsman.get_bat(self,sr,tr,hs,br)
        Bowler.get_bowl(self,wt,ec,ht,bor)
        self.allrounder_rank = ar
    def disp_all(self):
        print "\nALL-ROUNDER DATA"
        print "\nAll-Rounder Rank:",self.allrounder_rank
        self.disp_bat()
        self.disp_bowl()

player1 = AllRounder()
player1.get_all(89.7,3024,96,67,101,5.67,4,34,57)
player1.disp_all()
