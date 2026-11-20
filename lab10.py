# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    #  copy each number down in their own variables and then solve the question using revers polish notation, this will be done by using 
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    Ctokens = []
    for token in tokens:
        if token.lstrip('-').isdigit():
            Ctokens.append(int(token))
        else:
            if Ctokens[1:] != []:
                Int2 = Ctokens.pop()

                Int1 = Ctokens.pop()
                if token == "+":
                    Ctokens.append(int(Int1+Int2))
                elif token == "-":
                    Ctokens.append(int(Int1-Int2))
                elif token == "/":
                    Ctokens.append(int(Int1/Int2))
                elif token == "*":
                    Ctokens.append(int(Int1*Int2))
    return Ctokens.pop()


def decode_string(s):
    # Outline:
    #   we take in the multiplyer and when opening brackets are found, it goes through untill closing brackets are found and repeats that x times
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    stack2 = []
    current_string = ""
    current_num = 0
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            stack2.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == "]":
            previous_string, num = stack2.pop()
            current_string = previous_string + current_string * num
        else:
            current_string += char

    return  current_string


def daily_temperatures(temps):
    # Outline:
    #  go through every element in the array and then start another for loop to go through the array from there until a greater number is found, the second loop then ends,
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    Len = len(temps)
    temptime = [0] * Len
    for temp in range(Len):
        for x in range(temp+1, len(temps)):
            if temps[x] > temps[temp]:
                temptime[temp] = x-temp
                break
    return temptime

def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    #print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(eval_rpn(["2", "1", "+", "3", "*"]))
    pass


if __name__ == "__main__":
    main()
