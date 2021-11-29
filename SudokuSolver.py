import Cell

class SudokuSolver:

    def __init__(self,GridSize,SequenceOfNumbersRow):
        self.SequenceOfNumbersRow=SequenceOfNumbersRow
        self.GridSize=GridSize
        self.Grid=self.InitalizeGrid(GridSize,SequenceOfNumbersRow)

    def InitalizeGrid(self,GridSize,SequenceOfNumbersRow):
        Grid = []
        GridTemp=[]
        SeqTempList=[]
        SequenceList=[]
        for ind,let in enumerate(SequenceOfNumbersRow):
            SeqTempList.append(let)
            if (ind+1)%GridSize==0:
                SequenceList.append(SeqTempList)
                SeqTempList=[]

        for i in range(GridSize):
            Grid.append(["0"] * GridSize)
        GridTemp=Grid

        for RowIndex,Row in enumerate(GridTemp):
            for ColumnIndex,Column in enumerate(Row):
                Grid[RowIndex][ColumnIndex]=(Cell.SingleCell(RowIndex,ColumnIndex,int(SequenceList[RowIndex][ColumnIndex])))
        return Grid

    def PrintGrid(self,Grid):
        PrintG=""
        for x in Grid:
            for y in x:
                PrintG+=(" ".join(str(y.Value))+" ")
            print(PrintG)
            PrintG=""

    def SafeToMove(self,Grid,Row,Column,AssignedNumber):
        for x in range(self.GridSize):
            if Grid[Row][x].Value == AssignedNumber:
                return False

        for x in range(self.GridSize):
            if Grid[x][Column].Value == AssignedNumber:
                return False

        startRow = Row - Row % 3
        startCol = Column - Column % 3

        for i in range(3):
            for j in range(3):
                if Grid[i + startRow][j + startCol].Value == AssignedNumber:
                    return False
        return True

    def Solver(self,Grid,Row,Column):

        if (Row == self.GridSize - 1 and Column == self.GridSize):
            return True

        if Column == self.GridSize:
            Row += 1
            Column = 0

        if Grid[Row][Column].Value > 0:
            return self.Solver(Grid, Row, Column + 1)

        for num in range(1, self.GridSize + 1, 1):
            if self.SafeToMove(Grid, Row, Column, num):
                Grid[Row][Column].Value = num

                if self.Solver(Grid, Row, Column + 1):
                    return True
            Grid[Row][Column].Value = 0
        return False

    def Start_Solve(self,Grid):
        if self.Solver(Grid,0,0):
            self.PrintGrid(Grid)
        else:
            print("No Solutioon for problem")

# Test=SudokuSolver(9,"001734000097000084006000500400100020000070300050069008000200000629800010800500096")


SolveMe=SudokuSolver(9,"000003100693001020512009000000000094021704580340000000000100978050800341008900000")
SolveMe.Start_Solve(SolveMe.Grid)





