import angr
proj = angr.Project('./instructions/testw_r16_r16/testw_r16_r16.o')
print proj.arch
print proj.entry
print proj.filename
irsb = proj.factory.block(proj.entry).vex
irsb.pp()