[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=341478&assignment_repo_type=GroupAssignmentRepo)
# Group-Assignment

**Group Members:  Mustafa Ikbal Mehmedoglu, Furkan Enes Celtik, Umut Baris Basol, Kerem Gurses**

**We chose Strategy and Flyweight patterns to code for this assignment. We used those patterns for two seperate problems.**

# For Strategy Pattern:

We designed a 100 meters running simulation. In this application, we have two different players who chooses 
from variety of strategies (randomized in this case) to win the race. We selected the Strategy Pattern because 
otherwise, any change to the algorithms, whether it was a simple bug fix or a slight adjustment, would affect the whole class, 
increasing the chance of creating an error in already-working code. 

The Runner is not responsible for selecting an appropriate algorithm for the job. Instead, the client passes the randomized strategy 
to the context. In fact, the Runner does not know much about strategies. It works with all strategies through the same generic interface.

This way the Runner becomes independent of concrete strategies, so you can add new algorithms or modify existing ones without 
changing the code of the Runner or other strategies.

# For Flyweight Pattern:

We created a simulation of a sports application based in Turkey called 'Mackolik'. This app stores information on different sportspeople.

In our Flyweight pattern program, we create Flyweight objects with two types of information; these being common information and personal information.
In our case, common information is used as a key in updating and creating players, and personal information is used to store additional information
about the player. 

Common information of the player is used to compare values in the database, if there is a player with such information, then personal information 
can be bound to a player that already exists in the database. If not, then a player with the specified common and personal information will be created 
and added to the database. 

Since common information cannot be the same in two players, we can ensure that there will be no duplicates and we can safely add new players 
to the database. Because common information will not change from system to system, this program will be able to run on any specified device.

**For additional information refer to our comments in both of the codes.**
