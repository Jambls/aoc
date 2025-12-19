set infile [open "inputsmall.txt"]
set rows {}

while { [gets $infile line] >= 0 } {
    lappend rows $line
}
close $infile

proc check_row {grid row col} {
    if {$col < 0 || $col > [llength $grid]} {
        return 0
    } else {}
}

for {set i 0} {$i < [llength $rows]} {incr i} {
    for {set j 0} {$j < [llength [lindex $rows 0]]} {incr j} {
        if i
    }
}
# puts $rows