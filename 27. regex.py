"""
How Regular Expressions (Regex) Work
    Regex is a tool for searching, matching, and manipulating text based on patterns.
    🔎 Think of it like a search engine that looks for specific text patterns instead of exact words.
    Python provides the re module to work with regular expressions.


Basic Concepts of Regex
    Literals → Exact characters
        Matches the exact text.
        Example: "cat" matches "cat" in "my cat is cute".
    Metacharacters → Special characters with meanings
        Used to build patterns.
        Example: . (dot) means any character.
    Character Classes → Match specific groups of characters
        [abc] → Matches a, b, or c.
        [0-9] → Matches any digit.
    Predefined Character Sets
        \d → Digit (0-9)
        \w → Word character (letters, digits, _)
        \s → Whitespace (space, tab, newline)
    Quantifiers → Define how many times a character or pattern can repeat
        * → 0 or more times
        + → 1 or more times
        ? → 0 or 1 time
        {n} → Exactly n times
        {n,} → At least n times
        {n,m} → Between n and m times
    Anchors → Position in the text
        ^ → Start of a string
        $ → End of a string
    Groups and Alternation
        (abc) → Groups patterns
        a|b → Matches a or b

Common re Functions in Python
    re.match() → Matches the pattern at the beginning of the string.
    re.search() → Searches the entire string for a pattern.
    re.findall() → Returns all matches as a list.
    re.finditer() → Returns an iterator yielding match objects.
    re.sub() → Substitutes occurrences of a pattern with another string.
    re.split() → Returns a list where the string has been split at each match.

The r before a string in Python makes it a raw string.
What Is a Raw String?
    A raw string tells Python to ignore escape sequences like \n, \t, or \\.
    It treats the backslash (\) as a normal character, not as an escape character.
    Example: 
        text = r"Hello\nWorld"
        print(text)   # Hello\nWorld
        # \n is treated as two characters (\ and n), not a newline.


| Pattern  | Meaning                        | Example Match         |
|----------|--------------------------------|----------------------|
| \d       | Digit (0-9)                   | 2023 → 2, 0, 2, 3   |
| \w       | Word character (a-z, 0-9, _) | hello_123 → all      |
| \s       | Whitespace                   | "a b" → space        |
| [aeiou]  | Any vowel                    | apple → a, e        |

"""

import re

# 1. match() - Match at the beginning
result = re.match(r'Hello', 'Hello World')
print(result.group())  # Output: Hello

# 2. search() - Search anywhere
result = re.search(r'World', 'Hello World')
print(result.group())  # Output: World

# 3. findall() - Find all matches
result = re.findall(r'\d+', 'Order 1, Item 23, Total 456')
print(result)  # Output: ['1', '23', '456']

# 4. sub() - Replace pattern
result = re.sub(r'\s', '-', 'Hello World')
print(result)  # Output: Hello-World

# 5. finditer() - Iterator over matches
for match in re.finditer(r'\d+', 'Item 23 costs 456'):
    print(match)  # <re.Match object; span=(5, 7), match='23'>,  <re.Match object; span=(14, 17), match='456'>     returns the match object itself which containing information about the search and the result.
    print(match.span())  # Output: (5, 7), (14, 17)    returns a tuple containing the start-, and end positions of the match.
    print(match.group())  # Output: 23, 456     returns the part of the string where there was a match
    print(match.string)   # Item 23 costs 456    returns the string passed into the function.

# 6. split() - Split the string 
txt = "The rain in Spain"
x = re.split("\s", txt)  # Split the string at every white-space character
print(x)   # ['The', 'rain', 'in', 'Spain']



"""
📌 **Basic Character Sets**

| **Pattern**  | **Meaning**                                 | **Example Match**                 |
|--------------|---------------------------------------------|----------------------------------|
| \d           | Digit (0-9)                                | "2023" → 2, 0, 2, 3             |
| \D           | Non-digit character                        | "Year2023" → Y, e, a, r         |
| \w           | Word character (a-z, A-Z, 0-9, _)          | "hello_123" → all characters    |
| \W           | Non-word character                         | "hello!" → !                    |
| \s           | Whitespace (space, tab, newline)           | "a b" → space                   |
| \S           | Non-whitespace character                   | "a b" → a, b                    |
| .            | Any character except newline               | "cat" → c, a, t                |
| [abc]        | Any one of a, b, or c                     | "apple" → a                    |
| [^abc]       | Not a, b, or c                            | "apple" → p, p, l, e          |
| [a-z]        | Any lowercase letter                      | "Hello" → e, l, l, o          |
| [A-Z]        | Any uppercase letter                      | "Hello" → H                   |
| [0-9]        | Any digit                                 | "Room 42" → 4, 2             |
| [a-zA-Z0-9]  | Any letter or digit                       | "Hi5!" → H, i, 5             |

---

📌 **Anchors (Position Matching)**

| **Pattern**  | **Meaning**                                 | **Example Match**                 |
|--------------|---------------------------------------------|----------------------------------|
| ^            | Start of a string                          | "^Hello" → Matches "Hello World" |
| $            | End of a string                            | "world$" → Matches "Hello world" |
| \b           | Word boundary                              | r"\bcat" → "cat is here"        |
| \B           | Non-word boundary                          | r"\Bcat" → "educate"            |

---

📌 **Quantifiers (Repetitions)**

| **Pattern**  | **Meaning**                                 | **Example Match**                 |
|--------------|---------------------------------------------|----------------------------------|
| *            | 0 or more occurrences                      | "lo*l" → "ll", "lol", "lool"    |
| +            | 1 or more occurrences                      | "lo+l" → "lol", "lool"          |
| ?            | 0 or 1 occurrence                          | "colou?r" → "color", "colour"   |
| {n}          | Exactly n occurrences                      | "a{3}" → "aaa"                  |
| {n,}         | n or more occurrences                      | "a{2,}" → "aa", "aaa", "aaaa"  |
| {n,m}        | Between n and m occurrences                | "a{2,4}" → "aa", "aaa", "aaaa" |

---

📌 **Special Groups**

| **Pattern**     | **Meaning**                               | **Example Match**                |
|-----------------|-------------------------------------------|---------------------------------|
| (abc)           | Matches "abc" as a group                  | "(cat|dog)" → "cat" or "dog"   |
| (?:abc)         | Non-capturing group                      | Same as above, but not captured |
| (?P<name>abc)   | Named group                              | Captures group as "name"        |
| (?=abc)         | Positive lookahead (followed by abc)     | "foo(?=bar)" → "foo" in "foobar" |
| (?!abc)         | Negative lookahead (not followed by abc) | "foo(?!bar)" → "foo" not in "foobar" |

---

📌 **Escape Sequences**

| **Pattern**  | **Meaning**                                 | **Example Match**                |
|--------------|---------------------------------------------|---------------------------------|
| \\           | Escapes special characters                 | "\\" → "\"                      |
| \.           | Matches a literal dot                      | "3.14" → "."                    |
| \*           | Matches a literal asterisk                 | "5 * 2" → "*"                  |
| \|           | Matches a literal pipe                    | "a|b" → "|"                   |

---

📌 **Common Regex Functions in Python**

| **Function**             | **Description**                             | **Example**                              |
|--------------------------|---------------------------------------------|-----------------------------------------|
| `re.findall()`           | Returns all matches as a list               | `re.findall(r"\d+", "abc123") → ['123']` |
| `re.search()`            | Returns the first match as a match object   | `re.search(r"abc", "123abc")`           |
| `re.match()`             | Matches pattern only at the beginning       | `re.match(r"abc", "abc123")`           |
| `re.split()`             | Splits string by pattern                   | `re.split(r"\s", "a b c") → ['a','b','c']` |
| `re.sub()`               | Replaces matches with a string             | `re.sub(r"\s", "-", "a b c") → "a-b-c"` |

"""