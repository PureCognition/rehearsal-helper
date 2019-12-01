# rehearsal-helper
This is a small program I wrote to help my daughter practice her lines for her musical theater class.  It read the lines and stage directions that cue her speaking parts.  She then reads her parts and presses ENTER to continue.

# 12/1/2019 Update
Now that it's closer to my daughter's show, I wanted to see how well she memorized her lines.  So, I added a "check" mode.  You can pass in "check" or "read" (the default of nothing is passed in) as command line argument.  If you pass "check" then it will _not_ give the user their line up front, but instead it will prompt them to say it and then allow it to be checked afterwards.  Read mode works the way the application regular works by feeding the user the line up front.

This was a rushed update.  So, I'm hoping to refactor later.

## Here are the new ways to run to script
To run in check mode:
- python main.py check

To run in read mode:
- python main.py
- python main.py read

