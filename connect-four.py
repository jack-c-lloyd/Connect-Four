# Copyright (c) 2024 Jack C. Lloyd

import random

DISC_PLAYER_ONE = '\u25CB'
DISC_PLAYER_TWO = '\u25CF'
SLOT_EMPTY = '\u25CC'

COLUMNS, ROWS = 7, 6
Board = [[SLOT_EMPTY for _ in range(ROWS)] for _ in range(COLUMNS)]

PlayerOneName = ""
PlayerTwoName = ""
PlayerOneScore = 0
PlayerTwoScore = 0
PlayerOneTurn = True
HasWonOrDrawn = False
Answer = ''

def PlayerDisc(IsPlayerOne):
	if IsPlayerOne:
		return DISC_PLAYER_ONE
	else:
		return DISC_PLAYER_TWO

def PlayerName(IsPlayerOne):
	if IsPlayerOne:
		return PlayerOneName
	else:
		return PlayerTwoName

def PrintScore():
	print(PlayerOneName + ": " + str(PlayerOneScore))
	print(PlayerTwoName + ": " + str(PlayerTwoScore))
	print()

def ClearBoard(Board):
	for Column in range(COLUMNS):
		for Row in range(ROWS):
			Board[Column][Row] = SLOT_EMPTY

def PrintBoard(Board):
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

def TrySlot(Board, Slot, Disc):
	if not ValidSlot(Slot):
		print("Slot " + Slot + " is invalid!")
		return False
	Column = int(Slot) - 1 # Index
	for Row in range(ROWS):
		if Board[Column][Row] is SLOT_EMPTY:
			Board[Column][Row] = Disc
			return True
	else:
		print("Slot " + Slot + " is full!")
		return False

def CheckHorizontal(Board, Disc):
	for Column in range(COLUMNS - 3):
		for Row in range(ROWS):
			for Count in range(Column, Column + 4):
				if Board[Count][Row] != Disc:
					break
			else:
				return True
	else:
		return False

def CheckVertical(Board, Disc):
	for Column in range(COLUMNS):
		for Row in range(ROWS - 3):
			for Count in range(Row, Row + 4):
				if Board[Column][Count] != Disc:
					break
			else:
				return True
	else:
		return False

def CheckDiagonal(Board, Disc):
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

def CheckWin(Board, Disc):
	if CheckHorizontal(Board, Disc):
		return True
	elif CheckVertical(Board, Disc):
		return True
	elif CheckDiagonal(Board, Disc):
		return True
	else:
		return False

def CheckDraw(Board):
	for Column in range(COLUMNS):
		for Row in range(ROWS):
			if Board[Column][Row] == SLOT_EMPTY:
				return False
	else:
		return True

def FlipCoin():
	return random.random() < 0.5

if __name__ == "__main__":
	PlayerOneName = input("Enter the name of player one: ")
	PlayerTwoName = input("Enter the name of player two: ")
	PlayerOneTurn = FlipCoin()
	while Answer not in ['N', 'n']:
		print(PlayerName(PlayerOneTurn) + " starts!")
		ClearBoard(Board)
		PrintBoard(Board)
		HasWonOrDrawn = False
		while not HasWonOrDrawn:
			Slot = input(PlayerName(PlayerOneTurn) + ", enter a slot: ")
			while not TrySlot(Board, Slot, PlayerDisc(PlayerOneTurn)):
				Slot = input("Enter another slot: ")
			PrintBoard(Board)
			if CheckWin(Board, PlayerDisc(PlayerOneTurn)):
				if PlayerOneTurn:
					PlayerOneScore += 1
				else:
					PlayerTwoScore += 1
				print(PlayerName(PlayerOneTurn) + " wins!\n")
				HasWonOrDrawn = True
			elif CheckDraw(Board):
				print("Draw!\n")
				HasWonOrDrawn = True
			PlayerOneTurn = not PlayerOneTurn
		PrintScore()
		Answer = input("Play again?\nY/N: ")