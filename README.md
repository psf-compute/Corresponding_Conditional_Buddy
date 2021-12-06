# Corresponding Conditional Buddy
This program checks the validity or invalidity of every argument in propositional logic, by expoiting a feature of an argument's corresponding conditional.
</br>


<h2>Quick Logic Refresher</h2>
<h4>Conditionals</h4>

As you may know, in standand propositional logic, a conditional is true, either when its antecedent is false or when its consequent is true. Otherwise, it's false (i.e. when it's antecedent is true but its consequent is false). 

<h4>Logical Validity</h4>

An argument is said to be valid whenever it's not possible for its premises to true but its conclusion false.

<h4>Logical Truth</h4>

A statement is a logical truth whenever it's impossible to be false. On a truth table, the statement has true in every row. 

<h4>Corresponding Conditionals</h4>

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

<h4>How to use this Program </h4>

So, lol, this might be a bit hard on the eyes, but it's doable. I'll walk you through it.

Preface: I'm going to assume that you're going to use IDLE for everything. 

Firstly, open CorConPy.py in IDLE.

Next, make a set for your truth values for each of your variables. Make the one that would represent your conclusion false, but change them up for each iteration that you run the program. Here's an example: tv = {"A": False, "B": True}

Next, every statement variable you choose has to be put inside Var(). So, if your statement is "A", you'll put Var("A"). 

Next, let's try negation. It's a unary operator, so it takes only one input (technically, the correct word here is "argument," but I chose to say "input," since we're already using the word "argument" for something else). To negate A, you'll put Neg(Var("A")). 

Next, let's try disjunction. It's a binary operator, so it takes two inputs. To say A and B, you'll put Conj(Var("A"),Var("B")).

Next, to speed things up a bit, the same process applies to the other operators, since they're all binary operators. The only thing that changes, obviously, is the function name for the operator. For implications/conditionals use Imp, for conjunctions use Conj, and for biconditionals use Bic. 

Next, combine all of that to form an argument into its corresponding conditional. Keep track of the parentheses!

Lastly, save an run it.

<h2>How to use this Program </h2>

Let's use a modus tollens again. Here's its corresponding conditional: ((A implies B) and not B) implies not A. 

Here's how it would look like in this program: Imp(Conj(Imp(Var("A"),Var("B")), Neg(Var("B"))), Neg(Var("A")))

Here are some tips to construct an argument's corresponding conditional. 

1. Count the number of left and right parenthesis; if the number is equal, then you probably won't throw a parenthesis error; otherwise, you will.

2. Notice that you're nesting a function. Start with the first premise. Then use the conjuction  operator, with everything you put for the first premise as it's first conjuction. Keep nesting things up until you've constructed the corresponding conditional.

3. You can run the program to output each nested part, as it will output a well-formed formula, if you've made one. Otherwise, an error will occur.

4. Last, but not least, you can assign a lot of the code to different variables. 

Example: using the code from above: Imp(Conj(Imp(Var("A"),Var("B")), Neg(Var("B"))), Neg(Var("A"))), we can simplify it like this:
not_A = Neg(Var("A"))
not_B = Neg(Var("B"))
A = Var("A")
B = Var("B")

Imp(Conj(Imp(A, B), not_B), not_A)

You could assign more parts of this, if you so desire.  

<h2>How to Use This Program using IDLE</h2>

Step 1. Save the program anywhere in your filesystem.

Step 2. Open IDLE and then, at the top, go to File, Open, and then go to where you saved the program, and then select it.

Step 3. At the bottom, under the comment that starts with "# reproduce your argument here" type out your argument's corresponding conditional, as per the grammatical structure above. 

Step 4. Change the truth values in the tv set. Consider, for example, setting the variable that represents your conclusion as False. 

Step 5. Press Run at the top. 

Step 6. If the syntax is correct, you should get a “your argument may be valid” or “your argument is invalid” as the output.  

Step 7: Repeat steps 4 to 7. If you get an invalid, that determines that your argument is invalid and you may stop using the program. Until you exhaust all possible truth values for each variable, and if they call come out as “your argument may be valid” you’ll know that the argument is actually valid. 


<h2> Conclusion </h2>

That's basically it. Enjoy!
