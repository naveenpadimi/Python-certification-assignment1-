# Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks= student_marks[query_name]
    avg = sum(marks)/len(marks)
    print("{:.2f}".format(avg))

# String Split and Join



def split_and_join(line):
    # write your code here
    words = line.split()
    return "-".join(words)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Set .intersection() Operation


n = int(input())


english = set(map(int, input().split()))


m = int(input())


french = set(map(int, input().split()))


common = english.intersection(french)


print(len(common))

# Find the Runner-Up Score!


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
scores = set(arr)
sorted_scores = sorted(scores,reverse = True)
runner_up_score = sorted_scores[1]
print(runner_up_score)

# sWAP cASE


def swap_case(s):
    result = ""
    for char in s:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
            
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# Arithmetic Operators


if __name__ == '__main__':
    a = int(input())
    b = int(input())
summ = a + b
difference = a - b
product = a * b
print(summ)
print(difference)
print(product)

# Python: Division


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
integer_division = a//b
float_division = a/b

print(integer_division)
print(float_division)

# Python If-Else


if __name__ == '__main__':
    n = int(input().strip())
    
if n % 2 ==1:
   print("Weird") 
else:
    if n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    else:
        print("Not Weird")

# Nested Lists


if __name__ == '__main__':
    student_list =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append((name, score))
    sorted_list = sorted(student_list, key=lambda x: (x[1], x[0]))
    second_lowest_score = sorted(set(score for name, score in student_list))[1]
    for name, score in sorted_list:
        if score == second_lowest_score:
            print(name)

# Loops

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)

# Write a function


def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

year = int(input())
print(is_leap(year))

# Find a string


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# Lists


if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        query = input().split()
        command = query[0]
        if command == 'insert':
            lst.insert(int(query[1]), int(query[2]))
        elif command == 'print':
            print(lst)
        elif command == 'remove':
            lst.remove(int(query[1]))
        elif command == 'append':
            lst.append(int(query[1]))
        elif command == 'sort':
            lst.sort()
        elif command == 'pop':
            lst.pop()
        elif command == 'reverse':
            lst.reverse()

