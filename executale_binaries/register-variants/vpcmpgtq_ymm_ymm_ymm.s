.globl _start
_start:
  vpcmpgtq %ymm3, %ymm2, %ymm1
  retq
