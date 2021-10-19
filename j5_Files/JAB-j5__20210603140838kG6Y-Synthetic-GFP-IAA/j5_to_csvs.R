#' Parse a j5 assembly csv file into python readable feathers
#'
#' @param path a string representing the directory containing the j5 assembly
#' file to parse. This function operates on any file ending with
#' _combinatorial.csv by default.
#' @param file
#'
#' @details
#'
#' @return feather (arrow pkg) files for each section of a j5 assembly csv
#' files
#' @export
#' @import readr
#'
#' @examples
#' parse_j5(path = "./J5_EricZirkle_GH3_mCherry")
parse_j5 <- function(path = getwd(), file = "_combinatorial.csv")
{
  file <- list.files(path = path, pattern = file, full.names = TRUE)
  #body
  
  j5lines <- readLines(file) #reads lines from J5 file to help with parsing
  
  digests <- grep(pattern = "Digest Linearized Pieces",j5lines) #searches for first set of data needed from J5 file (Oligo Synthesis Data)
  #returns line number for the Oligo Synthesis
  
  oligo <- grep(pattern = "Oligo Synthesis",j5lines) #searches for first set of data needed from J5 file (Oligo Synthesis Data)
  #returns line number for the Oligo Synthesis
  
  pcr <- grep(pattern = "PCR Reactions",j5lines)#Searches for the title of the next set of data (PCR Reactions)
  #Returns the line number of this pattern
  
  gibson <- grep(pattern = "Assembly Pieces (SLIC/Gibson/CPEC)",j5lines,fixed = TRUE)#Searches for the title of next set of data if assembly pieces are gibson
  #returns the line number of this pattern
  
  golden_gate <- grep(pattern = "Assembly Pieces (Golden-gate)",j5lines, fixed = TRUE)#Searches for the next set of data if the assembly is golden gate
  #returns line number for this pattern
  
  combinations <- grep(pattern = "Combinations of Assembly Pieces",j5lines, fixed = TRUE)
  #Reads the Oligo Synthesis portion of the CSV file
  oligo_read <- readr::read_csv(file, col_names = c("ID Number", "Name", "Length", "Tm", "Tm (3' only)", "Cost", "Sequence", "Sequence (3' only)"),skip = oligo+1,n_max = pcr-oligo-3)
  #TODO Suppress messages from read_csv
  #return(oligo_read)
  #feather::write_feather(oligo_read, path = paste0(path,"/oligo.feather"))#Creates feather file for Oligo Synthesis information
  write.csv(oligo_read, file = paste0(path,"/oligo.csv"), row.names = FALSE)
  
  #Reads the PCR Reactions Portion of the CSV file
  pcr_read <- if (length(gibson) & length(golden_gate) > 0){
    readr::read_csv(file, col_names = c("Reaction ID Number", "Primary Template", "Alternate Template", "Forward Oligo ID Number", "Forward Oligo Name", "Reverse Oligo ID Number","Reverse Oligo Name", "Notes", "Mean Oligo Tm", "Delta Oligo Tm", "Mean Oligo Tm (3' Only)", "Delta Oligo Tm (3'Only)", "Length", "Sequence"), skip = pcr+1,n_max = golden_gate-pcr-3)
  } else if (length(golden_gate) > 0){
    readr::read_csv(file, col_names = c("Reaction ID Number", "Primary Template", "Alternate Template", "Forward Oligo ID Number", "Forward Oligo Name", "Reverse Oligo ID Number","Reverse Oligo Name", "Notes", "Mean Oligo Tm", "Delta Oligo Tm", "Mean Oligo Tm (3' Only)", "Delta Oligo Tm (3'Only)", "Length", "Sequence"), skip = pcr+1,n_max = golden_gate-pcr-3)
  } else if (length(gibson) > 0){
    readr::read_csv(file, col_names = c("Reaction ID Number", "Primary Template", "Alternate Template", "Forward Oligo ID Number", "Forward Oligo Name", "Reverse Oligo ID Number","Reverse Oligo Name", "Notes", "Mean Oligo Tm", "Delta Oligo Tm", "Mean Oligo Tm (3' Only)", "Delta Oligo Tm (3'Only)", "Length", "Sequence"), skip = pcr+1,n_max = gibson-pcr-3)
  }
  #feather::write_feather(pcr_read, path = paste0(path,"/pcr.feather"))#Creates feather file for Oligo Synthesis information
  write.csv(pcr_read, file = paste0(path,"/pcr.csv"), row.names = FALSE)
  
  #Reads the Assembly Pieces portion of the CSV file
  assembly_read <- if (length(gibson) & length(golden_gate) > 0){
    readr::read_csv(file, col_names = c("Reaction ID Number", "Reaction Type", "Type ID Number", "Part(s)" , "Relative Overlap Position", "Extra 5' CPEC bps", "Extra 3' CPEC bps","CPEC Tm Next", "Overlap with next (#bps)", "Overlap with Next (Sequence)", "Overlap with Next (Sequence Reverse Compliment)", "Sequence Length" , "Sequence" ), skip = golden_gate-1,n_max = combinations-golden_gate-3,guess_max = 100)
  } else if (length(golden_gate) > 0){
    readr::read_csv(file, col_names = c("Reaction ID Number", "Reaction Type", "Type ID Number", "Part(s)" , "Overhang with Previous", "Overhang with Next", "Relative Overhang Position", "Sequence Length", "Sequence" ), skip = golden_gate+1,n_max = combinations-golden_gate-3, guess_max = 100)
  } else if (length(gibson) > 0){
    readr::read_csv(file, col_names = c("Reaction ID Number", "Reaction Type", "Type ID Number", "Part(s)" , "Relative Overlap Position", "Extra 5' CPEC bps", "Extra 3' CPEC bps","CPEC Tm Next", "Overlap with next (#bps)", "Overlap with Next (Sequence)", "Overlap with Next (Sequence Reverse Compliment)", "Sequence Length" , "Sequence" ), skip = gibson+1,n_max = combinations-gibson-3, guess_max = 100)
  }
  #return(assembly_read)
  #feather::write_feather(assembly_read, path = paste0(path,"/assembly.feather"))#Creates feather file for Oligo Synthesis information
  write.csv(assembly_read, file = paste0(path,"/assembly.csv"), row.names = FALSE)
  
  combinations_read <- readr::read_csv(file, col_names = c("ID Number", "Name","Assembly Method", "Part(s) Bin 0", "Assembly Piece ID Number Bin 0", "Part(s) Bin 1", "Assembly Piece ID Number Bin 1","Part(s) Bin 2", "Assembly Piece ID Number Bin 2"), skip = combinations+2)
  #feather::write_feather(combinations_read, path = paste0(path,"/combinations.feather"))#Creates feather file for Oligo Synthesis information
  write.csv(combinations_read, file = paste0(path,"/combinations.csv"), row.names = FALSE)
  
  digests_read <- readr::read_csv(file, col_names = c("ID Number", "Sequence Source","Length", "Sequence"), skip = digests+1,n_max = oligo-digests-3)
  #feather::write_feather(combinations_read, path = paste0(path,"/combinations.feather"))#Creates feather file for Oligo Synthesis information
  write.csv(digests_read, file = paste0(path,"/digests.csv"), row.names = FALSE)
}

