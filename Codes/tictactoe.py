from tkinter import *
import tkinter.messagebox

# Create a instance of TK() this is going to let us use T kenter's method
root = tkinter.Tk()
# Change the icon of window and put it our tic-tac-toe icon
root.iconbitmap("C:\\Users\\MANASI\\Desktop\\Jarvis\\Games\\tic-tac-toe.ico")
# Change the title of window
root.title('Tic-Tac-Toe')
# It take 2 parameters one for width and one for height false means u cannot resize it
root.resizable(False, False)
click = True
# Keep the track of how many moves have been made so in tic-tac-toe we have 9 moves so if it already in 9th move it
# means it is tie
count = 0

# Text variable are associated with widgets in tkinter in our case we are going to associate these text variables
# With our buttons we are going to create total 9 buttons so we are going to create a total of nine text variable So
# if we click on button number one we are going to set the text variable associated with button number one to X and so
# on
btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

# Store image in the variables
xPhoto = PhotoImage(file='C:\\Users\\MANASI\\Desktop\\Jarvis\\Games\\X.png')
oPhoto = PhotoImage(file='C:\\Users\\MANASI\\Desktop\\Jarvis\\Games\\O.png')


# This play function contain the total 9 buttons that we need to play
def playtictaktoe():
    global xPhoto
    global oPhoto
    button1 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#f2e6ff', textvariable=btn1,
                     # Set height width and all parameter for buttons relief is for border
                     command=lambda: press(1, 0, 0))
    # In ridge style bg is for background color text variable is for type X or O so when user want to click buttons we want to
    # Click buttons we want to something happen to do that we have to type command = lambda it allows us to call on a function on
    # Press function same for all buttons.
    # Location of buttons same for all
    button1.grid(row=0, column=0)

    button2 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#f2e6ff', textvariable=btn2,
                     command=lambda: press(2, 0, 1))
    button2.grid(row=0, column=1)

    button3 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#f2e6ff', textvariable=btn3,
                     command=lambda: press(3, 0, 2))
    button3.grid(row=0, column=2)

    button4 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#d9b3ff', textvariable=btn4,
                     command=lambda: press(4, 1, 0))
    button4.grid(row=1, column=0)

    button5 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#d9b3ff', textvariable=btn5,
                     command=lambda: press(5, 1, 1))
    button5.grid(row=1, column=1)

    button6 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#d9b3ff', textvariable=btn6,
                     command=lambda: press(6, 1, 2))
    button6.grid(row=1, column=2)

    button7 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#bf80ff', textvariable=btn7,
                     command=lambda: press(7, 2, 0))
    button7.grid(row=2, column=0)

    button8 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#bf80ff', textvariable=btn8,
                     command=lambda: press(8, 2, 1))
    button8.grid(row=2, column=1)

    button9 = Button(root, height=9, width=19, bd=.5, relief='ridge', bg='#bf80ff', textvariable=btn9,
                     command=lambda: press(9, 2, 2))
    button9.grid(row=2, column=2)


# R for row and C for column
def press(num, r, c):
    global click, count
    if click == True:
        # Label class first parameter is name of our window and we want this label
        # To have a particular image of x
        labelPhoto = Label(root, image=xPhoto)
        # For the location of buttons and we used it here so we are placing this pic
        # In place of that button
        labelPhoto.grid(row=r, column=c)
        # If num==1 the we set the text variable for that particular button in this case it would be
        # Button number one to X and doing for every button
        if num == 1:
            btn1.set('X')
        elif num == 2:
            btn2.set('X')
        elif num == 3:
            btn3.set('X')
        elif num == 4:
            btn4.set('X')
        elif num == 5:
            btn5.set('X')
        elif num == 6:
            btn6.set('X')
        elif num == 7:
            btn7.set('X')
        elif num == 8:
            btn8.set('X')
        else:
            btn9.set('X')
        # Increase it because this point one move has been made
        count += 1
        # First is for x if it is true then it always print x only
        click = False
        checkWin()

    else:
        # Same as X we are here doing for O
        labelPhoto = Label(root, image=oPhoto)
        labelPhoto.grid(row=r, column=c)
        if num == 1:
            btn1.set('O')
        elif num == 2:
            btn2.set('O')
        elif num == 3:
            btn3.set('O')
        elif num == 4:
            btn4.set('O')
        elif num == 5:
            btn5.set('O')
        elif num == 6:
            btn6.set('O')
        elif num == 7:
            btn7.set('O')
        elif num == 8:
            btn8.set('O')
        else:
            btn9.set('O')
        count += 1
        # Turns go to X
        click = True
        checkWin()


# Check who won
def checkWin():
    global count, click

    # If x wins
    if (btn1.get() == 'X' and btn2.get() == 'X' and btn3.get() == 'X' or
            btn4.get() == 'X' and btn5.get() == 'X' and btn6.get() == 'X' or
            btn7.get() == 'X' and btn8.get() == 'X' and btn9.get() == 'X' or
            btn1.get() == 'X' and btn4.get() == 'X' and btn7.get() == 'X' or
            btn2.get() == 'X' and btn5.get() == 'X' and btn8.get() == 'X' or
            btn3.get() == 'X' and btn6.get() == 'X' and btn9.get() == 'X' or
            btn1.get() == 'X' and btn5.get() == 'X' and btn9.get() == 'X' or
            btn3.get() == 'X' and btn5.get() == 'X' and btn7.get() == 'X'):

        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'X Wins !')
        click = True
        count = 0
        clear()
        playtictaktoe()

    # If o wins
    elif (btn1.get() == 'O' and btn2.get() == 'O' and btn3.get() == 'O' or
          btn4.get() == 'O' and btn5.get() == 'O' and btn6.get() == 'O' or
          btn7.get() == 'O' and btn8.get() == 'O' and btn9.get() == 'O' or
          btn1.get() == 'O' and btn4.get() == 'O' and btn7.get() == 'O' or
          btn2.get() == 'O' and btn5.get() == 'O' and btn8.get() == 'O' or
          btn3.get() == 'O' and btn6.get() == 'O' and btn9.get() == 'O' or
          btn1.get() == 'O' and btn5.get() == 'O' and btn9.get() == 'O' or
          btn3.get() == 'O' and btn5.get() == 'O' and btn7.get() == 'O'):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'O Wins !')
        count = 0
        clear()
        playtictaktoe()

    elif (count == 9):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", 'Tie Game!')
        click = True
        count = 0
        clear()
        playtictaktoe()


# For clearing the game for next play
def clear():
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')


playtictaktoe()
# First method of t kenter's it is an event handler it's looking out for events like the click of a button
root.mainloop()
