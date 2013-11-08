Venture_Capital_Deals
=====================

This project does a few things:
1.  Website scraper - It compiles a list of pages at the CNN Venture Capital Deals blog with relevant
    information and then scrapes them to identify the name of the venture stage company, the round that was raised,
    how much  money was raised, and what VC/angels were involved.
2.  .graphml file complier - It then takes this information and complies it into a file that can be read and
    analyzed in Gephi, a free tool I ofund for analysing networks.
3.  Gephi analysis - I've included my Gephi analysis files in the folder and I'll probably keep them updated,
    but really the fun part is running the program yourself and seeing the network take shape.

How it works:
1.  vcd_list_maker.py - this identifies which cnn websites hold valuable information by cycling back through possible
    dates, searching for a server response code 200.
2.  vcd_list_appender.py - this takes an existing list and updates it to find any new sites that have been published.
3.  vcd_info_extractor.py - The real meat of the project, this code opens a website, looks for markers (both in the 
    html code and the writing style) indicating where relevant information might be, and then extracts it into a 
    dictionary.  I have functions that search for the name of the company, the round of capital raised, the amount
    of capital raised, a description of the company, and the VC/angels involved.  I also have functions that remove
    the passage containing each companys data as it's extracted.  If you look at only one file in this repository,
    it should be this one.
4.  graphy_builder.py - fairly straightfoward code that compiles my dictionary of events into a list of nodes and
    edges, and exports it as a .graphml file Gephi can read.  Gephi is an open source tool that can be used to play
    with graphs.  If your computer is fast enough (apparently mine is not), you can make nice videos of network
    features evolving out of the data.  But even with a slow computer, you can see the netowrk, play with the colors,
    and hover your mouse over nodes to quickly see who invested in which company, what companies a VC has invested in,
    and trace your way from one interesing company to another.
    
This is my first programming project:
I recently completed the Codecademy class on Python, this is the first code I've written in any language.  The code
works as written, but there are a lot of improvements I'm still making to get the thing to extract more and better
information.  For me, this is at least part of the fun.  But I'm sure I've also violated a number of best-practices,
so if you'd like to help me be a better programmer, help is much appreciated.

