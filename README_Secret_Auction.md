# 💰 Secret Auction Program – Python Project

Welcome to the **Secret Auction System**, a Python-based terminal project that simulates a private bidding environment. This program allows multiple users to place secret bids, and in the end, the highest bidder is revealed as the winner! 🏆

---

## 🧾 Features

- ✅ Accepts multiple users' names and bid amounts
- ✅ Keeps all bids secret until the end
- ✅ Automatically determines and displays the highest bidder
- ✅ Handles input validation for repeat entries
- ✅ Includes a custom ASCII-art auction logo on startup

---

## 🛠️ How It Works

1️⃣ The program starts with a logo and welcome message  
2️⃣ It prompts users one by one for their name and bid  
3️⃣ Bidding continues until no further participants  
4️⃣ The program finds the highest bidder and declares the winner

---

## 📂 File Structure

```
secret-auction/
├── program.py         # Main bidding logic and input handling
├── art.py             # Contains the ASCII logo (imported in program.py)
├── screenshot.png     # Sample output from the terminal
└── README.md          # Project documentation
```

---

## 🖥️ Sample Execution

```
Welcome to the secret auction program.
What is your name?: Alice
What's your bid?: $200
Are there any other bidders? Type 'yes' or 'no': yes

What is your name?: Bob
What's your bid?: $300
Are there any other bidders? Type 'yes' or 'no': no

The winner is Bob with a bid of $300
```

> 📌 All previous inputs are cleared between entries to keep the auction secret and fair.

---

## 🚀 How to Run

### Requirements:
- Python 3.x

### Steps:
```bash
git clone https://github.com/your-username/secret-auction.git
cd secret-auction
python program.py
```

---

## 💡 Learning Highlights

- Dictionary usage for storing bids
- Looping and input validation
- Working with functions and conditionals
- Creating a realistic bidding system experience

---