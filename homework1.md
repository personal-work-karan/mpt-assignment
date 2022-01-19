# Homework #1

## ⚠️ We use auto-graders for most parts of the assignment. Please, follow the instructions precisely; you will lose credit for deviances. Stick to the variables’ names and case sensitivity.

## ❗Do not try to modify the already created files under `tests/` directory. These are used to evaluate your submission; changes to these are considered cheating, and will cause your grade to be zero.

## 🎁 10% Bonus: When merging branches, squash the commits done in dev branches into one commit.

## **Objectives**

- Becoming familiar with completing programming assignments/projects using GitHub.
- Get started with git and GitHub
- Learn how to write mark-down documentation and put instructions on how to reproduce work.
- Learn how to create multiple versions of your project and create releases with tags.
- Learn to create both CLI and API.

## Part 1 (25 pts)

### 1.1 Connect to your GitHub using your ssh-key and test your connection.

Make sure you can connect to your GitHub account using your ssh-key. You can find instructions to achieve that here: [https://docs.github.com/en/authentication/connecting-to-github-with-ssh](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

It is recommended that create a new SSH key for GitHub. Never share your private key :)

### 1.2 Accept the invitation to the assignment

After making sure your environment is ready and you can connect to GitHub via SSH, click on the following URL to accept the assignment invitation. **Link goes here ...**

You will find a file named `student_info.json`in the project’s root directory. You will need to replace the placeholders with your exact information. This is part of the homework, don't skip this. 

## Part 2 (25 pts)

You will create a Python project that consists of two parts. The first part is a Python class that can be used as an API (a reusable library) in file `sorter_api.py`. The second part is a Python command-line interface (CLI) application, in file `sorter_cli.py` that uses that class to handle the user arguments and execute the sort function.

**All the source code should exist inside the `src` directory.**

### **GitHub Instructions**

- Create a new branch and name it `add/sort_strings`.
- Checkout  to the newly created branch.
- Develop the needed features in sections 2.1.
- Commit the changes with meaningful commit messages.
- Create a PR into the `main` branch with the changes.
- Add a description to the PR stating what you’ve done.
- Merge into the main branch when you are done with development.
- Don’t delete your old branch.

### 2.1 The Python class

You will find a Python class called `Sorter` that has the primary purpose of sorting data.

- We provided the appropriate constructor that can accept:
    1. `sort_type` : either `lexicographically` or `numbers`.
    2. `sort_order`: either `ASC` or `DESC` .

- We Implement a class method `sort_nums` that can accept an iterable of numbers, verifies that all items are integers, then return a sorted list according to the constructor configuration.
- You will implement `sort_strings` that accept list of strings and sort them `lexicographically` in `asc` or `desc` order. YOu can implement `sort_strings` using any algorithm you like. 
- As demonstrated in the example code, you will need to add the proper docstrings and documentation for the newly implemented function.

### 2.2 Release your current version

In your `main` branch, create a release of your stable, tested code.

GitHub provides a simple interface for creating releases and tags. You can also create that tag on your terminal without using the GitHub interface. [External docs](https://www.toolsqa.com/git/github-releases/)

Now that you have extended the `Sorter` class by the function `sort_strings`, it is ready to be used as an API (Python library). Create a new tag with version `v1.0` and let’s continue our development.

 

---

## Part 3 Python CLI (35 pts)

> Refer to the GitHub instructions from Part 2 to create a different branch called `add/cli` from your `main` branch once you have merged the previous code.

Inside the `src` directory, you will find a Python script file named `sorter_cli.py` that takes the following positional system arguments. *Please, notice the order and allow case insensitivity in the input parameters.*

1. Sort type: `lex` or `num`
2. Sort order: `asc` or `desc` 
3. Filename to be sorted (plain text file is expected with alphabet words in each line).
4. Output file name

The CLI script should only depend on the simple `sys.argv` to handle the system arguments. The script should import and use the `Sorter`class and invoke the `sort_strings` method. The script’s purpose is to take an input file **(3)**, and write a sorted output file **(4)** with the settings from **(1)**, **(2)**. You will need to sort the lines. Please note that the lines could be either number, or words, not both.

**For example:**

Unsorted file:
```
Zebra
Banana
Apple
```

Sorted file:
```
Apple
Banana
Zebra
```

Unsorted file:
```
4
0
1
```

Sorted file:
```
0
1
4
```

**Please remember to create a PR from the `add/cli` branch to `main` branch once you are done with your changes. Then you can merge that pull request**

<hr>

## Part 4 Wrapping up and final release (15 pts)

It is a good practice to make sure you are documenting everything for future reference or for user guidance. On GitHub, the common language to write docs is called markdown. Please refer to [https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) or look up for it.

In this part, you are required to write full documentation your developed program. You will write the following:

- Create a file called `docs.md` in the root directory.
- API example (How to call the library/API).
- CLI Example (How to call the command from the terminal)
- What are the different types of sorting?

After writing the documentation, you can now wrap up the whole project and release it in a second release tag named `v2.0`. *(Follow the releasing instructions from section 2.2)*

### Notes

- Don’t use external libraries (unless you provide a `requirements.txt`file.
- Do not use the GitHub application/any other UI application to upload code.
- Depend only on your terminal to get everything done.

### How we will grade

Our desired eductional outcome for this homework is to check that a) You can make the required python changes
(40% of the credit) for each part and b) you Have the proper git history for each part (60% of the credit). 

- We will run test cases to check that your code does the API and CLI functions correctly
- We will check the history of your submitted version control repo. We're looking for teh following: 

1. There are 3 branches in your repo, named: "main", "add/cli", and "add/sort_strings" - 15 points
2. There is a merged pull request on the "add/sort_strings" branch - 5 points
3. There is a merged pull request on the "add/cli" branch - 5 points
4. The "add/sort_strings" merge occurs before the "add/cli" merge - 5 points