#!/usr/bin/env python3

# Name: <Hakim Alhassan>
# Index number: <PS/ITC/14/0034>

# TODO: Put your codes here ...


my_input = "2345678901"
Zero = ["****** ", "*    * ", "*    * ", "*    * ", "*    * ", "*    * ", "*    * ", "*    * " , "*    * " , "*    * " , "****** "]
One = ["*      ","*      ","*      ","*      ","*      ","*      ","*      ","*      ","*      ","*      ","*      "]
Two = ["****** ", "     * ","     * ", "     * ","     * ", "****** ","*      ","*      ","*      ","*      ", "****** "]
Three = ["****** ", "     * ","     * ","     * ","     * ", "****** ", "     * ","     * ","     * ","     * ", "****** "]
Four = ["*    * ", "*    * ","*    * " , "*    * " ,"*    * " ,  "****** ", "     * ","     * ", "     * ","     * ","     * ","     * ","     * "]
Five = ["****** ", "*      ","*      " ,"*      " ,"*      " , "****** ", "     * ", "     * ","     * ","     * ", "****** "]
Six = ["****** ", "*      ","*      " ,"*      " ,"*      " , "****** ", "*    * ", "*    * ","*    * ","*    * ", "****** "]
Seven = ["****** ","     * " , "     * ", "     * ", "     * ", "     * ","     * ","     * ","     * ","     * ", "     * "]
Eight = ["****** ", "*    * ", "*    * ","*    * ","*    * ", "****** ", "*    * " , "*    * " ,"*    * " ,"*    * " , "****** "]
Nine = ["****** ", "*    * ", "*    * ", "*    * ","*    * ", "****** ", "     * " ,"     * " ,"     * " , "     * " , "****** "]

Digits = [Two, Three, Four, Five, Six, Seven, Eight, Nine, Zero, One]

# TODO: Print all the digits on the same line
try:
    row = 0
    while row < 11:
        line = ""
        column = 0
        while column < len(my_input):
            # TODO: Put your code after this comment
            
            line += Digits[column][row]            
            column += 1
            
        # TODO: Print line here and add an incrementer
        print (line)
        row += 1   
except:
    # TODO: Handle one suitable error which may occur
    pass
