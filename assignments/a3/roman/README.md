# 🏛️ Roman Numeral Tester

This is an **extra testing module** I made to help you debug your `toRoman(n: int)` function for Assignment 3.  
I know it might be tricky to figure out exactly where your code goes wrong — so here's a tool to help!

---

## 📄 Files in this folder

- `test_roman.py` – the main script where you paste your function and run the tests  
- `testset_roman.csv` – a test dataset of numbers `1` to `9999` and their correct Roman numeral strings (based on my implementation)
- `roman.py` - my solution

---

## ⚙️ How to use this
1. Clone this git repository using `git clone [this repository link]` (if you got a git account) or download the zip version, then navigate to `roman` directory.

2. Open `test_roman.py`

3. Paste your `toRoman(n: int)` function **under the comment** that says:

   ```python
   # PLACE YOUR CODE/FUNCTION UNDER HERE !!!
   ```

4. Make sure your function is named `toRoman`.  
   If not, update this line:

   ```python
   result = toRoman(num)
   ```

4. If you're on Windows or the CSV path is different, update:

   ```python
   path='testset_roman.csv'
   ```

5. Run the script:

   ```bash
   python test_roman.py
   ```

---

## ✅ What it does

- Loads the correct Roman numeral results from `testset_roman.csv`
- Runs your function on every number from `1` to `9999`
- Compares your output against the correct one
- If it **passes all tests**, you'll see:

  ```
  ✅ AC (Accepted) — all outputs match the testset!
  ```

- If it **fails**, it shows the **first 15 mismatches** like:

  ```
  number 444: expected 'CDXLIV', got 'CDLXXXXIV'
  ```

---

## 🛠 Notes

- This is based on **my own implementation**.
- If **my submission fails** when the grading portal opens, I’ll update the testset to a verified AC version — don’t worry.
- If you want to test **all the way up to 9999**, there’s a boolean flag in the dataset generator. Just set it to `True`.

---

## 💀 Final Tips

- Fix the first 15 mistakes the script shows
- Rerun the test — more may show up 💀
- Keep going until you get:

  ```
  ✅ AC
  ```

---

Good luck and hope this helps you get an AC 🙏
