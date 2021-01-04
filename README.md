# Festo Coding Challenge 2020

If you haven't taken up the challenge yet, please do, before reading on. The [challenge is here](https://coding-challenge.festo.com/)

This repository contains the challenge's puzzles and encourages everyone to upload and share their solutions.

To do so, please fork this repository and push your code into your fork. That way, everyone can easily find your solution.


Our own solutions to the puzzles are [available here](https://github.com/MichaelSinsbeck/festo-coding-challenge-2020-solutions).

## 1-1 Maintenance Man - Five XOR Seven

The maintenance man is tired of following the complicated rules enforced by the management. He will give you a clue about the password if you help him solve his problem:

The maintenance man is responsible for delivering the internal mail to all employees. In the company, there are different buildings with different room numbering schemes. In the first building, room numbers must contain a digit 5 or a digit 7, but not both of them. For example 5, 17, 52, 55, 177 are all valid room numbers, but 24, 157 or 7005 are not.

All rooms in the building are placed on one very long hallway. All valid room numbers are - of course - arranged in ascending order: 5, 7, 15 , 17 ...

The maintenance man needs to bring mail to the 1000th room in the hallway. What is the room number of this room?

## 1-2 System Admin - Christmas Cards

The system admin has long working hours. If we help him save time, he will help us.

Before he can go home today, he wants to deliver some christmas cards to his eights friends (Alice, Bob, Carla, David, Erica, Frank, Grace, Henry) who live nearby. His trip after work will look like this: work - friend - friend - ... - friend - home.

He knows how much time (in minutes) he needs for the individual distances:

        work  a   b   c   d   e   f   g   h  home
    work  -   6  10   4   1   9   2   9   7   -
       a  -   -   8   7   4   3   5   5  12   5
       b  -  11   -  16  12  11  10   5  20  15
       c  -   7  13   -   3  10   5  11   4   5
       d  -   4  10   3   -   8   2   8   7   5
       e  -   3   8  11   8   -   8   4  15   7
       f  -   5   8   6   2   8   -   7  10   7
       g  -   6   4  13  10   6   8   -  17  11
       h  -  10  16   3   6  14   8  15   -   8
    home  -   -   -   -   -   -   -   -   -   -

Labels on the left: starting points, labels on the top: destinations. For example, the trip from work to Alice (a) takes 6 minutes. Useless connections are left empty. Download [table as csv](files/1_2_christmas_cards.csv).

In what order should the system admin visit his friends to minimize the overall time of this trip? The solution code consists of the lowercase initials of the friends in optimal order (for example **adhbcgfe**).

## 1-3 The Boss - Social Distance Office

The boss is charged with a lot of tasks he does not actually want to do. If we do some of the tasks for him, he will provide us some clues. All of the bosses tasks can be solved with a pencil and a sharp mind. No coding required.

Even in THE EVIL COMPANY, social distance rules have to be obeyed. The latest task of the boss is to organize the office space to guarantee a safe and healthy environment. Furthermore, his employees have to sit in the correct cubicles.

Find the correct sitting order in the office.

Download [puzzle as pdf](files/1_3_social_distance_office.pdf).

Solution code: for each row in the diagram count the number of spaces between the two chairs. Concatenate all eight numbers to get the solution code.

## 1-4 Mystery Man - Follow the Trace

Mystery man does not speak much. He does not explain the rules.

By the way, did you check out the [blog of our intern](https://coding-challenge.festo.com/blog/)?

## 2-1 Maintenance Man - No More 2020

The year 2020 has been a terrible year for many industries, including the organized crime. Therefore, the management of THE EVIL COMPANY does not want to be reminded of the number 2020 in any kind of way.

In the second building of the company, the following number scheme applies: A room number must not contain the digits 2-0-2-0 in this order, not even if there are more digits in between.

For example, these numbers are not allowed any more: 2020, 20201, 205420, 20020, 12101020, whereas these numbers, for example, are still ok: 1, 2, 3, 7, 20, 200, 2021, 2002, 10022.

Oh, and of course, the first room number is 1, not 0.

The maintenance man needs to bring mail to the 1,000,000th room in the hallway. What is the room number of this room?

## 2-2 System Admin - Christmas Shopping

The other night, the system admin needs to buy some things on this way home. He needs to visit a super market (s), a pharmacy (p), a hardware store (h), a drug store (d) and a toy store (t). In the city, there are two shops of each type: s1, s2, p1, p2, h1, h2, d1, d2, t1, t2. Travel times:

         work s1  s2  p1  p2  h1  h2  d1  d2  t1  t2 home
     work  -   7  22  18  16  20  18  19  10  22   3   -
       s1  -   -   -  18  14  20  14  12   5  16   5  25
       s2  -   -   -  19  14  20  12   3  10   6  17  10
       p1  -  19  23   -   -   2   8  23  14  17  15  25
       p2  -  15  17   -   -   6   2  17   9  11  12  20
       h1  -  21  23   2   7   -   -  24  16  17  17  24
       h2  -  14  14   7   2   -   -  14   8   8  13  17
       d1  -  10   3  20  14  21  13   -   -   8  15  13
       d2  -   5  12  13   9  15   8   -   -  11   6  20
       t1  -  15   7  14   9  14   7   8  10   -   -   9
       t2  -   7  20  14  13  17  14  18   8   -   -  28
     home  -   -   -   -   -   -   -   -   -   -   -   -
     
Labels on the left: starting points, labels on the top: destinations. For example, the trip from super market 2 (s2) to pharmacy 1 (p1) takes 19 minutes. Useless connections are left empty. Download [table as csv](files/2_2_christmas_shopping.csv).

Find the shortest trip work - shop - shop - shop - shop - shop - home, such that each shop type is visited exactly once, in any order.

The solution code consists of the labels of the shops visited, in optimal order (for example p1s1h2d1t2).

## 2-3 The Boss - Crossword

The boss wants a new TV for his kids. But he does not want to pay for it. In a computer magazine, he finds a crossword puzzle with a TV as a prize. He wants to participate in the lottery, but finds the puzzle too hard. Can you help him solve it?

Download [puzzle as pdf](files/2_3_crossword.pdf).

Solution code: all nine characters, in normal reading order (left to right, top to bottom)

## 2-4 Mystery Man - Lyrics

A Rockstar knows, mystery is here. I feel my heart

the challenge was determined. absolutely sharp

Put it with mystery into victory

Shout victory

## 3-1 Maintenance Man - Prime Time

In the third building of the company, room numbers follow this rule: A number can only be a room number, if its only prime factors are 7, 11 and 13.

For example, the first valid room numbers are 1, 7, 11, 13, 49, 77, 91, 121, 143, 169,...

The maintenance man needs to bring mail to the 200th room in the hallway. What is the room number of this room?

## 3-2 System Admin - Food Delivery

To make up for his poor salary at THE EVIL COMPANY, the system admin works for a food delivery service on the way home. His job is to pick up meals from the five restaurants (r1,...,r5) in any order and bring them to the corresponding customers (c1,...,c5). After picking up one meal, he does not have to drive to the customer immediately. He can also pick up multiple meals first and then deliver them. The only constraint is that, on his bike, he can only carry three meals max. Travel times:

        work r1  r2  r3  r4  r5  c1  c2  c3  c4  c5 home
    work  -   6   3  22  20  10   -   -   -   -   -   -
      r1  -   -   5  28  18   4  22  17   8  23  26   -
      r2  -   4   -  23  18   7  17  12   8  19  21   -
      r3  -  25  21   -  21  27   5  17  22   6   4   -
      r4  -  20  20  25   -  16  19  28  10  17  26   -
      r5  -   5   9  30  16   -  23  21   6  24  28   -
      c1  -   -  16   6  16  21   -  14  16   3   6  16
      c2  -  14   -  17  24  17  14   -  17  17  14  15
      c3  -   9  10   -  10   6  19  21   -  18  24   3
      c4  -  22  18   8   -  22   4  19  16   -  10  17
      c5  -  23  18   4  22   -   5  13  21   8   -  20
    home  -   -   -   -   -   -   -   -   -   -   -   -
    
Labels on the left: starting points, labels on the top: destinations. For example, the trip from r3 to r4 takes 21 minutes. Useless connections are left empty. Download [table as csv](files/3_2_delivery_service.csv).

Find the shortest trip work - restaurant - ? - ? - ... - customer - home, such that each restaurant is visited before the corresponding customer and that the system admin never has more than three meals on his bike.

The solution code consists of the restaurants and customers in order (for example r1c1r2r3r4c2c4r5c5c3)

## 3-3 The Boss - Cable Spaghetti

The boss got a new laptop. But he is not good at technology, so he struggles putting in the cables into the correct plugs. Can you help him?

Download [puzzle as pdf](files/3_3_cable_spaghetti.pdf).

Solution code: The length of the screen cable, followed by the length of the mouse cable, followed by the length of the headphones cable. Length means number of line segments. The example puzzle has lengths 6 and 10. This would make for the code 610.

## 3-4 Mystery Man - Imagine

The code is hidden in the image on the page that does not exist.

