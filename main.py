import flet as ft
import random

wordBank = [
    "braulio", "pokemon", "college", "computer", "test", 
    "volleyball", "science", "engineer", "keyboard", "python",
    "programming", "mathematics", "software", "hardware", "developer"
]

def main(page: ft.Page):
    availableList = wordBank.copy()

    def getWord(e):
        nonlocal availableList
        if not availableList:
            availableList = wordBank.copy()

        if randomWord.value in availableList:
            availableList.remove(randomWord.value)

        if guessTextField.value == randomWord.value:
            rightOrWrong.value = "Correct!"
            rightOrWrong.color = "green"
        else:
            rightOrWrong.value = "Wrong..."
            rightOrWrong.color = "red"
            counter.value += 1

        if not availableList:
            availableList = wordBank.copy()

        randomWord.value = random.choice(availableList)
        page.update()

    counter = ft.Text(0)
    randomWord = ft.Text(random.choice(availableList))
    rightOrWrong = ft.Text("Status")
    guessTextField = ft.TextField(label="Guess the word:")

    page.add(
        randomWord,
        ft.Row(controls=[guessTextField, rightOrWrong]),
        ft.ElevatedButton("Test Word", on_click=getWord),
        ft.Row(controls=[ft.Text("Mistake Counter: "), counter])
    )
    

ft.app(target=main)