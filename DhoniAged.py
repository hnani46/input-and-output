...
MS Dhoni aged X years, is a Cancerian, born with very strong Mars in his birth chart. Notably, Mars is the ruling planet for sports. Write a program to get the age of Dhoni as an integer and display the same.
Input Format:
Input is an integer that corresponds to the age of Dhoni.
Output Format:
Display the age.
Refer sample Input and Output for formatting specifications.
[All the text in bold corresponds to the Input]
Sample Input and Output:
Enter the age:
35
Age of Dhoni is 35
...
a=int(input())
print("Age of Dhoni is",a)
program....
 
def get_dhoni_age():
    try:
        # Input age
        age = int(input("Enter MS Dhoni's age in years: "))
        print(f"MS Dhoni is {age} years old.")
    except ValueError:
        print("Please enter a valid integer.")

get_dhoni_age()
output....
 Enter MS Dhoni's age in years: 45
MS Dhoni is 45 years old.
