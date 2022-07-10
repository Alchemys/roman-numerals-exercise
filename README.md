# roman-numerals-exercise
Small Python program for converting roman to arabic and vice versa

## Usage
`> python romancvt.py`

You will be prompted for entering Arabic numerals or Roman numerals or Q/q to exit the script.

### Arabic to Roman
This is a simple program and only handles Arabic integers between 1 and 99999999.  Simply type the number to convert (*without commas or other delimiters*) and press enter.
The script will print the converted value or error message if the number couldn't be parsed or was out of range
<BR>

### Roman to Arabic
Normal Roman Numerals cannot be bigger than 3999.  Anything larger that 3999 have to use a modified syntax to allow for the numbers.  Traditionally this is done using a horizontal bar above the Roman numerals that exceed 3999.  This program uses parenthesis to provide a simple ascii notation for these values.
<BR>
The formula is as follows
[(([(val1 * 10)] + [val2]) * 10000)] + [(val3 * 10)] + [val4]
Double parens would be x10000 + single parens by x10 + value of with no parens .
For example '59845613' translates to '((D)CMLXXXIV)(D)DCXIII' : (((500 * 10) + 984) * 10000) + (500 * 10) + 613
