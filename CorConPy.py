#this program will  establish the validity every argument in propositional logic

# the class defines expressions. 
class Expr:
   pass

# creates a binary operator class that inherents from Expr.
class binOp(Expr):
     def __init__(self, left, right):
        self.left = left
        self.right = right 


# creates a disjunctive operator class. It's a sub-class of binOp. 

#The left and right have been coerced to a string. We have concatenated the operator, too. All of this permits recursion to occur, regardless of whether one of the sides are a  value or an operator.

#Similar considerations for the other operators.

class Disj(binOp):
    def __str__(self):
     return "("+str(self.left)+ " v " + str(self.right)+")"

# this evalutes what's input into Disj from the supplied dictionary. Each operator has a version of this.

    def eval(self,tv):
       return self.left.eval(tv) or self.right.eval(tv)



class Neg(Expr):
    def __init__(self, left):
        self.left = left
        
    def __str__(self):
     return "~"+str(self.left)
     
    def eval(self,tv):
       return not(self.left.eval(tv))

        
class Conj(binOp):
   def __str__(self):
     return "("+str(self.left)+ " & " + str(self.right)+")"

   def eval(self,tv):
       return self.left.eval(tv) and self.right.eval(tv)

class Imp(binOp):

     def __str__(self):
       return "("+str(self.left)+ " ⊃ " + str(self.right)+")"

   # 'if p then q'' is logically equivalent to 'not-p or q'

     def eval(self,tv):
       return (not(self.left.eval(tv)) or self.right.eval(tv))


class Bic(binOp):
     def __str__(self):
       return "("+str(self.left)+ " ≡ " + str(self.right)+")"

     def eval(self,tv):
         return ((self.left.eval(tv)) and (self.right.eval(tv))) or (not(self.left.eval(tv)) and not (self.right.eval(tv)))



class Var(binOp):
   def __init__(self,name):
         self.name = name

   def __str__(self):
       return self.name
       
   def eval(self,tv):
       return tv[self.name]
       
 
#tv for truth value

#Whatever variable your conclusion is, make it false, unless it's a negation (make it true then). If your argument is valid, no matter what, its corresponding conditional will come out true; otherwise, false.

tv = {"A": False, "B": True}


# reproduce your argument here, as it’s corresponding conditional, using the appropriate operators above, and by inputting  your dictionary keys into Var([key]). 

# the sample argument is an invalid argument.
       
x= Imp(Conj(Imp(Var("A"), Var("B")), (Var("B"))), (Var("A")))


print(x)

#evaluates tv
y = x.eval(tv)

print(y)

if y:
   print("Your argument may be valid.")
else:
   print("Your argument is invalid.")
