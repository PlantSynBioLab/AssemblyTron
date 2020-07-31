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
#' parse_j5("J5_EricZirkle_GH3_mCherry")
parse_j5 <- function(path = getwd(), file = "_combinatorial.csv")
{
  #body
  j5lines <- readLines(file) #reads lines from J5 file to help with parsing

  oligo <- grep(pattern = "Oligo Synthesis",J5Lines) #searches for first set of data needed from J5 file (Oligo Synthesis Data)
  #returns line number for the Oligo Synthesis

  pcr <- grep(pattern = "PCR Reactions",J5Lines)#Searches for the title of the next set of data (PCR Reactions)
  #Returns the line number of this pattern

  gibson <- grep(pattern = "Assembly Pieces (SLIC/Gibson/CPEC)",j5lines,fixed = TRUE)#Searches for the title of next set of data if assembly pieces are gibson
  #returns the line number of this pattern

  golden_gate <- grep(pattern = "Assembly Pieces (Golden Gate",j5lines, fixed = TRUE)#Searches for the next set of data if the assembly is golden gate
  #returns line number for this pattern

  #Reads the Oligo Synthesis portion of the CSV file
  oligo_read <- readr::read_csv(file, col_names = c("ID Number", "Name", "Length", "Tm", "Tm (3' only)", "Cost", "Sequence", "Sequence (3' only)"),skip = Oligo+1,n_max = PCR-Oligo-3)
  return(Oligo_Read)

  oligo_feather <- feather::write_feather(Oligo_Read)#Creates feather file for Oligo Synthesis information

  #Reads the PCR Reactions Portion of the CSV file
  pcr_read <- readr::read_csv(file, col_names = c("Reaction ID Number", "Primary Template", "Alternate Template", "Forward Oligo ID Number", "Forward Oligo Name", "Reverse Oligo ID Number","Reverse Oligo Name", "Notes", "Mean Oligo Tm", "Delta Oligo Tm", "Mean Oligo Tm (3' Only)", "Delta Oligo Tm (3'Only)", "Length", "Sequence"), skip = PCR+1,n_max = gibson-PCR-3)
  pcr_feather <- feather::write_feather(PCR_Read)#creates feather file for the PCR reaction information

  #Reads the Assembly Pieces portion of the CSV file
  Assembly_Read <- if (gibson & golden_gate > 0)
  {

  }
  else if (gibson > 0) {
    readr::read_csv(file, col_names = c("Reaction ID Number", "Primary Template", "Alternate Template", "Forward Oligo ID Number", "Forward Oligo Name", "Reverse Oligo ID Number","Reverse Oligo Name", "Notes", "Mean Oligo Tm", "Delta Oligo Tm", "Mean Oligo Tm (3' Only)", "Delta Oligo Tm (3'Only)", "Length", "Sequence"), skip = gibson+1,n_max = gibson-combinations-3)
  }
  else if (golden_gate > 0){
    readr::read_csv(file, col_names = c("Reaction ID Number", "Primary Template", "Alternate Template", "Forward Oligo ID Number", "Forward Oligo Name", "Reverse Oligo ID Number","Reverse Oligo Name", "Notes", "Mean Oligo Tm", "Delta Oligo Tm", "Mean Oligo Tm (3' Only)", "Delta Oligo Tm (3'Only)", "Length", "Sequence"), skip = PCR+1,n_max = golden_gate-combinations-3)
  }



}
