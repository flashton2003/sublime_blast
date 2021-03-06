import sublime
import sublime_plugin
import os
import subprocess
import uuid


class sublimeblastCommand(sublime_plugin.TextCommand):
	def run(self, edit, query):
		## get the contents of the tab that is the focus in sublime
		allcontent = sublime.Region(0, self.view.size())
		## convert to string
		allcontent = self.view.substr(allcontent)
		## get a unique string for use in the tmp files
		unique_filename = str(uuid.uuid4())
		## open db and query files in /tmp and write allcontent (i.e. the 'page' open, with the sublime console at the bottom)
		db_handle = '/tmp/%s.sublime_blast.tmp_db.fa' % unique_filename
		with open(db_handle, 'w') as fo:
			fo.write(allcontent)
		query_handle = '/tmp/%s.sublime_blast.tmp_query.fa' % unique_filename
		with open(query_handle, 'w') as fo:
			fo.write('>query\n%s\n' % query)
		## make a blastdb of the page open in sublime
		subprocess.call(['/usr/local/bin/makeblastdb', '-dbtype', 'nucl', '-in', '%s' % db_handle])
		## run blast, taking the query as what is input in the console
		blast_output = subprocess.getoutput(['/usr/local/bin/blastn -db {0} -query {1} -outfmt 6'.format(db_handle, query_handle)])
		## add the headers and the blast output to the end of the window of focus
		## self.view.size() is where you want to insert the text, in this case, at the end of the file so we use self.view.size() which is the total size
		## edit is a token which classes the insert as a single edit which can e.g. be undone with one 'undo'
		self.view.insert(edit, self.view.size(), '\nqseqid	sseqid	pident	length	mismatch	gapopen	qstart	qend	sstart	send	evalue	bitscore\n')
		self.view.insert(edit, self.view.size(), blast_output)

