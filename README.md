# Corresponding_Conditional_Buddy
This program checks the validity or invalidity of every argument in propositional logic, by expoiting a feature of an argument's corresponding conditional.
</br>


<h3>Quick Logic Refresher</h3>
<h5>Conditionals</h5>

As you may know, in standand propositional logic, a conditional is true, either when its antecedent is false or when its consequent is true. Otherwise, it's false (i.e. when it's antecedent is true but its consequent is false). 

<h5>Logical Validity</h5>

An argument is said to be valid whenever it's not possible for its premises to true but its conclusion false.

<h4>Logical Truth</h4>

A statement is a logical truth whenever it's impossible to be false. On a truth table, the statement has true in every row. 

<h4>Corresponding Conditionals</h5>

Lastly, every argument has what's called a "corresponding conditional." If the argument is valid, it's corresponding conditional is a logical truth. Otherwise, it's not.

Let's condider a modus tollens argument. 

1. A implies B.
2. Not B.
3. Not A.

Its corresponding conditional is: ((A implies B) and not B) implies not A. 

<h4>What this Program Does</h4>
Basically, what my argument does is allow you to input the corresponding conditional of your argument, in Python, and check if it's valid. The way to do this is to make one of the truth values of your premises false. If your argument is valid, a false premise will not affect the truth value of your argument's corresponding conditional; the corresponding conditional will still come out as true, which establishes your argument's validity.</br>
</br>
In case your argument's corresponding conditional comes out false, then that establishes your argument's invalidity.

<h5>How to use this Program </h5>
So, lol, this might be a bit hard on the eyes, but it's doable. I'll walk you through it. 

First, make a set for your truth values for each of your variables. Make the one that would represent your conclusion false, but change them up for each iteration that you run the program. Here's an example: tv = {"A": False, "B": True}

Next, every statement variable you choose has to be put inside Var(). So, if your statement is "A", you'll put Var("A"). 

Next, let's try negation. It's a unary operator, so it takes only one input (technically, the correct word here is "argument," but I chose to say "input," since we're already using the word "argument" for something else). To negate A, you'll put Neg(Var("A")). 

Next, let's try disjunction. It's a binary operator, so it takes two inputs. To say A and B, you'll put Conj(Var("A"),Var("B")).

Next, to speed things up a bit, the same process applies to the other operators. 






  
