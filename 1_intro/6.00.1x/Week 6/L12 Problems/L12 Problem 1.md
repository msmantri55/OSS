Consider the following code:

```
class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print self.incantation    


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print spell

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())
```

1. What are the parent class(es)? Note that the term "parent class" is interchangable with the term "superclass".

`Spell`

2. What are the child class(es)? Note that the term "child class" is interchangable with the term "subclass".

`Accio`, `Confundo`

3. What does the code print out? Try figuring it out in your head before you try running it in Python.

Hint: This code prints out 5 lines. Enter each line that is printed out in its own box, in sequential order.

    Accio

    Summoning Charm Accio

    No description

    Confundus Charm Confundo

    Causes the victim to become confused and befuddled.

4. Which `getDescription` method is called when `studySpell(Confundo())` is executed?

The getDescription method defined within the Confundo class

5. How do we need to modify `Accio` so that print `Accio()` will print the following description?

```
Summoning Charm Accio
This charm summons an object to the caster, potentially over a significant distance.
```

```
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'
```