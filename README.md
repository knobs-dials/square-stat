# squarestuff

Experiment with squarified treemaps representing things like CPU and memory use - in text shells.

Tries to group some known cases, in particular a bunch of kernel stuff into a group called kernel.

Depends on the
- curses
- squarify (python package)   https://github.com/laserson/squarify
- smem CLI tool (optional)


In particular square-mem is an experiment, because getting things like shared memory right is important to accuracy in some uses.

One good example is how postgres workers extensively use shared memory, and without considering this you would massively over-report. But the tool we use for this, smem, is also very slow and sort of CPU-heavy.



Again, it's an experiment. There are various known bugs. 
Not least of which is my misunderstanding of curses colors. And layout.

![CPU screenshot](/screenshots/square-cpu.png?raw=true)

![memory screenshot](/screenshots/square-mem.png?raw=true)
