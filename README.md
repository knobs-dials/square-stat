# square-stat

(Proof of concept version, needs work)

Colored text-shell squarified treemaps presenting things like CPU and memory use.

Tries to group some known process sets, e.g. 
- filesystem-related kernel processes
- other kernel processes
- various graphical interface support stuff 
- tiny-use processes into 'sumsmaller' so they don't fall away (still tends to be small)

...all mostly because a shell isn't exactly high resolution, and this is for glanced overview.

![CPU and memory, split in tmux](/screenshots/squarestuff.png?raw=true)


### Dependencies
- curses
- [squarify](https://github.com/laserson/squarify) (python package, can install with `pip install squarify`)   
- [smem](https://www.selenic.com/smem/) CLI tool (optional)


### square-cpu

Shows overall percentage. Sums to ~100%, regardless of core amount.

Based on running `ps`


### square-mem

This one's a test, because
- counting kernel stuff *usefully* is nontrivial - consider buffers, caches, slab, etc, and how some details overlap, so how they are and are best reported. 
  - Also because of practice.  It e.g. turns out that in linux, ZFS ARC reports as unreclaimable slab - and is intentionally quite large.
- basic tools don't care abous shared memory at all
  - getting shared memory right is important to accuracy in some uses. One good example is postgresql workers, which extensively using shared memory for efficient sharing of table data.
  - ...in which case just adding up processes totals would over-report quite a lot. The sum of total memory, or free amount (from total-alluse) would also be noticably wrong.
  - The `smem` tool fixes this, but is slowish and CPU-heavy. Which is why this isn't the default right now.

Based on running `ps` or `smem`


### square-swap

Shows how swapped-out (/ allocated-in-swap) size, by program names.

Based on reading `/proc/*/status`


### TODO
- learn curses better
    - stop misunderstanding curses colors
    - fix layouting bugs (it's integer rounding things)
    - fix redrawing


