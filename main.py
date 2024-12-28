// DANIEL ONYEAKAZI
// 21/11/24 -- 30/11/24
// HN SOFTWARE DEVELOPMENT ASSESSMENT



using System;
using System.IO;

// Welcome message
static void Message()
{
    Console.WriteLine("Welcome to Enigma, a cipher game");
    Console.WriteLine("Test your logic skills for a few minutes! \n");
}


// Function to create a username
static string CreateUsername()
{
    Console.WriteLine("Enter your first name: ");
    string firstName = Console.ReadLine();


    Console.WriteLine("Enter your initials (at least 3 characters): ");
    string initials = Console.ReadLine();


    // Validate input
    if (firstName.Length < 2 || initials.Length < 3)
    {
        Console.WriteLine("Invalid input. Please try again.");
        return CreateUsername(); // Recursive call for invalid input
    }


    // Create username from the full first name and lowercase initials
    string username = firstName.ToLower() + initials.ToLower();
    return username;
}


// User Authentication
static void UserAuthentication()
{
    Console.WriteLine("Do you want to create an account? (y/n)");


    string input = Console.ReadLine().ToLower();
    string username = "";
    string password = "";


    if (input == "y")
    {
        // Create username
        username = CreateUsername();
        Console.WriteLine($"Your generated username is: {username}");


        // Prompt for password
        Console.WriteLine("Enter your password (min 6 characters): ");
        password = Console.ReadLine();


        if (password.Length < 6)
        {
            Console.WriteLine("Must be a minimum of 6 characters. Please re-enter.");
        }
    }
    else if (input == "n")
    {
        // Default to guest account
        username = "Guest";
        Console.WriteLine("You are logged in as a Guest.");
    }
    else
    {
        Console.WriteLine("Invalid input. Please enter 'y' or 'n'.");
        UserAuthentication();
    }
}


// Main Execution
Message();
UserAuthentication();




Console.Clear();




// Difficulty Selection
Console.WriteLine($"Welcome {username}");


string choice;


Console.WriteLine("\nChoose a difficulty level: ");
Console.WriteLine("1 - Easy: (4 digits, 6 attempts)");
Console.WriteLine("2 - Medium: (5 digits, 8 attempts)");
Console.WriteLine("3 - Hard: (6 digits, 10 attempts)");
Console.WriteLine("Now, enter your choice (1-3): ");


choice = Console.ReadLine();




bool validChoice = false;
int digitCount = 0;
int maxAttempts = 0;
int basePoints = 0;
int bonusPoints = 5;
string difficultyLevel = "";




while (validChoice == false)
{
   if (choice == "1")
   {
       digitCount = 4;
       maxAttempts = 6;
       basePoints = 10;
       difficultyLevel = "Easy (4 digits, 6 attempts)";
       validChoice = true;
   }




   else if (choice == "2")
   {
       digitCount = 5;
       maxAttempts = 8;
       basePoints = 15;
       difficultyLevel = "Medium (5 digits, 8 attempts)";
       validChoice = true;
   }




   else if (choice == "3")
   {
       digitCount = 6;
       maxAttempts = 10;
       basePoints = 20;
       difficultyLevel = "Hard (6 digits, 10 attempts)";
       validChoice = true;
   }
  
   else
   {
       Console.WriteLine("\nInvalid category. Please re-enter your choice");
       Console.WriteLine("Choose a difficulty level: ");
       Console.WriteLine("1 - Easy: (4 digits, 6 attempts)");
       Console.WriteLine("2 - Medium: (5 digits, 9 attempts)");
       Console.WriteLine("3 - Hard: (6 digits, 12 attempts)");
       Console.WriteLine("Now, enter your choice (1-3): ");


       choice = Console.ReadLine();
       validChoice = false;




   }




}




// Generate random code


Random random = new Random();
string code = "";




for (int i = 0; i < digitCount; i++)
{
  code += random.Next(1, 7).ToString(); // Turns the code into a string
}




Console.WriteLine("\nGameplay Instructions: ");
Console.WriteLine($"Guess the {digitCount}-digit number. Each digit is between 1 and 6.");
Console.WriteLine("A plus sign (+) means a correct digit in the right position.");
Console.WriteLine("A minus sign (-) means a correct digit in the wrong position.");
Console.WriteLine("And a hashtag (#) indicates completely incorrect digits that are not in the code.");
Console.WriteLine($"You have {maxAttempts} guesses. Good luck!! \n");






// Gameplay
int attemptsUsed = 0;
int reAttempts = 0;
bool isCodeGuessed = false;
int total = 0;
bool isValidGuess;
string guess = null;


for (int attempts = 0; attempts < maxAttempts; attempts++)
{
   attemptsUsed = attempts + 1;
   Console.WriteLine($"Attempt {attemptsUsed}/{maxAttempts}: ");
   guess = Console.ReadLine();




// Validate guess
   reAttempts = 0;
   isValidGuess = false;


   while (reAttempts < 3)
   {
       if (guess.Length != digitCount)
       {
           Console.WriteLine($"Invalid input. Must be {digitCount} digits (1-6).");
           reAttempts++;
           Console.WriteLine($"Attempt {attemptsUsed}/{maxAttempts}: ");
           guess = Console.ReadLine();
       }
      
       else
       {
           isValidGuess = true;
           foreach (char c in guess)
           {
               if (c < '1' || c > '6')
               {
                   Console.WriteLine($"Invalid input. All digits must be between 1 and 6.");
                   reAttempts++;
                   Console.WriteLine($"Attempt {attemptsUsed}/{maxAttempts}: ");
                   guess = Console.ReadLine();
                   isValidGuess = false;
                   break;
               }
           }
       }




       if (isValidGuess) break;
   }




// Generate hint
   int plusCount = 0; // Correct digit in correct position
   int minusCount = 0; // Correct digit in wrong position


   char[] hint = new char[guess.Length];
   bool[] matchedCode = new bool[digitCount]; // position of code relative to the number of digits
   bool[] matchedGuess = new bool[digitCount]; // position of guess relative to the number of digits


   
   for (int i = 0; i < hint.Length; i++)
   {
       hint[i] = '#';
   }
  
   // Check for exact matches
   for (int i = 0; i < digitCount; i++)
   {
       if (guess[i] == code[i])
       {
           hint[i] = '+';
           plusCount++;
           matchedCode[i] = true;
           matchedGuess[i] = true;
       }
   }


// Check for misplaced matches
   for (int i = 0; i < digitCount; i++)
   {
       if (!matchedGuess[i])
       {
           for (int j = 0; j < digitCount; j++)
           {
               if (!matchedCode[j] && guess[i] == code[j])
               {
                   hint[i] = '-';
                   minusCount++;
                   matchedCode[j] = true;
                   break;
               }
           }
       }
   }




   Console.WriteLine($"Hint: {new string(hint)}"); // the hint of pluses / minuses / hashtags as a string


// Check for win
   if (guess == code)
   {
       Console.WriteLine("\nCongratulations! You've guessed the code!");
       isCodeGuessed = true;
       break;
   }
}




// Score Calculation
    if (isCodeGuessed && attemptsUsed <= maxAttempts / 2)
    {
        total = basePoints + bonusPoints;
    }


    else if (isCodeGuessed)
    {
        total = basePoints;
    }




// Save to file
    if (isCodeGuessed || attemptsUsed == maxAttempts)
    {
        using (StreamWriter sw = new StreamWriter("Enigma.txt", true))
        {
            sw.WriteLine($"Username: {username}");
            sw.WriteLine($"Difficulty: {difficultyLevel}");
            sw.WriteLine($"Code: {code}");
            sw.WriteLine($"Guessed: {(isCodeGuessed ? "Yes" : "No")}");
            sw.WriteLine($"Bonus Points: {(isCodeGuessed && attemptsUsed <= (maxAttempts / 2) ? "Yes" : "No")}");
            sw.WriteLine($"Score: {total}");
            sw.WriteLine($"Attempts Used: {attemptsUsed}");
            sw.WriteLine("-------------------------------");
        }


        // Final message
        if (isCodeGuessed)
        {
            Console.WriteLine($"Congratulations, {username}! Your total score: {total}");
        }


        else
        {
            Console.WriteLine($"Game Over! The correct code was: {code}");
        }
        
    }
