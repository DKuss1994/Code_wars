##  Duplicate Encoder (6 kyu)
 [Challenge on CodeWars](https://www.codewars.com/)

### Problem
Convert a string into a new string where each character is:
- `"("` if it appears only once in the original string  
- `")"` if it appears more than once  

Ignore capitalization when checking for duplicates.

### Approach
- Convert the string to lowercase  
- Check each character for duplicates  
- Use `)` if a character appears multiple times, otherwise `(`  

### Example
| Input       | Output    |
|------------ |-----------|
| `"din"`     | `"((("`   |
| `"recede"`  | `"()()()"`|
| `"Success"` | `")())())"`|
| `"(( @"`    | `"))(("`  |


### Lessons Learned
- I learned how to count characters in a string.
- I practiced ignoring uppercase and lowercase letters.
- I learned how to keep track of characters that appear more than once.
- I realized that unit tests help to find errors early.
- I practiced checking my code step by step and keeping it organized.


