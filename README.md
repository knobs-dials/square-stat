# squarestuff

Text-shell squarified treemaps presenting things like CPU and memory use - in text shells.

Tries to group some known process sets, e.g. 
- filesystem-related processes
- other kernel stuff
- systemd stuff 
- various GNOME stuff 
- small-use processes into 'sumsmaller' so they don't fall away (still tends to be tiny)
...all mostly because a shell isn't exactly high resolution, and this is for a glanced overview.

![CPU and memory, split in tmux](/screenshots/squarestuff.png?raw=true)


### Dependencies
- curses
- [squarify](https://github.com/laserson/squarify) (python package)   
- [smem](https://www.selenic.com/smem/) CLI tool (optional)


### square-cpu

Shows overall percentage. Sums to ~100%, regardless of core amount.


### square-mem

This one's a test, because
- getting things like shared memory right is important to accuracy in some uses. One good example is postgres workers extensively using shared memory for table data, so just  processes' mapped total would over-report use more than a little. Also sums up to total memory would look weird. The smem tool fixes this, but is slowish and CPU-heavy. Which is why this isn't the default right now.
- how things like buffers, caches, slab, etc sum up and are best reported varies. Also because of practice - it e.g. out that ZFS ARC reports as unreclaimable slab.

### TODO
- learn curses better
    - stop misunderstanding curses colors
    - fix layouting bugs (it's integer rounding things)
    - fix redrawing

### square-swap


