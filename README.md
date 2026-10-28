# MET-CS526

PROBLEM 1:

Algorithm: The algorithm checks every possible group of three consecutive days to see if the snowfall during those days is more than half of the total snowfall. Since the input has the cumulative snowfall totals, I calculate the snowfall for three days by subtracting the cumulative total from before those days. For the first three days, I use the third value because there is no earlier total I can subtract. The program compares each result with half of the total snowfall. If one group has strictly more than half of the total, it returns YES. If none of the groups meet this condition, it returns NO. If there are fewer than three days, it also returns NO. This works well because the cumulative totals let me calculate the snowfall for each group using subtraction instead of adding the snowfall from three separate days. The program checks each group and stops as soon as it finds one that meets the condition.

How to run the program: I ran the commands below in the terminal from my Midterm CS526 folder. I ran all five input files. The first four results matched the expected answers from the assignment, and the fifth returned YES. The example outputs are saved in outputs/snowfall_output.txt, showing the results for each of the input files. 

Commands: 

python snowfall.py "Input files\snowfall_input1.txt"

python snowfall.py "Input files\snowfall_input2.txt"

python snowfall.py "Input files\snowfall_input3.txt"

python snowfall.py "Input files\snowfall_input4.txt"

python snowfall.py "Input files\snowfall_input5.txt"




PROBLEM 2:

Algorithm: The algorithm simulates the spread of infection across an N x N grid. Each cell represents a county, and the program records whether that county is infected or healthy. For each day, the program checks every healthy county and counts its infected neighbors above, below, to the left, and right. If at least two of these neighbors are infected, the county becomes infected on the next day. I use a copy of the grid to record the new infections. This is important because all infections must happen at the same time. A county infected during the current day should not affect other counties until the following day. The program repeats this process until no new counties become infected. It then checks whether any healthy counties remain and prints the required message. This follow the infection rules correctly. Checking the four neighbors of each county determines whether it should become infected. Using a separate grid the next day makes sure the simulation updates all counties at the same time, rather than one after another.

How to run the program: I ran the commands below in the terminal from my Midterm CS526 folder. I ran both input files. The first returned "There are healthy counties left", and the second returned "There are no healthy counties left". Both matched the expected answers. The example outputs are saved in outputs/pandemic_output.txt, showing the final results for each of the input files. 

Commands:

python pandemic.py "Input files\pandemic_input1.txt"

python pandemic.py "Input files\pandemic_input2.txt"



PROBLEM 3:

Algorithm: The algorithm checks whether a puzzle board follows all the rules. It checks the rows, columns, and smaller square sections of the board to make sure there are no repeated symbols. It also checks that every symbol on the board belongs to the list of allowed symbols. Empty cells marked with a period are ignored. The program uses sets to keep track of the symbols it has already seen. For each row, column, and smaller square, it checks whether a symbol has appeared before. If it finds a duplicate or a symbol that is not allowed, it returns "The board is invalid". If all checks pass, it returns "The board is valid". Checking all rows, columns, and smaller squares separately makes it easier to follow each rule of the puzzle. Sets are useful because they let the program check whether a symbol has already appeared. The program also stops as soon as it finds a problem, so it does not need to finish checking the board once it knows the board is invalid.

How to run the program: I ran the commands below in the terminal from my Midterm CS526 folder. I ran all four input files. The first and third boards were valid, and the second and fourth boards were invalid. The results matches the expected answers. The example outputs are saved in 
outputs/puzzle_game_output.txt, showing the final results for each of the input files. 


Commands:

python puzzle_game.py "Input files\puzzle_game_input1.txt"

python puzzle_game.py "Input files\puzzle_game_input2.txt"

python puzzle_game.py "Input files\puzzle_game_input3.txt"

python puzzle_game.py "Input files\puzzle_game_input4.txt"



Running the programs for each problem: The input files are stored in my Input files folder, which is in my Midterm CS526 folder. Each command specifies which file the program should read. 
















