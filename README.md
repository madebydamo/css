# Agent-Based Modeling and Social System Simulation 2021

> * Group Name: MLA (Machine Learning Avoiders, very ironic...)
> * Group participants names: Joël Andenmatten, Jan Grunder, Damian Moser
> * Project Title: Optimizing agent interaction in pedestrian model

## General Introduction

Due to robots being expensive and ever increasingly, owners may wish to rescue them as well in emergency situations.
We think about rescue of autonomous cars from tunnels or robot arms out of factories.

## The Model

We search optimal values for the parameters:
Interaction strenght and interaction range of interaction forces 1. between agents 2. between agent and obstacle
The relaxation time for an agent.

## Fundamental Questions

Can the social forces model combined with the genetic algorithm help us to find optimized parameters?
Is this simulation computationally feasible?

## Expected Results

There were no previous implications that the combination would not to yield reasonable results.
We were expecting that the interaction forces would take strength and range parameters, such that collisions would be avoided.

## References 

Books:
Social Self-Organization: Agent-Based Simulatons and Experiments to Study Emergent Social Behavior.

## Research Methods

Agent-Based Model, Social Force Model, Genetic Algorithm Optimization

## Run a simulation
First we need to set up the environment. We used [pipenv](https://github.com/pypa/pipenv)
```
pipenv install
pipenv shell
```
Before running a simulation you can chose between different models (in models folder) and different scenes (in scene folder)
The model must be set in train.py. Import therefore the desired model like this:
```
from models import simple as simulationcase #select model. Can be {simple, fov}
```
The scene must be set in simulation.py. Import therefore the desired model like this:
```
from scene import evacuate as scene #select scene. Can be {evacuate, crossing, lane, bottleneck}
```
To run a simulation call the following function in the project root folder:
```
python3 -m scoop train.py
```
Now the best creature of each generation gets saved in ./tmp/evol...
To view a simulation call the following code: (path to npy file must be modified accordingly)
```
pthon3 ui.py ./tmp/evol.../genxy.npy
```
Already generated data is in ./trained folder
For plotting data, look in the plot folder

