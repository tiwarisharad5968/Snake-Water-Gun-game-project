# Snake Water Gun 🎮

A simple and readable Python project created during my learning phase to simulate the classic **Snake-Water-Gun** game (an Indian twist on Rock-Paper-Scissors).

## 🧠 Game Rules

- **Snake drinks Water** 🐍 > 💧 → Snake Wins
- **Water douses Gun** 💧 > 🔫 → Water Wins
- **Gun kills Snake** 🔫 > 🐍 → Gun Wins

### Rule Summary:
| Player vs Computer | Outcome        |
|--------------------|----------------|
| Same Choice        | Draw           |
| Snake vs Water     | Snake Wins     |
| Water vs Gun       | Water Wins     |
| Gun vs Snake       | Gun Wins       |
| and vice-versa     | You either win or lose accordingly |

---

## 👨‍💻 How It Works

- Computer makes a random choice (`Snake`, `Water`, or `Gun`).
- You enter your choice using:
  - `S` for Snake
  - `W` for Water
  - `G` for Gun
- The program compares and tells you the result.

---

## 🏗️ Code Highlights

- Clean and beginner-friendly logic.
- Uses dictionaries for input mapping.
- Uses `random.choice()` for computer behavior.
- Fully covers all win/loss/draw conditions.

---

## 🚀 How to Run

Make sure you have Python installed, then:

```bash
python Main.py
