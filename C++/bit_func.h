#ifndef BIT_FUNC_H
#define BIT_FUNC_H

bool GetBit(int num, int i);
int SetBit(int num, int i);
int ClearBit(int num, int i);
int ClearBitsMSBthrouthI(int num, int i);
int ClearBitsIthrough0(int num, int i);
int UpdateBit(int num, int i, bool bit_is_1);

#endif /* BIT_FUNC_H */
