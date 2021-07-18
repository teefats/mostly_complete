def matrix_mul(A, B):
     matrix=[]
     def multiply_line_by(line,column):
          try:
               sizeLine=len(line)
               sizeColumn=len(column)
               if(sizeLine!=sizeColumn):
                    raise ValueError("Exception")
               res = sum([line[i] * column[i] for i in range(sizeLine)])
               return res
          except ValueError:
               print("The columns and lines must be equal in number")

     def  getColumn(matrix,numColumn):
          size=len(matrix)
          column= [matrix[i][numColumn] for i in range(size)]
          return column

     def getLine(matrix,numLine):
          line = matrix[numLine]
          return line

     for i in range(len(A)):
          matrix.append([])
          for j in range(len(B)):
               matrix[i].append(multiply_line_by(getLine(A,i),getColumn(B,j)))

     print(matrix) 

matrix_mul(A,B)