def MyQuickSort(L, L_Index, R_Index):
    ll,rr=L_Index,R_Index
    pivot=L[(ll+rr)//2]
    while ll<rr:
        while L[ll]<pivot and ll<R_Index:
            ll=ll+1
        while L[rr]>pivot and rr>L_Index:
            rr=rr-1
        if ll<=rr:
            L[rr],L[ll]=L[ll],L[rr]
            ll=ll+1
            rr=rr-1
    if rr>L_Index:
        MyQuickSort(L,L_Index,rr)
    if ll<R_Index:
        MyQuickSort(L,ll,R_Index)