import random

# version 0.1

# format
# dinnerPref mainDesc mainFood
# with a side of sideDish
# bevPref

# dinner generation starts

dinnerPref  = ['Tonight\'s dinner in the mind palace will be',
'Dinner tonight is',
'Dinner is served!']
print(random.choice(dinnerPref), end=' ')

mainDesc = ['lemon pepper',
'peppercorn',
'hot n\' spicy BBQ',
'plain',
'tikka masala',
'xtra cheezy',            
'Japanese golden curry',
'grilled and salted',            
'buffalo sauce-dipped',            
'Kung Pao']                
print(random.choice(mainDesc), end=' ')

mainFood = ['baked chicken',
'dinosaur chicken nuggets',
'impossible tacos',
'impossible steak',
'impossible burger',
'turkey sausage',
'udon noodles',
'ramen',
'spiral pasta',            
'potatoes',            
'bean burger',            
'tofu']
print(random.choice(mainFood), end=' ')

print ('with a side of')

sideDish = ['mashed potatoes',
'steamed green beans',
'curly fries',
'a chips ahoy cookie',
'a handfull of pixie stix',            
'a snickers',
'a dinner roll',
'a whole wheat dinner roll',
'a warm buttered dinner roll',            
'a pickle',            
'Busch\'s Grillin\' Beans',            
'dinosaur chicken nuggets',
'a pizza bagel',            
'a plain bagel'] 
print(random.choice(sideDish), end=' ')

bevPref = [', and a tall glass of',
', and a small glass of',
', and a glass of',
', and a mason jar full of',
', and a big glass of',
', and a cup of',           
', for a beverage,',
', and a refreshing glass of'] 
print(random.choice(bevPref), end=' ') 

bev = ['sparking lemon water',
'MTN DEW CODE RED',
'water',
'sparkling apple cider',
'sparkling grape cider',
'sparkling pear cider',
'sparkling cranberry cider',
'ancient fruit wine',       
'oat milk',
'almond milk',
'unsweetened almond milk',
'vanilla almond milk',
'chocolate almond milk'] 
print(random.choice(bev))             
