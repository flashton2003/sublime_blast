# sublime_blast

A sublime text plugin for running BLAST on a nucleotide sequence file that is open in sublime text.

### Thought behind the plugin

Many, many times, I have a sequence file open in sublime text, and i want to know whether it contains a specific sequence. Ctrl-F works ok sometimes, but there are various issues, foremost, that it doesn't handle differences between your sequence of interest and the sequence in the file.

Sublime text has a rich ecosystem of plugins, and I thought it would be nice to add blast as one of them.

Essentially, the plugin takes the entire sequence that is in the open (by which I mean, current focus) sublime tab, writes it to a file in /tmp, makes a blast database of it. Then, it takes a query sequence (in form mentioned below), writes it to another file in /tmp, blasts the query vs the db, and prints the results at the bottom of the open tab.

### Pre-requisites

* Obviously, sublime text
* makeblastdb and blastn have to be in /usr/local/bin/, not just in your $PATH, system calls from within sublime text don't seem to look in the path in the usual way.


### current limitations

* the plugin is currently in an alpha state, all seems to work for me but ymmv.
* the output at the bottom of the open tab is a bit clunky, ideally it would open a new tab and put the output there. but this requires using the window api of sublime text, which is a bit beyond my boxing day hacking.
* there is no sanity checking of any input, errors will probably be silent.

### Install

Pull down the directory into the here:

`~/Library/Application Support/Sublime Text 3/Packages/`

### Usage

Within sublime text open the 'console', either through the view -> show console option or ctrl + `.

Then, in the console enter this, with your query of interest instead of ATCGACTGATCGATCGATCGATGCTAGCT.

view.run_command('sublimeblast', {'query':'ATCGACTGATCGATCGATCGATGCTAGCT'})
