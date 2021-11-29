class SingleCell:

    def __init__(self,Row,Column,Value):
        self.RowColumn=((Row+1),(Column+1))
        self.RowColumnIndex=(Row,Column)
        self.Value=Value