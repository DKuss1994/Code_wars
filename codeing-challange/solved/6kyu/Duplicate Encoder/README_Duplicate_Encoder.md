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

### Code
➡️ [Duplicate_Encoder.py](./codeing-challange/solved/6kyu/Duplicate_Encoder/Duplicate_Encoder.py)  

### Tests
➡️ [test_Duplicate_Encoder.py](./codeing-challange/solved/6kyu/Duplicate_Encoder/test_Duplicate_Encoder.py)  

### Lessons Learned
- Using hashmaps or `Counter` simplifies duplicate checking  
- `.lower()` makes the comparison case-insensitive  
- Writing unit tests helps catch logic errors early

