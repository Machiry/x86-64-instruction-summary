import angr
proj = angr.Project('./instructions/vpaddd_xmm_xmm_xmm/vpaddd_xmm_xmm_xmm.o')
print proj.arch
print proj.entry
print proj.filename
irsb = proj.factory.block(proj.entry).vex
irsb.pp()