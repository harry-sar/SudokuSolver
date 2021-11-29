#!/usr/bin/python

import argparse
import sys,Cell

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
            print("Result:")
            self.PrintGrid(Grid)
        else:
            print("No Solutioon for problem")


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Sudoku Solver')
    parser.add_argument('Size', type=int,
                        help='An integer representing the Grid Size e.g (9x9)')
    parser.add_argument('Length', type=str,
                        help='An 81 Character String going Row-Row -->> where its the starter values for the Puzzle')
    args = parser.parse_args()
    SolveMe=SudokuSolver(args.Size,args.Length)
    SolveMe.Start_Solve(SolveMe.Grid)





