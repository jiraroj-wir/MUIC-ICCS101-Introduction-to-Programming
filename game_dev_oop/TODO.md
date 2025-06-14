# TODOs [14/06/2025]

## 🍬 Pill Feature

- [ ] Import `Pill` class into the game.
- [ ] Create a new `self.pill` object in the `reset()` method of the `Game` class.
- [ ] In the `update()` method of the `Game` class:
  - [ ] Call `self.pill.draw()`.
  - [ ] Add logic for when the snake eats the pill:
    - [ ] Decrease the score by **50**.
    - [ ] Shrink the snake by **2 segments**, but ensure its length doesn’t go below 1.
    - [ ] Respawn the pill at a random location.

---

## 🪙 Coin Feature

- [ ] Create a new class `Coin`. It should:
  - [ ] Be similar to `Food`.
  - [ ] Use `assets/coin.jpg` for display.
  - [ ] Play sound from `assets/sfx2.wav` on collection.
- [ ] In the `reset()` method of `Game`:
  - [ ] Create **5** instances of `Coin` and store them in `self.coins`.
- [ ] In the `update()` method of `Game`:
  - [ ] Check if the snake has collected any coin.
    - [ ] If collected, increase score by **500**.
    - [ ] Respawn the coin at a new random location.
  - [ ] Call the `draw()` method for each coin.

---
## 👾 changes
> Eating a coin should not kill the snake, should it? Any penalty?

---

## 🐛 Bug Fix

- [ ] Fix "last row" bug where the snake leaves a trail when moving through the last row.
