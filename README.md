# Corresponding_Conditional_Buddy
This program checks the validity or invalidity of every argument in propositional logic, by expoiting a feature of an argument's corresponding conditional.

So, I'll keep this brief. 

<h3>Quick Logic Refresher</h3>
<h5>Conditionals</h5>

As you may know, in standand propositional logic, a conditional is true, either when its antecedent is false or when its consequent is true. Otherwise, it's false (i.e. when it's antecedent is true but its consequent is false). 

<h5>Logical Validity</h5>

An argument is said to be valid whenever it's not possible for its premises to true but its conclusion false.

<h5>Logical Truth</h5>

A statement is a logical truth whenever it's impossible to be false. 

<h5>Corresponding Conditionals</h5>

Lastly, every argument has what's called a "corresponding conditional." If the argument is valid, it's corresponding conditional is a logical truth. Otherwise, it's not.

<h3>What this Program Does</h3>
Basically, what my argument does is allow you to input the corresponding conditional of your argument, in Python, and check if it's valid. The way to do this is to make one of the truth values of your premises false. If your argument is valid, a false premise will not affect the truth value of your argument's corresponding conditional; the corresponding conditional will still come out as true, which establishes your argument's validity. 

In case your argument's corresponding conditional comes out false, then that establishes your argument's invalidity.

  
