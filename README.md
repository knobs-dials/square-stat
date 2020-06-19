# squarestuff

Text-shell squarified treemaps presenting things like CPU and memory use - in text shells.

Tries to group some known process sets, e.g. kernel stuff, systemd stuff, and unknown-but-tiny ones into 'sumsmaller' so they don't fall away. A shell isn't exactly high resolution, and this is for a glanced overview.


Depends on the
- curses
- squarify (python package)   https://github.com/laserson/squarify
- smem CLI tool (optional)


In particular square-mem is an experiment, because getting things like shared memory right is important to accuracy in some uses.

One good example is postgres workers extensively using shared memory, and just adding processes' memory map figures would massively over-report its use, as well as the amount of memory there is.  But the tool we use to fix this, smem, is also very slow and sort of CPU-heavy. Which is why this isn't even the default right now.

TODO:
- learn curses better
    - stop misunderstanding curses colors
    - fix layouting bugs (it's integer rounding things)
    - fix redrawing

![CPU and memory, split in tmux](/screenshots/squarestuff.png?raw=true)

