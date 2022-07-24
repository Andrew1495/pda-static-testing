### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# else is missing a :   should be else:
# should be if card.value == 1:
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# dif should be spelt def
# return card should be card 1
# missing comma after card1 in arguments
# if and else need indedented 
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# total is not declared to be anything so total += means nothing to python also don't think you
# can only concatenate str not and total is a int 
# whole function needs indented
# return is inside for loop
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
