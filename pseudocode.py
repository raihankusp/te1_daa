BCIS Main Body
1: SL ← left
2: SR ← right
3: while SL < SR do
4:      SWAP(array, SR, SL + (SR−SL)/2)
5:      if array[SL] = array[SR] then
6:          if ISEQUAL(array, SL, SR)=-1 then
7:              return
8:          end if
9:      end if
10:     if array[SL] > array[SR] then
11:         SWAP(array, SL, SR)
12:     end if
13:     if (SR − SL) ≥ 100 then
14:         for i ← SL + 1 to (SR − SL)^0.5 do
15:             if array[SR] < array[i] then
16:                 SWAP(array, SR, i)
17:             else if array[SL] > array[i] then
18:                 SWAP(array, SL, i)
19:             end if
20:         end for
21:     else
22:         i ← SL + 1
23:     end if
24:     LC ← array[SL]
25:     RC ← array[SR]
26:     while i < SR do
27:         CurrItem ← array[i]
28:         if CurrItem ≥ RC then
29:             array[i] ← array[SR − 1]
30:             INSRIGHT(array,CurrItem, SR,right)
31:             SR ← SR − 1
32:         else if CurrItem ≤ LC then
33:             array[i] ← array[SL + 1]
34:             INSLEFT(array,CurrItem, SL, le f t)
35:             SL ← SL + 1
36:             i ← i + 1
37:         else
38:             i ← i + 1
39:         end if
40:     end while
41:     SL ← SL + 1
42:     SR ← SR − 1
43: end while

44: function ISEQUAL(array, SL, SR)
45:     for k ← SL + 1 to SR − 1 do
46:         if array[k] != array[SL] then
47:             SWAP(array, k, SL)
48:             return k
49:         end if
50:     end for
51:     return − 1
52: # End the algorithm because all scanned items are equal
53: end function

54: function INSRIGHT(array, CurrItem, SR, right)
55:     j ← SR
56:     while j ≤ right and CurrItem > array[j] do
57:         array[j − 1] ← array[j]
58:         j ← j + 1
59:     end while
60:     Array[j − 1] ← CurrItem
61: end function

62: function INSLEFT(array, CurrItem, SL, left)
63:     j ← SL
64:     while j ≥ le f t and CurrItem < array[j] do
65:         array[j + 1] ← array[j]
66:         j ← j − 1
67:     end while
68:     Array[j + 1] ← CurrItem
69:     end function

70: function SWAP(array,i,j)
71:     Temp ← array[i]
72:     array[i] ← array[j]
73:     array[j] ← T emp
74: end function