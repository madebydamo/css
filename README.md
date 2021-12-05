# css
Create pedestrain social forces model and train them for efficency
## Run a simulation
First we need to set up the environment. We used [pipenv](https://github.com/pypa/pipenv)
```
pipenv install
pipenv shell
```
Before running a simulation you can chose between different models (in models folder) and different scenes (in scene folder)
The model must be set in train.py. Import therefore the desired model like this:
```
from models import simple as simulationcase#select model. Can be {simple, fov}
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

