
#' Diluting Primer Protocols
#'
#' @param path the path to the J5 folder that containing approriate assembly files
#' @param oligo_sheet a link to the approriate google sheets containing information on the oligo(s)
#'
#' @return an opentrons protocol for diluting necessary primers
#' @export
#'
#' @details This function is used for primer dilutions
#' @examples
dilute_oligos <- function(path = getwd(), oligo_sheet){
 #
 # Dilutions Tasks-
 #    Ask what is being diluted(Which Primer) (Pop up that matches oWL ID in spreadsheet)
 #  -Check if there is any in stock that is already diluted from OWL or another spreadsheet (Grab
 #                                                                                           information from spreadsheet)
 #  -If no stock (If else statement/loop)
 #  -Confirm what is being diluted (reconfirm the oWL ID)
 #  -Calculate appropriate dilution volume to dilute 10x to 10uM (perform 10x dilution into
 #
 #                                                                appropriate tube)
 #  -Else If stock available
 #  -Check date
 #  -If less than one month old, use primer (display message: “Primer in stock and
 #
 #                                           fresh” and kick out)
 #
 #  -If greater than one month old, assume no stock assumption and redilute (go
 #
 #                                                                           back and assume no stock and perform no stock loop)
 #
 #  Pseudo code:
 #    Take information from the parsing code
 #  Compare primers in the file to the oWL spreadsheet (for stock)
 #
 #  If (primer name stock not available):
 #    pipette.pick_up_tip(tiprack[&#39;A1&#39;])
 #                                  pipette.aspirate((amount needed for dilution), plate[&#39;NFW&#39;], rate=2.0)
 #                                                                                         pipette.dispense(Amount from aspiration, plate[&#39;Primer&#39;], rate=2.0)
 #                                                                                                                                          pipette.blow_out()
 #                                                                                                                                        Else (primer available)
 #                                                                                                                                        Compare Date
 #                                                                                                                                        If date &lt; 30 days
 #                                                                                                                                        Perform operation
 #                                                                                                                                        Else date &gt;30 days
 #                                                                                                                                        No stock option
 #
 #
 #
 #
 #
 #
 #
 #








}
