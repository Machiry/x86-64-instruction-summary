.globl _start
_start:
  vfmadd231sd %xmm3, %xmm2, %xmm1
  retq
