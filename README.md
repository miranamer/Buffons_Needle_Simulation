# Buffons Needle Simulation

<h1>What It Is?</h1>
In probability theory, Buffon's needle problem is a question first posed in the 18th century by Georges-Louis Leclerc, Comte de Buffon

Suppose we have a floor made of parallel strips of wood, each the same width, and we drop a needle onto the floor. What is the probability that the needle will lie across a line between two strips?
Buffon's needle was the earliest problem in geometric probability to be solved; it can be solved using integral geometry.

It can be used to estimate $\pi$ although I just simulated the needle crossing validation to check how many crossed and to practice matplotlib.


<h1>How It Works</h1>
<ol>
  <li>Needles Are Generated</li>
  <li>Needles are then validated to check which needle crosses a boundary</li>
</ol>

<h1>Needle Generation</h1>
<ul>
  <li>All needles need to be of the same size - some size 'L' where L is <i>usually</i> some factor of t (the distance between boundaries) but not necessarily</li>
</ul>

In order to generate needles of a constant length with random positions and directions I had to use some trigonometry (as follows):

<strong>Pythagoras' Theorem:</strong>
$a^2+b^2 = c^2$. Where $a = \Delta x$ and $b = \Delta y$. Therefore, $a = x_{2} - x_{1}$ and $b = y_{2} - y_{1}$.



![Blank diagram - Page 1](https://user-images.githubusercontent.com/91673777/236015668-6459f1ab-32ff-40d5-9cba-c0529e5ce230.png)





We will randomly generate an $x_{1}$, $y_{1}$ and $x_{2}$ coordinates but we will have to solve for $y_{2}$ such that a given $y_{2}$ will cause the $\left | c \right | = L$. This will cause the needle length to be constant but allow randomly placed needles.

Therefore, Point 1 = ($x_{1}, y_{1}$) and Point 2 = ($x_{2}, y_{2}$) where $x_{1}$, $y_{1}$ and $x_{2}$ are randomly generated => $x_{1}, x_{2}, y_{1}\in Random()$ and $y_{2}$ will be trigonometrically determined.

Therefore, in order to ensure the needle is a constant length (magnitude as its a vector), we just need to ensure that the longest side of the triangle is always equal to L.
In other words: 
$c = L$

Therefore, we need to solve for $b$ which can then be re-arranged to give us our $y_{2}$ coordinate.

1. So we know that $a^2+b^2 = L^2$ as $c = L$ therefore when we re-arrange for b we get: $\sqrt{L^2 - a^2} = b$
2. Then we can re-arrange $b$ for $y_{2}$ -> $b+y_{1} = y_{2}$
3. So we are left with: $y_{2} = \sqrt{L^2 - a^2} + y_{1}$

I have also added some constraints to ensure that C is always positive as it made it easier to have a +ve slope rather than a -ve one. This does however limit the number of angles formed.


<h1>Validate Crossings</h1>
<ul>
  <li>Any needle that crosses a boundary must be highlighted as red</li>
</ul>

<strong>Diagram Example:</strong>



![Blank diagram - Page 1 (1)](https://user-images.githubusercontent.com/91673777/236018695-994497b9-9e8c-4884-b9b4-9cb520b1932d.png)



The distance between sections will be a constant $T$.

In order to evaluate as to whether or not a needle crosses, I will check the $x-coordinates$ of both $Point_{1}$ & $Point_{2}$ and if the coordinates are in the same section (slice between 2 boundaries) then they are not crossing,
However, if they are in different sections, then it means that needle is crossing as it's $x-coordinates$ are in different slices along the graph therefore there must be an overlap.

In order to check if a given $x-coordinate$ is in a section I will first need to define the range of values for each section and the number of sections.

Example:



![Blank diagram - Page 1 (2)](https://user-images.githubusercontent.com/91673777/236021099-f4a88a17-269b-49af-9058-2e067a0d3ebb.png)



In this Example diagram, T=4 so the slices are spaced by 4 units on the $x-axis$ therefore I know the range of coordinates possible in a given section.
Now, in order to check if there is a crossing, I just have to iterate over all the needles, check the sections of both $x_{1}$ and $x_{2}$ for the needle and see if they lie in the same range e.g $x_{1} range = (4-8),  x_{2} range = (4-8)$ or 
if the ranges vary e.g $x_{1} range = (4-8),  x_{2} range = (8-12)$

Example:



![Blank diagram - Page 1 (3)](https://user-images.githubusercontent.com/91673777/236025081-0df5e34c-3a70-403f-beb1-84804cb23316.png)



Table:



![Blank diagram - Page 1 (4)](https://user-images.githubusercontent.com/91673777/236025314-43063c50-41c9-4020-bbfd-32d68fce7320.png)



As both the blue lines x-coords are in the same range, they are not crossing, however, the red lines x-coords vary therefore it crosses.




<strong>Edge Case:</strong>
As the end values in the ranges repeat and are present in 2 ranges, e.g: (4-8) and (8-12) has 8 twice, I simply check if there is a single overlap in slices and if there is, there is no crossing.


Example Of Edge Case:


![Blank diagram - Page 1 (6)](https://user-images.githubusercontent.com/91673777/236027439-019d3732-f6ef-471f-ab6a-085e444a10f8.png)



Table:



![Blank diagram - Page 1 (5)](https://user-images.githubusercontent.com/91673777/236027293-167a93ea-6ea0-4979-bf10-1c61df85d656.png)


As there's an overlap in the ranges, they do not cross despite the fact that each x-coord appears in 2 ranges.

Graphed Result:



![image](https://user-images.githubusercontent.com/91673777/236029321-4323bd26-0446-4e2b-aafb-0ef1e7d1e142.png)





