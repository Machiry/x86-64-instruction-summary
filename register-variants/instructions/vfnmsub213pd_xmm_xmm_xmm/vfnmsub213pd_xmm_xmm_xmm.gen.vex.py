import angr
proj = angr.Project('./instructions/vfnmsub213pd_xmm_xmm_xmm/vfnmsub213pd_xmm_xmm_xmm.o')
print proj.arch
print proj.entry
print proj.filename
irsb = proj.factory.block(proj.entry).vex
irsb.pp()