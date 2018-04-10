import angr
proj = angr.Project('./instructions/salb_rh_cl/salb_rh_cl.o')
print proj.arch
print proj.entry
print proj.filename
irsb = proj.factory.block(proj.entry).vex
irsb.pp()