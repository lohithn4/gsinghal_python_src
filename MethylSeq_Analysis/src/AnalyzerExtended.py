'''
Created on Jul 14, 2010
Last Edited on Jul 18, 2010 
@author: Gaurav
'''



import matplotlib.pyplot as plt 
import sys
from pylab import *   #required for legend
from matplotlib.font_manager import FontProperties

'''
This script generates plots from files containing per base scores for repeat elements using matplotlib.

'''


'''
This script takes in four files having consensus scores for a Repeat Element
@param - read1, read2 : File containing mapped reads
@param readFile: File containing per base scores from reads (sequencing data)
@param siteFile1: File containing per base scores from one kind of Restriction Site (eg CCGG); similarly siteFile2 and siteFile3  
@param save: Boolean, save the file or not.
@output : plot, which contains read data on one Y axis and Restriction site data on another Y axis. 
'''

def multiGraph4(readFile1, readFile2, siteFile1, siteFile2, siteFile3, save ):
    
    # making a list of scores from readFile1
    
    read1Data = open(readFile1, 'rU') # normal
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score  
    rep1Fam = read1Data.readline().rstrip()
    rC1 = read1Data.readline().split()   # this line contains 'total read count' + '/t' + '# of unmatched reads'
    read1Count = float(rC1[0])
    ind = rep1Fam.find('_') 
    rep1Family = rep1Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element :  ', rep1Family
    read1Con = []
    for line in read1Data:
        list = line.split()
        read1Con.append(int(list[2]))    # list[2] contains the scores.
        
        
    read2Data = open(readFile2, 'rU')  #cancer
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score
    rep2Fam = read2Data.readline().rstrip()
    rC2 = read2Data.readline().split()
    read2Count = float(rC2[1])
    ind = rep2Fam.find('_') 
    rep2Family = rep2Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element =  ', rep2Family
    read2Con = []
    for line in read2Data:
        list = line.split()
        read2Con.append(int(list[2]))    # list[2] contains the scores.
    print 'readCount1 = ', read1Count
    print 'readCount2 = ', read2Count
    print 'readCount1/readCount2 = ', read1Count/read2Count
    
    normRead1Con = []
    normRead2Con = []
    
    if read1Count>read2Count:
        normRead2Con = read2Con
        for base in read1Con:
            normRead1Con.append(int(float(base)*(read2Count/read1Count)))
    else:
        normRead1Con = read1Con
        for base in read2Con:
            normRead2Con.append(int(float(base)*(read1Count/read2Count)))

    
    
    
    
    # making a list of scores from file containing scores for a particular RS
    siteData1 = open(siteFile1, 'rU')
    site1 = siteData1.readline().strip()
    site1name = site1.strip('_sites.bed_score')  # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon1 = []
    for line in siteData1:
        list = line.split()
        siteCon1.append(int(list[2]))
        
    
    siteData2 = open(siteFile2, 'rU')
    site2 = siteData2.readline().strip()
    site2name = site2.strip('_sites.bed_score')
    # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon2 = []
    for line in siteData2:
        list = line.split()
        siteCon2.append(int(list[2]))
    
    
    siteData3 = open(siteFile3, 'rU')
    site3 = siteData3.readline().strip()
    site3name = site3.strip('_sites.bed_score')
    # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon3 = []
    for line in siteData3:
        list = line.split()
        siteCon3.append(int(list[2]))
    
    #once the names of repeat element and RS sites is read and  list of per base scores are made, manyplots4() is called. This method plots 4 curves.
    manyplots4(rep1Family, normRead1Con, rep2Family, normRead2Con, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save)


def multiGraph5ExSp(repeats, readFile1, readFile2, readFile3, readFile4, siteFile1, siteFile2, siteFile3, save ):
    
    repData = open(repeats, 'rU') # normal
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score  
    repFam = repData.readline().rstrip()
#    rC1 = read1Data.readline().split()   # this line contains 'total read count' + '/t' + '# of unmatched reads'
#    read1Count = float(rC1[0])
    ind = repFam.find('_') 
    repFamily= repFam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element :  ', repFamily
    repCon = []
    for line in repData:
        list = line.split()
        repCon.append(int(list[2]))    # list[2] contains the scores.
    repCon = repCon[:326]  
    
    # making a list of scores from readFile1
    
    read1Data = open(readFile1, 'rU') # normal
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score  
    rep1Fam = read1Data.readline().rstrip()
    rC1 = read1Data.readline().split()   # this line contains 'total read count' + '/t' + '# of unmatched reads'
    read1Count = float(rC1[0])
    ind = rep1Fam.find('_') 
    rep1Family = rep1Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element :  ', rep1Family
    read1Con = []
    for line in read1Data:
        list = line.split()
        read1Con.append(int(list[2]))    # list[2] contains the scores.
        
        
    read2Data = open(readFile2, 'rU')  #cancer
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score
    rep2Fam = read2Data.readline().rstrip()
    rC2 = read2Data.readline().split()
    read2Count = float(rC2[0])
    ind = rep2Fam.find('_') 
    rep2Family = rep2Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element =  ', rep2Family
    read2Con = []
    for line in read2Data:
        list = line.split()
        read2Con.append(int(list[2]))    # list[2] contains the scores.
    print 'readCount1 = ', read1Count
    print 'readCount2 = ', read2Count
    print 'readCount1/readCount2 = ', read1Count/read2Count
    
    normRead1Con = []
    normRead2Con = []
    
    if read1Count>read2Count:
        normRead2Con = read2Con
        for base in read1Con:
            normRead1Con.append(int(float(base)*(read2Count/read1Count)))
    else:
        normRead1Con = read1Con
        for base in read2Con:
            normRead2Con.append(int(float(base)*(read1Count/read2Count)))

    read3Data = open(readFile3, 'rU') # normal
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score  
    rep3Fam = read3Data.readline().rstrip()
    rC3 = read3Data.readline().split()   # this line contains 'total read count' + '/t' + '# of unmatched reads'
    read3Count = float(rC3[0])
    ind = rep3Fam.find('_') 
    rep3Family = rep3Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element :  ', rep3Family
    read3Con = []
    for line in read3Data:
        list = line.split()
        read3Con.append(int(list[2]))    # list[2] contains the scores.
        
        
    read4Data = open(readFile4, 'rU')  #cancer
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score
    rep4Fam = read4Data.readline().rstrip()
    rC4 = read4Data.readline().split()
    read4Count = float(rC4[0])
    ind = rep4Fam.find('_') 
    rep4Family = rep4Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element =  ', rep4Family
    read4Con = []
    for line in read4Data:
        list = line.split()
        read4Con.append(int(list[2]))    # list[2] contains the scores.
    print 'readCount1 = ', read3Count
    print 'readCount2 = ', read4Count
    print 'readCount1/readCount2 = ', read3Count/read4Count
    
    normRead3Con = []
    normRead4Con = []
    
    if read3Count>read4Count:
        normRead4Con = read4Con
        for base in read3Con:
            normRead3Con.append(int(float(base)*(read4Count/read3Count)))
    else:
        normRead3Con = read3Con
        for base in read4Con:
            normRead4Con.append(int(float(base)*(read3Count/read4Count)))
    
    
    
    # making a list of scores from file containing scores for a particular RS
    siteData1 = open(siteFile1, 'rU')
    site1 = siteData1.readline().strip()
    site1name = site1.strip('_sites.bed_score')  # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon1 = []
    for line in siteData1:
        list = line.split()
        siteCon1.append(int(list[2]))
        
    
    siteData2 = open(siteFile2, 'rU')
    site2 = siteData2.readline().strip()
    site2name = site2.strip('_sites.bed_score')
    # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon2 = []
    for line in siteData2:
        list = line.split()
        siteCon2.append(int(list[2]))
    
    
    siteData3 = open(siteFile3, 'rU')
    site3 = siteData3.readline().strip()
    site3name = site3.strip('_sites.bed_score')
    # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon3 = []
    for line in siteData3:
        list = line.split()
        siteCon3.append(int(list[2]))
    
    #once the names of repeat element and RS sites is read and  list of per base scores are made, manyplots4() is called. This method plots 4 curves.


def multiGraph5SuExSp(readFile1, readFile2, readFile3, readFile4, save ):
    
    read1Data = open(readFile1, 'rU') # normal
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score  
    rep1Fam = read1Data.readline().rstrip()
    rC1 = read1Data.readline().split()   # this line contains 'total read count' + '/t' + '# of unmatched reads'
    read1Count = float(rC1[0])
    ind = rep1Fam.find('_') 
    rep1Family = rep1Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element :  ', rep1Family
    read1Con = []
    for line in read1Data:
        list = line.split()
        read1Con.append(int(list[2]))    # list[2] contains the scores.
        
        
    read2Data = open(readFile2, 'rU')  #cancer
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score
    rep2Fam = read2Data.readline().rstrip()
    rC2 = read2Data.readline().split()
    read2Count = float(rC2[0])
    ind = rep2Fam.find('_') 
    rep2Family = rep2Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element =  ', rep2Family
    read2Con = []
    for line in read2Data:
        list = line.split()
        read2Con.append(int(list[2]))    # list[2] contains the scores.
    print 'readCount1 = ', read1Count
    print 'readCount2 = ', read2Count
    print 'readCount1/readCount2 = ', read1Count/read2Count
    
    normRead1Con = []
    normRead2Con = []
    
    if read1Count>read2Count:
        normRead2Con = read2Con
        for base in read1Con:
            normRead1Con.append(int(float(base)*(read2Count/read1Count)))
    else:
        normRead1Con = read1Con
        for base in read2Con:
            normRead2Con.append(int(float(base)*(read1Count/read2Count)))

    read3Data = open(readFile3, 'rU') # normal
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score  
    rep3Fam = read3Data.readline().rstrip()
    rC3 = read3Data.readline().split()   # this line contains 'total read count' + '/t' + '# of unmatched reads'
    read3Count = float(rC3[0])
    ind = rep3Fam.find('_') 
    rep3Family = rep3Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element :  ', rep3Family
    read3Con = []
    for line in read3Data:
        list = line.split()
        read3Con.append(int(list[2]))    # list[2] contains the scores.
        
        
    read4Data = open(readFile4, 'rU')  #cancer
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score
    rep4Fam = read4Data.readline().rstrip()
    rC4 = read4Data.readline().split()
    read4Count = float(rC4[0])
    ind = rep4Fam.find('_') 
    rep4Family = rep4Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element =  ', rep4Family
    read4Con = []
    for line in read4Data:
        list = line.split()
        read4Con.append(int(list[2]))    # list[2] contains the scores.
    print 'readCount3 = ', read3Count
    print 'readCount4 = ', read4Count
    print 'readCount3/readCount4 = ', read3Count/read4Count
    
    normRead3Con = []
    normRead4Con = []
    
    if read3Count>read4Count:
        normRead4Con = read4Con
        for base in read3Con:
            normRead3Con.append(int(float(base)*(read4Count/read3Count)))
    else:
        normRead3Con = read3Con
        for base in read4Con:
            normRead4Con.append(int(float(base)*(read3Count/read4Count)))
    
    
    
   
    
    #once the names of repeat element and RS sites is read and  list of per base scores are made, manyplots4() is called. This method plots 4 curves.
    manyplots5SuExSp( rep1Family, normRead1Con, rep2Family, normRead2Con,rep3Family, normRead3Con, rep4Family, normRead4Con,save)



def multiGraph4Sp(readFile1, readFile2, siteFile1, siteFile2, siteFile3, save ):
    
    # making a list of scores from genome consensus
    
    read1Data = open(readFile1, 'rU') # normal
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score  
    rep1Fam = read1Data.readline().rstrip()
#    rC1 = read1Data.readline().split()   # this line contains 'total read count' + '/t' + '# of unmatched reads'
#    read1Count = float(rC1[0])
    ind = rep1Fam.find('_') 
    rep1Family = rep1Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element :  ', rep1Family
    read1Con = []
    for line in read1Data:
        list = line.split()
        read1Con.append(int(list[2]))    # list[2] contains the scores.
    read1Con = read1Con[:326]   
        
    read2Data = open(readFile2, 'rU')  #cancer
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score
    rep2Fam = read2Data.readline().rstrip()
    rC2 = read2Data.readline().split()
#    read2Count = float(rC2[1])
    ind = rep2Fam.find('_') 
    rep2Family = rep2Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element =  ', rep2Family
    read2Con = []
    for line in read2Data:
        list = line.split()
        read2Con.append(int(list[2]))    # list[2] contains the scores.
    
    
    # making a list of scores from file containing scores for a particular RS
    siteData1 = open(siteFile1, 'rU')
    site1 = siteData1.readline().strip()
    site1name = site1.strip('_sites.bed_score')  # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon1 = []
    for line in siteData1:
        list = line.split()
        siteCon1.append(int(list[2]))
        
    
    siteData2 = open(siteFile2, 'rU')
    site2 = siteData2.readline().strip()
    site2name = site2.strip('_sites.bed_score')
    # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon2 = []
    for line in siteData2:
        list = line.split()
        siteCon2.append(int(list[2]))
    
    
    siteData3 = open(siteFile3, 'rU')
    site3 = siteData3.readline().strip()
    site3name = site3.strip('_sites.bed_score')
    # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon3 = []
    for line in siteData3:
        list = line.split()
        siteCon3.append(int(list[2]))
    
    #once the names of repeat element and RS sites is read and  list of per base scores are made, manyplots4() is called. This method plots 4 curves.
    manyplots4Sp(rep1Family, read1Con, rep2Family, read2Con, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save)
       

       
def multiGraph3(readFile1, siteFile1, siteFile2, siteFile3, save ):
    
    # making a list of scores from readFile1
    
    read1Data = open(readFile1, 'rU') # normal
    #name of repeat family is picked from the first line of the read file, which looks like AluJb_read_score  
    rep1Fam = read1Data.readline().rstrip()
#    rC1 = read1Data.readline().split()   # this line contains 'total read count' + '/t' + '# of unmatched reads'
#    read1Count = float(rC1[0])
    ind = rep1Fam.find('_') 
    rep1Family = rep1Fam[:ind] # keeping everything before the first underscore '_', which is the name of the repeat element
    print 'plotting read data for the repeat element :  ', rep1Family
    read1Con = []
    for line in read1Data:
        list = line.split()
        read1Con.append(int(list[2]))    # list[2] contains the scores.
    
    read1Con = read1Con[:326]
    
    # making a list of scores from file containing scores for a particular RS
    siteData1 = open(siteFile1, 'rU')
    site1 = siteData1.readline().strip()
    site1name = site1.strip('_sites.bed_score')  # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon1 = []
    for line in siteData1:
        list = line.split()
        siteCon1.append(int(list[2]))
        
    
    siteData2 = open(siteFile2, 'rU')
    site2 = siteData2.readline().strip()
    site2name = site2.strip('_sites.bed_score')
    # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon2 = []
    for line in siteData2:
        list = line.split()
        siteCon2.append(int(list[2]))
    
    
    siteData3 = open(siteFile3, 'rU')
    site3 = siteData3.readline().strip()
    site3name = site3.strip('_sites.bed_score')
    # removing unnecessary stuff from the end of the string. 
    #this will be used as the label in legend 
    siteCon3 = []
    for line in siteData3:
        list = line.split()
        siteCon3.append(int(list[2]))
    
    #once the names of repeat element and RS sites is read and  list of per base scores are made, manyplots4() is called. This method plots 4 curves.
    manyplots3(rep1Family, read1Con, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save)
       



'''
This script takes in two files having consensus scores for a Repeat Element
@param Consensus: File containing per base scores for a repeat element from hg18 
@param CpGsite: File containing per base scores for CpG Sites (eg CCGG)  
@param save: Boolean, save the file or not.
@output : plot, which contains hg18/hg19 consensus data on one Y axis and CpG site density data on another Y axis. 
'''

def multiGraph2(Consensus, CpGsite, save ):
   
    # making a list of scores from Consensus

    
    CpGdata = open(CpGsite, 'rU')
    site1name = CpGdata.readline().rstrip()
    siteCon1 = []
    for line in CpGdata:
        list = line.split()
        siteCon1.append(int(list[2]))
    
    axislen = len(siteCon1)  # using the no of bases in siteCon to cut down excess of readData
    
    readData = open(Consensus, 'rU')
    repFam = readData.readline().rstrip()
    ind = repFam.find('_')
    repFamily = repFam[:ind]
    print 'multiGraph4 repFamily =  ', repFamily
    readCon = []
    
    
    # in case read data file is longer than other files,     
    i=0
    for line in readData:
        if i < axislen:
            list = line.split()
            readCon.append(int(list[2]))
            i+=1
    
        
    #once the names of repeat element and CpG site is read and list of per base scores are made, manyplots2() is called. This method plots 2 curves.
    manyplots2(repFamily, readCon, site1name, siteCon1, save)
       

'''
This script takes in two files having consensus scores for a Repeat Element
@param Consensus: File containing per base scores for a repeat element from hg18 
@param CpGsite: File containing per base scores for CpG Sites (eg CCGG)  
@param save: Boolean, save the file or not.
@output : plot, which contains hg18/hg19 consensus data on one Y axis and CpG site density data on another Y axis. 
'''

def multiGraph1(Consensus, save ):
   
    # making a list of scores from Consensus

#    axislen = len(siteCon1)  # using the no of bases in siteCon to cut down excess of readData
    
    axislen = 326
    readData = open(Consensus, 'rU')
    repFam = readData.readline().rstrip()
    ind = repFam.find('_')
    repFamily = repFam[:ind]
    print 'multiGraph4 repFamily =  ', repFamily
    readCon = []
    
    
    # in case read data file is longer than other files,     
    i=0
    for line in readData:
        if i < axislen:
            list = line.split()
            readCon.append(int(list[2]))
            i+=1
    
        
    #once the names of repeat element and CpG site is read and list of per base scores are made, manyplots2() is called. This method plots 2 curves.
    manyplots1(repFamily, readCon, save)


'''
This method takes in 4 consensus scores, one for reads, and one each for three restriction sites.
@param repFamily : This string froms the first part of file name and legend for readCon data
@param readCon : This is the per base consensus score for reads.
@param siteCon1 : This is the per base consensus score for restriction site. similarly siteCon2, siteCon3
@param site1name : String, representing the name of the string, and will make the legend. similarly site2name, site3name
'''     
def manyplots4Sp(rep1Family, read1Con, rep2Family, read2Con, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save):
    rcParams['legend.loc'] = 'upper right'    # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11 # manually setting the plot size (width X height)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    length = len(read1Con)
    ys = read1Con #genome cons
    ys4 = read2Con #normal
    ys1 = siteCon1
    ys2 = siteCon2
    ys3 = siteCon3
    
    print 'normal :'
    print ys
    print '\n'
    
    print 'cancer :'
    print ys4
    print '\n'
    
    
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    print rep1Family
    print 'xs = ', len(xs)
    print 'ys = ', len(ys)
    print 'ys4 = ', len(ys4)
    print 'ys1 = ', len(ys1)
    print 'ys2 = ', len(ys2)
    print 'ys3 = ', len(ys3)
        
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    
    
    filename = rep1Family+'_read_RS.png' # plot will be saved with this name
    con1Label = rep1Family + ' Genome Coverage'   #legend for reads data
    con2Label = rep2Family + ' reads (Normal)'
    line1, = ax1.plot(xs, ys, linewidth = 1.5, color = 'b')
    line2, = ax1.plot(xs, ys1, color = 'k') 
    line3, = ax1.plot(xs, ys2, color = 'm')
    line4, = ax1.plot(xs, ys3, color = 'c')
   
    ax1.set_xlabel('base position in Repeat Element consensus')
    ax1.set_ylabel('per base score from hg18', color='k')
    #yticklabels are also kept with the same color as the line so that they can be visually related to each other. 
    for tl in ax1.get_yticklabels():
        tl.set_color('k')
    
    
    #making a twin y - axis, on the right hand side of the plot. This axis is used for plotting Restriction site data. 
    ax2 = ax1.twinx()
    
    ax2.axis([0,350, 0,8000])
    #plotting the data for restriction site
    
    line5, = ax2.plot(xs, ys4, linewidth = 2.0, color = 'g')
#    line2, = ax2.plot(xs, ys1, color = 'b') 
#    line3, = ax2.plot(xs, ys2, color = 'm')
#    line4, = ax2.plot(xs, ys3, color = 'c')
   
    ax2.set_ylabel('per base score from MRE reads', color='k')
    for tl in ax2.get_yticklabels():
        tl.set_color('k')
    
    #building legend
    legend((line1, line5, line2, line3, line4),(con1Label, con2Label, site1name, site2name, site3name))
   
    
    plt.title(rep1Family )
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    
    plt.show()      

def manyplots5Sp(repFamily, repeatCon, rep1Family, read1Con, rep2Family, read2Con, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save):
    rcParams['legend.loc'] = 'upper right'    # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11 # manually setting the plot size (width X height)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    length = len(read1Con)
    ys = repeatCon #genome cons
    
   
    ys1 = siteCon1
    ys2 = siteCon2
    ys3 = siteCon3
    
    ys4 = read1Con #normal
    ys5 = read2Con #cancer
    print 'normal :'
    print ys
    print '\n'
    
    print 'cancer :'
    print ys4
    print '\n'
    
    
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    print rep1Family
    print 'xs = ', len(xs)
    print 'ys = ', len(ys)
    print 'ys4 = ', len(ys4)
    print 'ys1 = ', len(ys1)
    print 'ys2 = ', len(ys2)
    print 'ys3 = ', len(ys3)
        
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    
    
    filename = rep1Family+'_read_RS_con.png' # plot will be saved with this name
    conlbl = repFamily + ' Genome Coverage'
    con1Label = rep1Family + ' reads (Normal)'   #legend for reads data
    con2Label = rep2Family + ' reads (Cancer)'
    line1, = ax1.plot(xs, ys, linewidth = 1.5, color = 'b')
    line2, = ax1.plot(xs, ys1, color = 'k') 
    line3, = ax1.plot(xs, ys2, color = 'm')
    line4, = ax1.plot(xs, ys3, color = 'c')
   
    ax1.set_xlabel('base position in Repeat Element consensus')
    ax1.set_ylabel('per base score from hg18', color='k')
    #yticklabels are also kept with the same color as the line so that they can be visually related to each other. 
    for tl in ax1.get_yticklabels():
        tl.set_color('k')
    
    
    #making a twin y - axis, on the right hand side of the plot. This axis is used for plotting Restriction site data. 
    ax2 = ax1.twinx()
    
    ax2.axis([0,350, 0,8000])
    #plotting the data for restriction site
    
    line5, = ax2.plot(xs, ys4, linewidth = 2.0, color = 'g') #normal
    line6, = ax2.plot(xs, ys5, linewidth = 2.0, color = 'r') #cancer
#    line2, = ax2.plot(xs, ys1, color = 'b') 
#    line3, = ax2.plot(xs, ys2, color = 'm')
#    line4, = ax2.plot(xs, ys3, color = 'c')
   
    ax2.set_ylabel('per base score from MRE reads', color='k')
    for tl in ax2.get_yticklabels():
        tl.set_color('k')
    
    #building legend
    legend((line1, line5, line6, line2, line3, line4,),(conlbl, con1Label, con2Label, site1name, site2name, site3name))
   
    
    plt.title(rep1Family )
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    
    plt.show()      

def manyplots5SuExSp(rep1Family, normRead1Con, rep2Family, normRead2Con,rep3Family, normRead3Con, rep4Family, normRead4Con, save):
    rcParams['legend.loc'] = 'upper right'    # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11 # manually setting the plot size (width X height)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    length = len(normRead1Con)

    
   
    ys1 = normRead1Con # mre normal
    ys2 = normRead2Con #mre Cancer
    
    ys3 = normRead3Con #meDip normal
    ys4 = normRead4Con #medip cancer
    
    
    
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    print rep1Family
    print 'xs = ', len(xs)
    
    
    print 'ys1 = ', len(ys1)
    print 'ys2 = ', len(ys2)
    print 'ys3 = ', len(ys3)
    print 'ys4 = ', len(ys4)    
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    
    
    filename = rep1Family+'_MeDip_MRE.png' # plot will be saved with this name
    
    con1Label = rep1Family + ' MRE reads (Normal)'   #legend for reads data
    con2Label = rep2Family + ' MRE reads (Cancer)'
    con3Label = rep3Family + ' MeDIP reads (Normal)'   #legend for reads data
    con4Label = rep4Family + ' MeDIP reads (Cancer)'
    line1, = ax1.plot(xs, ys1, linewidth = 1.5, color = 'g')
    
    line2, = ax1.plot(xs, ys2, linewidth = 1.5, color = 'r')
    
    
   
   
    ax1.set_xlabel('base position in Repeat Element consensus')
    ax1.set_ylabel('per base score from MRE reads', color='k')
    #yticklabels are also kept with the same color as the line so that they can be visually related to each other. 
    for tl in ax1.get_yticklabels():
        tl.set_color('k')
    
    
    #making a twin y - axis, on the right hand side of the plot. This axis is used for plotting Restriction site data. 
    ax2 = ax1.twinx()
    
    #plotting the data for medip
   
    line3, = ax2.plot(xs, ys3, linewidth = 1.5, color = 'm') #normal medip
    line4, = ax2.plot(xs, ys4, linewidth = 1.5, color = 'k') #cancer medip

   
    ax2.set_ylabel('per base score from MeDIP reads', color='k')
    for tl in ax2.get_yticklabels():
        tl.set_color('k')
    
    #building legend
    legend((line1, line2, line3, line4,),(con1Label, con2Label,con3Label, con4Label))
   
    
    plt.title(rep1Family )
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    
    plt.show()      

'''
This method takes in 4 consensus scores, one for reads, and one each for three restriction sites.
@param repFamily : This string froms the first part of file name and legend for readCon data
@param readCon : This is the per base consensus score for reads.
@param siteCon1 : This is the per base consensus score for restriction site. similarly siteCon2, siteCon3
@param site1name : String, representing the name of the string, and will make the legend. similarly site2name, site3name
'''     
def manyplots4(rep1Family, read1Con, rep2Family, read2Con, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save):
    rcParams['legend.loc'] = 'best'    # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11 # manually setting the plot size (width X height)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    length = len(read1Con)
    ys = read1Con #genome consensus
    ys4 = read2Con #cancer
    ys1 = siteCon1
    ys2 = siteCon2
    ys3 = siteCon3
    
    print 'normal :'
    print ys
    print '\n'
    
    print 'cancer :'
    print ys4
    print '\n'
    
    
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    print rep1Family
    print 'xs = ', len(xs)
    print 'ys = ', len(ys)
    print 'ys4 = ', len(ys4)
    print 'ys1 = ', len(ys1)
    print 'ys2 = ', len(ys2)
    print 'ys3 = ', len(ys3)
        
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    
    
    filename = rep1Family+'_cons_RS_normal.png' # plot will be saved with this name
    con1Label = rep1Family + ' Genome Coverage'   #legend for reads data
    con2Label = rep2Family + ' reads (Normal)'
    line1, = ax1.plot(xs, ys, linewidth = 2.0, color = 'g')
    line5, = ax1.plot(xs, ys4, linewidth = 2.0, color = 'r')
    ax1.set_xlabel('base position in consensus')
    ax1.set_ylabel('per base score from read data', color='k')
    #yticklabels are also kept with the same color as the line so that they can be visually related to each other. 
    for tl in ax1.get_yticklabels():
        tl.set_color('k')
    
    
    #making a twin y - axis, on the right hand side of the plot. This axis is used for plotting Restriction site data. 
    ax2 = ax1.twinx()
    
    
    #plotting the data for restriction site
    line2, = ax2.plot(xs, ys1, color = 'b') 
    line3, = ax2.plot(xs, ys2, color = 'm')
    line4, = ax2.plot(xs, ys3, color = 'c')
   
    ax2.set_ylabel('per base score for Restriction site', color='k')
    for tl in ax2.get_yticklabels():
        tl.set_color('g')
    
    #building legend
    legend((line1, line5, line2, line3, line4),(con1Label, con2Label, site1name, site2name, site3name))
   
    
    plt.title(rep1Family )
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    
    plt.show()
    

def manyplots3(rep1Family, read1Con, site1name, siteCon1, site2name, siteCon2, site3name,siteCon3, save):
    rcParams['legend.loc'] = 'upper right'    # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11 # manually setting the plot size (width X height)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    length = len(read1Con)
    ys = read1Con #Normal
   
    ys1 = siteCon1
    ys2 = siteCon2
    ys3 = siteCon3
    
    print 'normal :'
    print ys
    print '\n'
    
   
    
    
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    print rep1Family
    print 'xs = ', len(xs)
    print 'ys = ', len(ys)
    
    print 'ys1 = ', len(ys1)
    print 'ys2 = ', len(ys2)
    print 'ys3 = ', len(ys3)
        
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    
    
    filename = rep1Family+'Cons_RS.png' # plot will be saved with this name
    conlbl = rep1Family + ' Genome Coverage'   #legend for reads data
   # con2Label = rep2Family + ' reads (Cancer)'
    line1, = ax1.plot(xs, ys, linewidth = 1.5, color = 'b')
    line2, = ax1.plot(xs, ys1, color = 'k') 
    line3, = ax1.plot(xs, ys2, color = 'm')
    line4, = ax1.plot(xs, ys3, color = 'c')
    #line5, = ax1.plot(xs, ys4, linewidth = 2.0, color = 'r')
    ax1.set_xlabel('base position in Repeat Element Consensus')
    ax1.set_ylabel('per base score from hg18', color='k')
    #yticklabels are also kept with the same color as the line so that they can be visually related to each other. 
    for tl in ax1.get_yticklabels():
        tl.set_color('k')
    
    
    
    
    #building legend
    legend((line1, line2, line3, line4),(conlbl, site1name, site2name, site3name))
   
    
    plt.title(rep1Family )
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    
    plt.show()
    
    

'''
This method takes in 2 consensus scores, one for consensus score for a particular repeat element for a hg reference, such as hg18, and one for CpG site density.
@param repFamily : This string froms the first part of file name and legend for readCon data
@param repeatCon : This is the per base consensus score for repeat element.
@param siteCon1 : This is the per base consensus score for CpG site. In other words, this represents the per base density of CpG sites on a repeat element.
@param site1name : this String will make the legend for CpG curve.
'''  
    
def manyplots2(repFamily, repeatCon, site1name, siteCon1, save):
    rcParams['legend.loc'] = 'best'  # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11  # manually setting the plot size (width X height)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    length = len(repeatCon)
    ys = repeatCon
    
    ys1 = siteCon1
        
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    
    filename = repFamily+'_CpG.png' # plot will be saved with this name
    conlbl = repFamily + ' Consensus' #legend for hg18/hg19 consensus data
    line1, = ax1.plot(xs, ys, linewidth = 2.0, color = 'b')
    ax1.set_xlabel('base position in consensus')
    ax1.set_ylabel('per base score from consensus (hg18) ', color='b')
    for tl in ax1.get_yticklabels():
        tl.set_color('b')
    
    
    #making a twin y - axis, on the right hand side of the plot. This axis is used for plotting CpG site data. 
    ax2 = ax1.twinx()
    #plotting the data for restriction site
    line2, = ax2.plot(xs, ys1, color = 'g') 

    
    ax2.set_ylabel('per base score for CpG site', color='g')
    for tl in ax2.get_yticklabels():
        tl.set_color('g')
    
    #building legend
    legend((line1, line2),(conlbl, site1name))
   
    
    plt.title(repFamily)
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    plt.show()
  
  
'''
This method takes in 2 consensus scores, one for consensus score for a particular repeat element for a hg reference, such as hg18, and one for CpG site density.
@param repFamily : This string froms the first part of file name and legend for readCon data
@param repeatCon : This is the per base consensus score for repeat element.
@param siteCon1 : This is the per base consensus score for CpG site. In other words, this represents the per base density of CpG sites on a repeat element.
@param site1name : this String will make the legend for CpG curve.
'''  
    
def manyplots1(repFamily, repeatCon, save):
    font0 = FontProperties()
    rcParams['legend.loc'] = 'upper right'  # puts the legend at the best possible location, where it minimally overlaps the curves
    rcParams['figure.figsize'] = 16, 11  # manually setting the plot size (width X height)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    
    length = len(repeatCon)
    ys = repeatCon
    
    
        
    base = 0
    xs = []
    for base in range(length):
        base += 1
        xs.append(base)
        
    
    #xs just forms the x axis, and is a list of numbers from 1 to length of repeat consensus family.
    #eg, for AluY, xs = [1,2,3,4...,311]
    
    filename = repFamily+'.png' # plot will be saved with this name
    conlbl = repFamily + ' Genome Coverage' #legend for hg18/hg19 consensus data
    line1, = ax1.plot(xs, ys, linewidth = 1.5, color = 'b', label = conlbl)
    ax1.set_xlabel('base position in Repeat Element consensus')
    ax1.set_ylabel('per base score from hg18', color='b')
    for tl in ax1.get_yticklabels():
        tl.set_color('b')
    
   
    #building legend
    legend()
   
    
    plt.title(repFamily)
    plt.grid(True)
   
    if save:
        plt.savefig(filename)
    plt.show()
  


def SuperPlotter(siteFile1, siteFile2, siteFile3, readFile1N, readFile1C, readFile2N, readFile2C, readFile3N, readFile3C ):
    save = True
    multiGraph4(readFile1N, readFile1C, siteFile1, siteFile2, siteFile3, save)
    multiGraph4(readFile2N, readFile2C, siteFile1, siteFile2, siteFile3, save)
    multiGraph4(readFile3N, readFile3C, siteFile1, siteFile2, siteFile3, save)
   


#def main():
#    # use either of the two method calls. 
#    readFile1N = sys.argv[1] #normal
#    readFile1C = sys.argv[2] #cancer
#    readFile2N = sys.argv[3] #normal
#    readFile2C = sys.argv[4] #cancer
#    readFile3N = sys.argv[5]
#    readFile3C = sys.argv[6]
#    siteFile1 = sys.argv[7]
#    siteFile2 = sys.argv[8]
#    siteFile3 = sys.argv[9]
#    
#    
#    SuperPlotter(siteFile1, siteFile2, siteFile3, 
#                 readFile1N, readFile1C, readFile2N, readFile2C, readFile3N, readFile3C )
#    
#
##    readFile = sys.argv[1]
##    siteFile1 = sys.argv[2]
##    save = sys.argv[3]
##    multiGraph2(readFile, siteFile1, save )
    
    
#def main():
#    readFile1N = sys.argv[1]
#    readFile1C = sys.argv[2]
#    siteFile1 = sys.argv[3]
#    siteFile2 = sys.argv[4]
#    siteFile3 = sys.argv[5]
#    save = sys.argv[6]
#    multiGraph4(readFile1N, readFile1C, siteFile1, siteFile2, siteFile3, save )

#def main():
#    Consensus = sys.argv[1]
#    save = sys.argv[2]
#    multiGraph1(Consensus, save)
    

#def main():
#    readFile1N = sys.argv[1]
#   
#    siteFile1 = sys.argv[2]
#    siteFile2 = sys.argv[3]
#    siteFile3 = sys.argv[4]
#    save = sys.argv[5]
#    multiGraph3(readFile1N, siteFile1, siteFile2, siteFile3, save )
    
#def main():
#    readFile1N = sys.argv[1]
#    readFile1C = sys.argv[2]
#    siteFile1 = sys.argv[3]
#    siteFile2 = sys.argv[4]
#    siteFile3 = sys.argv[5]
#    save = sys.argv[6]
#    multiGraph4Sp(readFile1N, readFile1C, siteFile1, siteFile2, siteFile3, save )

#def main():
#    repeatFile = sys.argv[1]
#    readFile1N = sys.argv[2]
#    readFile1C = sys.argv[3]
#    siteFile1 = sys.argv[4]
#    siteFile2 = sys.argv[5]
#    siteFile3 = sys.argv[6]
#    save = sys.argv[7]
#    multiGraph5Sp(repeatFile, readFile1N, readFile1C, siteFile1, siteFile2, siteFile3, save )


def main():
    readFile1N = sys.argv[1]
    readFile1C = sys.argv[2]
    readFile2N = sys.argv[3]
    readFile2C = sys.argv[4]
    
    multiGraph5SuExSp(readFile1N, readFile1C, readFile2N, readFile2C, save )


if __name__=='__main__':
    main()    