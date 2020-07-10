#' Parse a j5 assembly csv file into python readable feathers
#'
#' @param path a string representing the directory containing the j5 assembly
#' file to parse. This function operates on any file ending with
#' _combinatorial.csv by default.
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
parse_j5 <- function(path = getwd(), file = "_combinatorial.csv"){
  #body
}
