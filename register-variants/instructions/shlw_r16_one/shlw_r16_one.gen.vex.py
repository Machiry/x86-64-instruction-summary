import angr
proj = angr.Project('./instructions/shlw_r16_one/shlw_r16_one.o')
print proj.arch
print proj.entry
print proj.filename
irsb = proj.factory.block(proj.entry).vex
irsb.pp()