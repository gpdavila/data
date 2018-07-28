#!/usr/bin/env python3.4
import math
import statistics
def main():	
	with open( "log_30_bs.txt","r" ) as file_d:
		with open( "kernel_time_30.txt","w" ) as file_best:
			column = []
			tempo_total = 0
			amostras = 0
			for line in file_d:
				line = line.strip()			
				if line.find( "Kernel Time (ms):" )!= -1:#  Kernel Time
					time=float(line[17:])
					tempo_total = tempo_total + time
					amostras = amostras + 1 
#					time=line[17:]
#					print(time)
					column.append(time)
					#column.sort()					
#			print(column)
			file_best.write(str(column))	

#			file_best.write(str(new_list))	
			media = tempo_total / amostras
			file_best.write("\n Media:")	
			file_best.write(str(media))	
			file_best.write("\n")	
			dp = statistics.pstdev(column)
			file_best.write("Desvio Padrao:")
			file_best.write(str(dp))	
			file_best.write("\n")	
main()
