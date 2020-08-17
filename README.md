# Magic Passes
This is a simple script to solve the next problem:  
>The wizards at the magic academy are having trouble saying their magic passes because they can't calculate remains. Help them!
>
>To say spells they first have to count to a number but if the number is multiple of 3 replace it with "abracadabra" and if the number is multiple of 5 replace it with "alakazam". If it is a multiple of 3 and 5 they have to say "abracadabraalakazam".
>
>Make a python script that receives the number they have to reach and print out what magic words they have to say before their spell.


## Environment
I make this in a docker just for fun and to improve the recipe I have.  
You can install Docker on your system folowing the [next steps](https://docs.docker.com/get-docker/).
```bash
$ git clone https://github.com/galloramiro/magic-passes.git
$ cd magic-passes/docker
$ bash build_docker.sh
$ bash run_docker.sh
```
Now in the jupyter notebook go to the magic-passes folder and open the try-it.ipynb and give enter.   
  
This code have basic unit tests and one integration test.   
If you want to run the tests open a console on the proyect folder and run the folowing command:
```bash
$ docker exec magic_passes pytest -vv
```