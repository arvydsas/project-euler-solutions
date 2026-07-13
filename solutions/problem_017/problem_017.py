# Solution note: I build the written form of every number from 1 to 1000 and
# count the letters after omitting spaces and hyphens.
ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
]
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
an = 'and'
hundred = 'hundred'

stri = 'onethousand'

for i in range(1, 1000):
    a = str(i)
    if len(a) == 1:
        stri += ones[i]
    if len(a) == 2:
        if 10 <= i <= 19:
            stri += teens[i - 10]
        else:
            stri += tens[i // 10]
            stri += ones[i % 10]
    if len(a) == 3:
        stri += ones[i // 100]
        stri += hundred
        if i % 100 == 0:
            pass
        else:
            b = i % 100
            stri += an
            if 10 <= b <= 19:
                stri += teens[b - 10]
            else:
                stri += tens[b // 10]
                stri += ones[b % 10]

print(len(stri))
