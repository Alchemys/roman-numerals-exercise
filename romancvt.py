import numbers
import re

'''
Copyright 2022 Townsend Software, All rights reserved
Version : 1.0.0
Date    : 2022-07-07
Author  : Jeffrey T. Jones

Author does not assume any responsibility for the use or abuse of this code.  
This code is simply an experiment and is intended for educational purposes only.
That being said, if you wish to use this code in part or in whole, please acknowledge the original author.
'''

intToRoman = {
    0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 
    10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60 : "LX", 70 : "LXX", 80 : "LXXX", 90 : "XC",
    100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
    1000: "M", 2000: "MM", 3000: "MMM", 4000: "(CD)", 5000: "(D)", 6000: "(DC)", 7000: "(DCC)", 8000: "(DCCC)", 9000: "(CM)"
}

romanToInt = {
    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
}

def getInputFromUser():
    print("Please Enter your Roman or Arabic numerals or q[uit] to exit: >")
    return input()


def isRomanNumeral(toTest):
    strVal = str(toTest).upper()
    if re.search(r"[\bMDCLXVI]+", strVal) != None:
        return True
    return False


def isArabicNumeral(toTest):
    try:
        # print("Testing [{}] to see if it is a number".format(toTest))
        if toTest.isnumeric():
            return True
    except:
        pass
    return False


def identifyRawInput(rawVal):
    if rawVal != None: 
        strVal = str(rawVal).upper()
        # print ("rawVal: [{}]. strVal:[{}]".format(rawVal, strVal))
        if re.search(r"^Q[UIT]*", strVal) != None:
            print ("User expressed desire to quit")
            return "quit"
        elif isRomanNumeral(toTest=strVal) == True:
            print("Identified [{}] as a set of Roman Numerals".format(strVal))
            return "roman"
        elif isArabicNumeral(toTest=rawVal) == True:
            print("Identified [{}] as an Arabic Number".format(rawVal))
            return "number"
        else:
            print("Raw input [{}] is not a valid Arabic integer (one or more value from 0-9) or Roman Numeral (one or more upper case letter from set M D C L X V I)".format(rawVal))
            return "invalid"
    else:
        print ("No input was provided for validation")
        return "invalid"

def lt10KToRoman(smallIntVal):
    retVal = ""
    if (smallIntVal < 10000):
        (thous,remVal) = divmod(smallIntVal, 1000)
        (huns,remVal) = divmod(remVal, 100)
        (tens,remVal) = divmod(remVal, 10)
        retVal = "{}{}{}{}".format(intToRoman[thous*1000], intToRoman[huns*100], intToRoman[tens*10], intToRoman[remVal])
    return retVal

def ge10KToRoman(bigIntVal):
    retVal = ""
    
    if (bigIntVal != None and bigIntVal > 0):
        retVal = "{}".format(lt10KToRoman(smallIntVal = bigIntVal))

    if (len(retVal) > 0):
        retVal = "({})".format(retVal)

    return retVal

def convertArabicToRoman(inputVal = None):
    romanVal = ""

    if inputVal != None and isArabicNumeral(toTest=inputVal):
        intVal = int(inputVal)
        if intVal < 0 or intVal > 99999999:
            print("[{}] is out of range for this converter".format(inputVal))
            return romanVal

        if intVal > 0:
            (iVal, rVal) = divmod(intVal, 10000)
            # print("intVal[{}], iVal[{}], rVal[{}]".format(intVal, iVal, rVal))
            romanVal = "{}{}".format(ge10KToRoman(bigIntVal = iVal), lt10KToRoman(smallIntVal = rVal))
        print("Arabic number [{}] converted to Roman '{}'".format(inputVal, romanVal))

    else:
        print("Could not convert arabic number [{}] to Roman Numerals".format(inputVal))


def cvtRomanToArabic(romanNum = None):
    intVal = 0
    if romanNum != None:
        # Run from left most to right most building up the arabic string to convert to an int
        # First Remove any parens
        romanNum = re.sub("\(\)", "", romanNum)
        previousVal = 0
        for idx in range(len(romanNum), 0, -1):
            try:
                romanNumVal = romanToInt[romanNum[idx-1]]
                # print("intVal[{}], previousVal[{}], romanNumVal[{}]".format(intVal, previousVal, romanNumVal))
                if romanNumVal != None:
                    if previousVal > romanNumVal:
                        intVal -= romanNumVal
                    else:
                        intVal += romanNumVal
                previousVal = romanNumVal
            except:
                pass

    return intVal

def convertRomanToArabic(inputVal = None):
    if inputVal != None :
        strVal = str(inputVal)
        if (isRomanNumeral(strVal)):
            strVal = re.sub("\s", "", strVal)
            rMatch = re.search(r"^\((\([MDCLXVI]*\))?([MDCLXVI]*)?\)?(\([MDCLXVI]*\))?([MDCLXVI]*)$", strVal)
            if rMatch != None:
                matchGroups = rMatch.group
                # print("Matched g1[{}], g2[{}], g3[{}], g4[{}]".format(matchGroups(1), matchGroups(2), matchGroups(3), matchGroups(4)))
               
                arabicNum = ((cvtRomanToArabic(matchGroups(1)) * 10 + cvtRomanToArabic(matchGroups(2))) * 10000) + (cvtRomanToArabic(matchGroups(3)) * 10) + cvtRomanToArabic(matchGroups(4))
                print("Roman Numerals [{}] converted to Arabic '{}'".format(inputVal, arabicNum))
            else:
                print("'{}' didn't match the expected Roman Numeral syntax".format(strVal))
        else:
            print("[{}] doesn't seem to be a Roman Numeral.".format(strVal))
    


def mainLoop():
    doExit = 0
    while doExit < 1:
        inValRaw = getInputFromUser()
        rawInputType = identifyRawInput(rawVal = inValRaw)
        if rawInputType == "number":
            # Convert Number to Roman numerals
            convertArabicToRoman(inputVal = inValRaw)
        elif rawInputType == "roman":
            # Convert Roman Numerals to arabic integer
            convertRomanToArabic(inputVal = inValRaw)
        elif rawInputType == 'quit':
            doExit = 1
        else:
            continue
    
'''
Roman Numeral -> Arabic value
M	1,000
D	500
C	100
L	50
X	10
V	5
I	1
'''
print("""
Hello! This will allow you to convert Roman numerals to Arabic (aka standard) numbers and vice versa.

Note: This converter won't handle any integer above 99999999.
Typically a horizontal bar is above the numerals greater than 3999.  However we use a modified nested parans formula to 'handle' values greater than 3999
[(([(val1 * 10)] + [val2]) * 10000)] + [(val3 * 10)] + [val4]
Double parens would be x10000 + single parens by x10 + value of with no parens .
For example '59845613' translates to '((D)CMLXXXIV)(D)DCXIII' : (((500 * 10) + 984) * 10000) + (500 * 10) + 613

If attempting to convert a roman numerals > 3999, use this formula
""")

try:
    mainLoop()
except:
    print("An exception occured during conversion.")
exit