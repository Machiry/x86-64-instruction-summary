import angr
proj = angr.Project('./instructions/vpsrad_ymm_ymm_xmm/vpsrad_ymm_ymm_xmm.o')
print proj.arch
print proj.entry
print proj.filename
irsb = proj.factory.block(proj.entry).vex
irsb.pp()