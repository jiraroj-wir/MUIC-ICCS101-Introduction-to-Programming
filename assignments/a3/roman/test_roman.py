import csv

'''
PLACE YOUR CODE/FUNCTION UNDER HERE !!!
'''


CHECK_UP_TO_9999 = False    # if you want to go up to 9999, change it to True

# you might have to change the testset_roman.csv path, if you're using other os, especially window
def load_testset(path='testset_roman.csv'):
    data = {}
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[int(row['number'])] = row['roman']
    return data

def compare_with_testset():
    dataset = load_testset()
    failed = []
    max_check = 9999 if CHECK_UP_TO_9999 else 4000

    for num in range(1, max_check + 1):
        expected = dataset.get(num)
        if expected is None:
            continue
        try:
            '''
            I SUPPOSED YOUR FUNCTION NAME IS 'toRoman', BUT CHANGE IT IF NOT
            '''
            result = toRoman(num)   # change here !!!
            if result != expected:
                failed.append((num, expected, result))
        except Exception as e:
            failed.append((num, expected, f'exception: {str(e)}'))

    if failed:
        print(f"{len(failed)} mismatches found (showing first 15:")
        for f in failed[:15]:
            print(f"number {f[0]}: expected '{f[1]}', got '{f[2]}'")
    else:
        print("✅ AC")

if __name__ == "__main__":
    compare_with_testset()
