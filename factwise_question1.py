def number_to_words(n):
    num_dict = {
        0: "", 1: "one", 2: "two", 3: "three", 4: "four", 
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 
        14: "fourteen", 15: "fifteen", 16: "sixteen", 
        17: "seventeen", 18: "eighteen", 19: "nineteen", 
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }
    if n < 20:
        return num_dict[n]
    elif n < 100:
        return num_dict[n - (n % 10)] + num_dict[n % 10]
    elif n < 1000:
        if n % 100 == 0:
            return num_dict[n // 100] + "hundred"
        else:
            return num_dict[n // 100] + "hundredand" + number_to_words(n % 100)
    elif n == 1000:
        return "onethousand"
def counting_letters_in_words(n):
    total_letters = 0
    for i in range(1, n + 1):
        words = number_to_words(i)
        total_letters += len(words)
    return total_letters
total_letters = counting_letters_in_words(1000)
print("Total letters used from 1 to 1000 inclusive:", total_letters)
