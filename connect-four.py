# Copyright (c) 2024 Jack C. Lloyd

import random

DISC_ONE = '\u25CB' # Red
DISC_TWO = '\u25CF' # Yellow
EMPTY    = '\u25CC'

COLUMNS, ROWS = 7, 6
Board = [[EMPTY for _ in range(ROWS)] for _ in range(COLUMNS)]

PlayerOneName = ""
PlayerTwoName = ""
PlayerOneScore = 0
PlayerTwoScore = 0

def PrintScore():
	print(PlayerOneName, PlayerOneScore)
	print(PlayerTwoName, PlayerTwoScore)
	print()

def ClearBoard():
	for Column in range(COLUMNS):
		for Row in range(ROWS):
			Board[Column][Row] = EMPTY

def PrintBoard():
	print() # Header
	print("  1 2 3 4 5 6 7  ")
	print("|---------------|")
	for Row in reversed(range(ROWS)):
		print('|', end=' ')
		for Column in range(COLUMNS):
			print(Board[Column][Row], end=' ')
		print('|')
	print("|---------------|")
	print() # Footer

def ValidSlot(Slot):
	Slots = [str(Count) for Count in range(1, COLUMNS + 1)]
	return Slot in Slots

def TrySlot(Slot, Disc):
	if not ValidSlot(Slot):
		print("Slot " + Slot + " is invalid!")
		return False
	Column = int(Slot) - 1 # Index
	for Row in range(ROWS):
		if Board[Column][Row] is EMPTY:
			Board[Column][Row] = Disc
			return True
	else:
		print("Slot " + Slot + " is full!")
		return False

def CheckHorizontal(Disc):
	for Column in range(COLUMNS - 3):
		for Row in range(ROWS):
			for Count in range(Column, Column + 4):
				if Board[Count][Row] != Disc:
					break
			else:
				return True
	else:
		return False

def CheckVertical(Disc):
	for Column in range(COLUMNS):
		for Row in range(ROWS - 3):
			for Count in range(Row, Row + 4):
				if Board[Column][Count] != Disc:
					break
			else:
				return True
	else:
		return False

def CheckDiagonal(Disc):
	for Column in range(COLUMNS - 3):
		for Row in range(ROWS - 3):
			for Count in range(4): # Forwards
				if Board[Column + Count][Row + Count] != Disc:
					break
			else:
				return True
			for Count in range(4): # Backwards
				if Board[Column + Count][Row + (3 - Count)] != Disc:
					break
			else:
				return True
	else:
		return False

def CheckWin(Disc):
	if CheckHorizontal(Disc):
		return True
	elif CheckVertical(Disc):
		return True
	elif CheckDiagonal(Disc):
		return True
	else:
		return False

def CheckDraw():
	for Column in range(COLUMNS):
		for Row in range(ROWS):
			if Board[Column][Row] == EMPTY:
				return False
	else:
		return True

def FlipCoin():
	return random.random() < 0.5

if __name__ == "__main__":
	PlayerOneName = input("Enter the name of player one: ")
	PlayerTwoName = input("Enter the name of player two: ")
	PlayerOneTurn = FlipCoin()
	Answer = ''
	while Answer not in ['N', 'n']:
		if PlayerOneTurn:
			print(PlayerOneName, "starts!")
		else:
			print(PlayerTwoName, "starts!")
		ClearBoard()
		PrintBoard()
		HasWonOrDrawn = False
		while not HasWonOrDrawn:
			if PlayerOneTurn:
				Name = PlayerOneName
				Disc = DISC_ONE
			else:
				Name = PlayerTwoName
				Disc = DISC_TWO
			Slot = input(Name + ", enter a slot: ")
			while not TrySlot(Slot, Disc):
				Slot = input(Name + ", enter another slot: ")
			PrintBoard()
			if CheckWin(Disc):
				HasWonOrDrawn = True
				if PlayerOneTurn:
					PlayerOneScore += 1
				else:
					PlayerTwoScore += 1
				print(Name, "wins!")
				print()
			elif CheckDraw():
				HasWonOrDrawn = True
				print("Draw!")
				print()
			else:
				PlayerOneTurn = not PlayerOneTurn
		PrintScore()
		print("Play again? (Y/N)")
		Answer = input("Answer: ")