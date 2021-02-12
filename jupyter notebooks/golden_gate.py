#
#Golden Gate
#
#
#
#
#
#
#
#
#
#Here is the Golden Gate DNA assembly protocol (adapted from Engler 2008 and Engler 2009):
### Print to screen to collect the necessary materials 
# 1) Measure the DNA concentration (ng/uL) of each assembly piece.
### Read in the concentration of each piece
#
#2) Add 100 ng of the linearized vector backbone and equimolar amounts of the other assembly pieces to a 15 uL total volume assembly reaction mixture as follows:
### Calculate volumes of each fragment and water to make up 15 ul

#                linearized vector backbone (100 ng)
#    +            each additional assembly piece (to equimolar with backbone)
#    +      1.5    uL    10X NEB T4 Buffer
#    +      0.15    uL    100X BSA*
#    +      1    uL    BsaI
#    +      1    uL    NEB T4 Ligase, 2 million cohesive end units / uL
#    +         dH20 to
#        15     uL
#
#    NOTE: It is essential to use a High Concentration Ligase
#
#    * BsaI is only 10% active at 37 C without the addition of BSA.
#
#3) Perform the assembly reaction in a thermocycler as follows:
#
#    either (following Engler 2009): (we usually prefer this one)
#
#    3        min     @ 37 C}
#     4        min    @ 16 C}    15-25 cycles
#
#    5        min    @ 50 C}
#     5        min    @ 80 C}    1 cycle
#
#    or, alternatively (modified from Engler 2008)
#
#    1        hour    @ 37 C      1 cycle
#
#    5        min    @ 50 C}
#     5        min    @ 80 C}    1 cycle
#
#    NOTE: If any of the assembly pieces contain an internal BsaI site(s), it
#        would be first preferable to silence the internal BsaI site(s) through
#        point mutation(s); a second option, if the internal BsaI site overhang(s)
#        are not cohesive with the other assembly overhangs, is to adjust the
#thermocycling parameters to terminate after a ligation step (e.g. skip the final cycle at 50 and then 80 C).
#
#4) Transform 5 uL of the assembly reaction into 100 uL of competent E. coli and/or run a diagnostic agarose gel to check for successful assembly.
#
