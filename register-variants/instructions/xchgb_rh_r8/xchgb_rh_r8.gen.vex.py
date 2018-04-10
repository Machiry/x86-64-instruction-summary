import angr
proj = angr.Project('./instructions/xchgb_rh_r8/xchgb_rh_r8.o')
print proj.arch
print proj.entry
print proj.filename
irsb = proj.factory.block(proj.entry).vex
irsb.pp()