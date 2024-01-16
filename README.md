# Suleman Seid_Learning_CPP
 
### 1. My goal is to get a Python Language properly installed and running inside my IDE of choice Visual Studio (VS)

[How to install a PYthon](https://visualstudio.microsoft.com/downloads/)

[How To Run Python In VS Code](https://code.visualstudio.com/docs/languages/python)

### 2. Get my first hello world in python going and learn how to deploy.

[G4G -Hello World In Python](https://www.geeksforgeeks.org/python-program-to-print-hello-world/)

---

### 3. Find out what's going on in my main
   1. What is #include <io>
      * A library for reading input and output streams in Python is io. 
      * It provides various types of I/O such as text, binary, and raw.
   2. what is using namespace std;
      * `std` stands for standard, as in python.and
      * A namespace is a system that has a unique name for each and every object in Python.
      * The statement using namespace std is generally considered bad practice in Python.
      * without std we would have to use `scope operator (::) `

      * ***Is it bad practice?***
      * [G4G : using std, bad practice](https://www.geeksforgeeks.org/using-namespace-std-considered-bad-practice/#)
   3. The main() function is like the entry point of a program.
     # Python program to demonstrate
       # main() function
       *print("Hello")
      # Defining main function
       *def main():
       *print("hey there")
      # Using the special variable
      # __name__
       *if __name__=="__main__":
           main()
   4. what is cout in python?
      *Python takes all the input as a string input by default.
   1. *To convert it to any other data type we have to convert the input explicitly.
      * used to display characters to the screen. 
      * forexamle
        # Taking input from the user
              *name = input("Enter your name: ")
        # Taking input from the user as integer
              *num = int(input("Enter a number: "))
              *add = num + 1
 
       # Output
              *print(add)
       # Output
             *print("Hello, " + name)
             *print(type(name))
   * Take the elements of the List/Set one by one and 
   * use the append() method in the case of List, and 
   * add() method in the case of a Set, to add the elements to the List / Set.
   * Exaple input:-        
           List = list()
           Set = set()
           l = int(input("Enter the size of the List : "))
           s = int(input("Enter the size of the Set  : "))
           print("Enter the List elements : ")
           for i in range(0, l):
               List.append(int(input()))
           print("Enter the Set elements : ")
           for i in range(0, s):
               Set.add(int(input()))
           print(List)
           print(Set)
       Output :
           Enter the size of the List : 4
           Enter the size of the Set  : 3
           Enter the List elements : 
           9
           0
           1
           3
           Enter the Set elements : 
           2
           9
           1
          [9, 0, 1, 3]
          {9, 2, 1}
   5. why does main return 0, what does it mean.
      * 0 stands for succesfull exit. Anything else means an error happened.

### 4. Get my fundamentals down

   1. [Inputs](https://www.w3schools.com/cpp/cpp_user_input.asp)
      * cin ( using `std`)
        * Ex : `cin << variable_Name`

   2. [Outputs](https://www.w3schools.com/cpp/cpp_output.asp)
      * cout ( using `std`)
        * Ex : `cout >> "Display This Message`
      * printf( using `stdio.h`)
        * Ex : `printf("Message")`
         
      Loops
   1.Python has two primitive loop commands:
   3. [While](https://www.w3schools.com/cpp/cpp_while_loop.asp)
        *WHILE Loops
     *With the while loop we can execute a set of statements as long as a condition is true.
          
          Examp Print i as long as i is less than 6:
                  i = 1
                  while i < 6:
                  print(i)
                  i += 1
         *With the break statement we can stop the loop 
                 even if the while condition is true:
        
           Exp:-  Exit the loop when i is 3:
                  i = 1
                  while i < 6:
                  print(i)
                  if i == 3:
                    break
                  i += 1
   4. [For](https://www.w3schools.com/cpp/cpp_for_loop.asp)
          
           for i in data:
            do something 
       OR  
   1. 
          for letter in name:
          print(letter)   
  * A For loop is used for iterating over a sequence.
   * With the for loop we can execute a set of statements.
            
         Example Print each fruit in a fruit list:
               fruits = ["apple", "banana", "cherry"]
               for x in fruits:
               print(x)
       * With the break statement we can stop
              
             Exit the loop when x is "banana":
                fruits = ["apple", "banana", "cherry"]
                for x in fruits:
                print(x)
                if x == "banana":
                   break
       * 
   5. [Conditions](https://www.w3schools.com/cpp/cpp_conditions.asp)
      * if <expr>:
            <Statement(s)>
      * elif <expr>:
            <Statement(s)>
      * else :
            <statements>
      * Python will support switch by using match in place of switch:
   6. [Variables](https://www.w3schools.com/cpp/cpp_variables.asp)
      * There are two types of variables in Python: global and local.
      * A global variable is a variable that is defined outside a function.
         
            Exple:- x = 10
                    def my_function():
                    print(x)
     * my_function A local variable is a variable that is defined inside a function and 
     * can only be accessed within that function.n() # output: 10
      
           Expl:-def my_function():
                    y = 5
                    print(y)
                    my_function() # output: 5
   7. [Data Types](https://www.w3schools.com/cpp/cpp_variables.asp) 
    *In programming, data type is an important concept.
    *Python has the following data types built-in by default:
              
              Text Type:	str
              Numeric Types:	int, float, complex
              Sequence Types:	list, tuple, range
              Mapping Type:	dict
              Set Types:	set, frozenset
              Boolean Type:	bool
              Binary Types:	bytes, bytearray, memoryview
              None Type:	NoneType
   8. [Operation](https://www.w3schools.com/cpp/cpp_variables.asp)
      * [Arithmatic]()  
      * 
         | Operator  | Description         | Example         |
         |-----------|---------------------|-----------------|
         | +         | Addition            | `a + b`         |
         | -         | Subtraction         | `a - b`         |
         | *         | Multiplication      | `a * b`         |
         | /         | Division            | `a / b`         |
         | %         | Modulus (Remainder) | `a % b`         |
         | **        | Exponentiation      | 'x ** y'        |
         | //        | Floor division      | `x // y`        |
      * [Assignment Operation](https://www.w3schools.com/cpp/cpp_operators_assignment.asp)
         | Operator  | Description         | Example         |
         |-----------|---------------------|-----------------|
         | =         | Assignment          | `a = b`         |
         | +=        | Addition assignment | `a += b`        |
         | -=        | Subtraction assignment | `a -= b`     |
         | *=        | Multiplication assgn | `a *= b`       |
         | /=        | Division assignment | `a /= b`        |
         | %=        | Modulus assignment  | `a %= b`        |
         | &=        | Bitwise AND assignment | `a &= b`     |
         | \|=       | Bitwise OR assignment | `a \|= b`     |
         | ^=        | Bitwise XOR assignment | `a ^= b`     |
         | <<=       | Left shift assignment | `a <<= b`     |
         | >>=       | Right shift assignment | `a >>= b`    |


      * [Comparison Operation](https://www.w3schools.com/cpp/cpp_operators_comparison.asp)

         | Operator  | Description            | Example         |
         |-----------|------------------------|-----------------|
         | ==        | Equal to               | `a == b`        |
         | !=        | Not equal to           | `a != b`        |
         | <         | Less than              | `a < b`         |
         | >         | Greater than           | `a > b`         |
         | <=        | Less than or equal to  | `a <= b`        |
         | >=        | Greater than or equal to | `a >= b`      |

      * [Logical Operation](https://www.w3schools.com/cpp/cpp_operators_logical.asp)

         | Operator  | Description          | Example       |
         |-----------|----------------------|---------------|
         | &&        | Logical AND          | `a && b`      |
         \| \|       | Logical OR           | `a \|\| b`    |
         | !         | Logical NOT          | `!a` or `not a`|


   4. [Arrays](https://www.w3schools.com/cpp/cpp_arrays.asp)
      * `type name[count]`
      * Python does not have built-in support for Arrays,
      * but Python Lists can be used instead or using a LISTS as ARRAYS.
      * like the NumPy library
      * We can use the append() method to add an element to an array.
      * We can use the pop() method to remove an element from the array.
      * We can use the pop() method to remove an element from the array.
      Python has a set of built-in methods that you can use on lists/arrays.

              * Method	Description
           | append()|	  |Adds an element at the end of the list|
           | clear() |	  |Removes all the elements from the list|
           | copy()	 |    |Returns a copy of the list|
           | count() |    |Returns the number of elements with the specified value|
           | extend()|	  |Add the elements of a list to the end of the current list|
           | index() |	  |Returns the index of the first element with the specified value|
           | insert()|	  |Adds an element at the specified position|
           | pop()	 |    |Removes the element at the specified position|
           | remove()|	  |Removes the first item with the specified value|
           |reverse()|	  |Reverses the order of the list|
           | sort()	 |    |Sorts the list|
   8. [Classes]
      * [Geeks for Geeks - Headers](https://www.geeksforgeeks.org/header-files-in-c-cpp-and-its-uses/) 
      * Python is an object oriented programming language.
      * Almost everything in Python is an object, with its properties and methods.
      * A Class is like an object constructor, or a "blueprint" for creating objects.
         *To create a class, use the keyword class:
---
1. The similarities of C# anad Python Language:-
   * C# and Python are both high-level, object-oriented, and easy-to-learn languages.
   * They are both general-purpose languages that can be used for a wide range of applications. 
   * They are both popular languages for developing web applications, desktop applications, and games. 
   * They are both general-purpose languages that can be used for a wide range of applications. Both languages have a large community of developers and users, which means that there is a lot of support available online.
2. Python and C# are two different programming languages that are used for different purposes. Here are some key differences between Python and C#:
   * Syntax: Python has a simpler and more straightforward syntax, which makes it easier to read and write. On the other hand, C# has a more complex syntax, which requires more attention to detail.
   * Performance: C# is generally faster than Python because it is a compiled language. Python, on the other hand, is an interpreted language, which means that it is slower than C#.
   * Use cases: Python is commonly used for scientific computing, data analysis, and web development, while C# is often used for Windows desktop applications, game development, and enterprise software.
   * Platform independence: Python is platform-independent, which means that it can run on multiple operating systems. C# is primarily used on the Windows platform, although it can also be used on other platforms with the help of .NET Core.
   * Type system: Python is a dynamically typed language, which means that the type of a variable is determined at runtime. C#, on the other hand, is a statically typed language, which means that the type of a variable is determined at compile time.
   * Garbage collection: Python has an automatic garbage collection system, which means that it frees up memory automatically. C#, on the other hand, also has a garbage collection system, but it requires more manual intervention to manage memory efficiently.
  
 NB.In summary, Python is a simpler language that is ideal for scientific computing and data analysis, while C# is a more complex language that is better suited for Windows desktop applications, game development, and enterprise software. However, both languages have their own strengths and weaknesses, and the choice between them
3. Why do I want to learn Python. 
   * Python is a popular programming language that is used in a variety of fields, from data science and machine learning to game design. It is an in-demand, accessible language with an active, ever-growing community of users.
   * Python is relatively easy to learn and incredibly versatile, making it a great place to start if you’re new to coding. 
   * It’s also a great language to learn if you’re looking to switch careers into the tech world through coding. 
   * It is used across many different industries, from data science and software engineering to mobile app development, artificial intelligence, and machine learning.
   * Python is also platform-independent, meaning that it can run on multiple operating systems.
   * Python is highly versatile, and you can use it for both small and complex tasks
4. What Tutorials am I considering using for my project?  
[W3Schools: ](https://www.w3schools.com/python/)  
[freeCodeCamp.org:](https://www.freecodecamp.org/news/the-best-way-to-learn-python-python-programming-tutorial-for-beginners/)
[LearnPython.org:](https://www.learnpython.org/)


5. End goal : What do I want to have built within 4 weeks of starting to learn CPP. 
   * To build websites and software or.
   * To be a conduct data analysis.
   * 
6. Experience doing the code review in a new language :
   *Python’s simple syntax and readability make it an accessible language for beginners, while its modularity and code reuse make it a popular choice for experienced developers. 
   
  Part 2 : Details and Observations ( Short answers )

   * What language did you choose?  
        Python                           
   * What IDE did you choose?
        Visual Studio
   * Did you have any difficulty getting it installed and running?
        Yes
   * Is Python a higher or lower-level language than C# and Java?
       Python is a high-level programming language. 
       Also, it has dynamic semantics and is suitable for rapid application development,
       which is closer to human languages and abstracts low-level details 
       such as memory management and hardware interaction.
       Python, C#, and Java are high-level languages but are compiled languages 
       while Python interprets them. It means Python code is executed line by line at runtime, 
       while C# and Java codes are converted into machine code before execution.
   
   * Is Python a strongly or loosely typed language?
       Python is a dynamic and strongly typed language. 
       That means the type of a value doesn’t change in unexpected ways, 
       and every change of types requires an explicit conversion. 
   
   * Is Python a compiled or scripted language?
        Python can be both compiled and interpreted, but the default implementation of Python is
        an interpreted language. When you run a Python script, 
        the Python interpreter reads the code line by line, compiles it into bytecode, 
        and then executes the bytecode.
   
   * Why did you choose this language?
        Python is a popular programming language that is easy to learn, open-source, and flexible. 
        Python has extensive built-in libraries and sturdy frameworks that help with data analysis, web development, machine learning, and more.
        Python is also portable, fast, and scalable, which makes it suitable for handling large amounts of data and complex problems. 

   * What applications did you plan to build with it? 
       I want to go with either web development or data analysis. 
