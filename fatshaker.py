inp=input("Name of the .gro containing lipids: ")
outp=input("Name of the .gro output:   ")

pope=['   N', ' HN1', ' HN2', ' HN3', ' C12', 'H12A', 'H12B', ' C11', 'H11A', 'H11B', '   P', ' O13', ' O14', ' O11', ' O12', '  C1', '  HA', '  HB', '  C2', '  HS', ' O21', ' C21', ' O22', ' C22', ' H2R', ' H2S', '  C3', '  HX', '  HY', ' O31', ' C31', ' O32', ' C32', ' H2X', ' H2Y', ' C23', ' H3R', ' H3S', ' C24', ' H4R', ' H4S', ' C25', ' H5R', ' H5S', ' C26', ' H6R', ' H6S', ' C27', ' H7R', ' H7S', ' C28', ' H8R', ' H8S', ' C29', ' H91', 'C210', 'H101', 'C211', 'H11R', 'H11S', 'C212', 'H12R', 'H12S', 'C213', 'H13R', 'H13S', 'C214', 'H14R', 'H14S', 'C215', 'H15R', 'H15S', 'C216', 'H16R', 'H16S', 'C217', 'H17R', 'H17S', 'C218', 'H18R', 'H18S', 'H18T', ' C33', ' H3X', ' H3Y', ' C34', ' H4X', ' H4Y', ' C35', ' H5X', ' H5Y', ' C36', ' H6X', ' H6Y', ' C37', ' H7X', ' H7Y', ' C38', ' H8X', ' H8Y', ' C39', ' H9X', ' H9Y', 'C310', 'H10X', 'H10Y', 'C311', 'H11X', 'H11Y', 'C312', 'H12X', 'H12Y', 'C313', 'H13X', 'H13Y', 'C314', 'H14X', 'H14Y', 'C315', 'H15X', 'H15Y', 'C316', 'H16X', 'H16Y', 'H16Z']
popc=['   N', ' C12', ' C13', ' C14', ' C15', 'H12A', 'H12B', 'H13A', 'H13B', 'H13C', 'H14A', 'H14B', 'H14C', 'H15A', 'H15B', 'H15C', ' C11', 'H11A', 'H11B', '   P', ' O13', ' O14', ' O12', ' O11', '  C1', '  HA', '  HB', '  C2', '  HS', ' O21', ' C21', ' O22', ' C22', ' H2R', ' H2S', '  C3', '  HX', '  HY', ' O31', ' C31', ' O32', ' C32', ' H2X', ' H2Y', ' C23', ' H3R', ' H3S', ' C24', ' H4R', ' H4S', ' C25', ' H5R', ' H5S', ' C26', ' H6R', ' H6S', ' C27', ' H7R', ' H7S', ' C28', ' H8R', ' H8S', ' C29', ' H91', 'C210', 'H101', 'C211', 'H11R', 'H11S', 'C212', 'H12R', 'H12S', 'C213', 'H13R', 'H13S', 'C214', 'H14R', 'H14S', 'C215', 'H15R', 'H15S', 'C216', 'H16R', 'H16S', 'C217', 'H17R', 'H17S', 'C218', 'H18R', 'H18S', 'H18T', ' C33', ' H3X', ' H3Y', ' C34', ' H4X', ' H4Y', ' C35', ' H5X', ' H5Y', ' C36', ' H6X', ' H6Y', ' C37', ' H7X', ' H7Y', ' C38', ' H8X', ' H8Y', ' C39', ' H9X', ' H9Y', 'C310', 'H10X', 'H10Y', 'C311', 'H11X', 'H11Y', 'C312', 'H12X', 'H12Y', 'C313', 'H13X', 'H13Y', 'C314', 'H14X', 'H14Y', 'C315', 'H15X', 'H15Y', 'C316', 'H16X', 'H16Y', 'H16Z']
chol=['  C3', '  O3', " H3'", '  H3', '  C4', ' H4A', ' H4B', '  C5', '  C6', '  H6', '  C7', ' H7A', ' H7B', '  C8', '  H8', ' C14', ' H14', ' C15', 'H15A', 'H15B', ' C16', 'H16A', 'H16B', ' C17', ' H17', ' C13', ' C18', 'H18A', 'H18B', 'H18C', ' C12', 'H12A', 'H12B', ' C11', 'H11A', 'H11B', '  C9', '  H9', ' C10', ' C19', 'H19A', 'H19B', 'H19C', '  C1', ' H1A', ' H1B', '  C2', ' H2A', ' H2B', ' C20', ' H20', ' C21', 'H21A', 'H21B', 'H21C', ' C22', 'H22A', 'H22B', ' C23', 'H23A', 'H23B', ' C24', 'H24A', 'H24B', ' C25', ' H25', ' C26', 'H26A', 'H26B', 'H26C', ' C27', 'H27A', 'H27B', 'H27C']
pops=['   N', ' HN1', ' HN2', ' HN3', ' C12', 'H12A', ' C13', 'O13A', 'O13B', ' C11', 'H11A', 'H11B', '   P', ' O13', ' O14', ' O12', ' O11', '  C1', '  HA', '  HB', '  C2', '  HS', ' O21', ' C21', ' O22', ' C22', ' H2R', ' H2S', '  C3', '  HX', '  HY', ' O31', ' C31', ' O32', ' C32', ' H2X', ' H2Y', ' C23', ' H3R', ' H3S', ' C24', ' H4R', ' H4S', ' C25', ' H5R', ' H5S', ' C26', ' H6R', ' H6S', ' C27', ' H7R', ' H7S', ' C28', ' H8R', ' H8S', ' C29', ' H91', 'C210', 'H101', 'C211', 'H11R', 'H11S', 'C212', 'H12R', 'H12S', 'C213', 'H13R', 'H13S', 'C214', 'H14R', 'H14S', 'C215', 'H15R', 'H15S', 'C216', 'H16R', 'H16S', 'C217', 'H17R', 'H17S', 'C218', 'H18R', 'H18S', 'H18T', ' C33', ' H3X', ' H3Y', ' C34', ' H4X', ' H4Y', ' C35', ' H5X', ' H5Y', ' C36', ' H6X', ' H6Y', ' C37', ' H7X', ' H7Y', ' C38', ' H8X', ' H8Y', ' C39', ' H9X', ' H9Y', 'C310', 'H10X', 'H10Y', 'C311', 'H11X', 'H11Y', 'C312', 'H12X', 'H12Y', 'C313', 'H13X', 'H13Y', 'C314', 'H14X', 'H14Y', 'C315', 'H15X', 'H15Y', 'C316', 'H16X', 'H16Y','H16Z']
output=[]
def order(list,input_file,output,resname):
	f=open(input_file,"r").readlines()
	tab=[]
	print(resname+" has "+str(len(list))+" atoms")
	for atomtype in list:
		print("Saving "+atomtype+" atoms for lipid "+resname)
		tab.append([x for x in f if x[11:15]==atomtype and resname in x])
	for lipid in range(len(tab[0])):
		for atomtype in range(len(tab)):
			try:
				output.append(tab[atomtype][lipid])
			except:
				while True:
					eval("print("+input("command: ")+")")

order(popc,inp,output,resname='POPC')
order(pope,inp,output,resname='POPE')
order(pops,inp,output,resname='POPS')
order(chol,inp,output,resname='CHL')
f=open(outp,"w")

f.write("GROMACS - FatShaker\n")
f.write(str(len(output))+"\n")
for line in output:
	f.write(line)
f.write(open(inp,"r").readlines()[-1])
f.close()
