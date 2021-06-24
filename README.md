# TSP-SOM
Solving TSP with self-organizing map.
# explanation
- solved TSP with self-organizing map for the berlin59 dataset. the best path which the algorithm calculates is 1620.
- I put analysis for each parameter but it is in persian.
# algorithm
We cut the starting points by shifting to a single square starting at the origin. Then we place a neuron twice the number of cities on a circle to the center (0.5 and 0.5) and a radius of 0.5, which defines a circle. Then in each stage a city is randomly selected and the nearest neuron is found as the winner and its neighboring neurons and itself are updated by the following formula.

W(new, i) = W(old, i) + alpha x (X(i)- W(old, i)

Finally, for each city, we consider the nearest neuron as a substitute for that city, and build the path in the order that the neurons previously had.


![image W6AH50](https://user-images.githubusercontent.com/47561586/123282985-316f9c80-d520-11eb-8af8-f8534b2d8feb.png)

- Degree of learning: The degree of learning is constant during the performance. It has a number between 0 and 1.
- Neighborhood Radius: At each stage, each winning neuron and its neighbors change to a distance of R. It is better to change the neighborhood radius during the performance.
- End of algorithm: The algorithm terminates after iteration.
