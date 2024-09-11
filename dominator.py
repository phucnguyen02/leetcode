

# # dominator(A)
# # n = len(A)
# # chunk_count = n // 4
# # chunks = []*chunk_count
# # for i = 0, ..., n - 1:
# #   chunks[i]

# get_dominators(A, l, r, same)
#     n = len(A)
#     dominators = []
#     for i = l, ..., r:
#         if same[i] > floor(n/4) then
#             if dominators is empty then dominators.add((i, same[i]))
#             else then
#                 dupe = false
#                 for dominator in dominators:
#                     if CheckEQ(i, dominator, A) then dupe = True
#                 if !dupe then dominators.add((i, same[i]))
#     return dominators

# dominator_indices_4(A, l, r)
#     n = len(A)
#     same = {}
#     same[l] = same[l + 1] = ... = same[r] = 1
    
#     for i = l, ..., r - 1:
#         for j = l + 1, ..., r:
#             if CheckEQ(i, j, A) then same[i] += 1

#     dominators = get_dominators(A, l, r, same)
#     if dominators is empty then return (false, [])
#     return (true, dominators)

# dominator_indices_rest(A, l, r, same, Al, Ar)
#     n = Ar - Al + 1
    
#     for i = 1, 2, ..., len(same) - 1:
#         index = same[i][1]
#         for j = Al, Al + 1, ..., Ar:
#             if l <= j <= r then continue
#             if CheckEQ(i, j, A) then same[i] += 1

#     dominators = get_dominators(A, l, r, same)
#     if dominators is empty then return (false, [])
#     return (true, dominators)

# dominator(A, l, r)
#     n = len(A)
#     if n <= 3: return (True, [l, l + 1, ..., r])
#     if n == 4:
#         return dominator_indices_4(A, l, r)
#     chunk_size = floor(n / 4)
#     chunks = []*4
#     for i = 0, 1, 2:
#         chunks[i] = [dominator(A, l + i * chunk_size, l + (1 + i) * chunk_size - 1), l + i * chunk_size, l + (1 + i) * chunk_size - 1]
#     chunks[3] = [dominator(A, l + 3 * chunk_size, r), l + 3 * chunk_size, r]

#     dominators = []
#     for chunk in chunks:
#         if chunk[0][0] then 
#             dominator_indices = dominator_indices_rest(A, chunk[1], chunk[2], chunk[0][1], l, r)
#             if dominator_indices[0] then dominators.extend(dominator_indices[1])
    
#     if dominators is empty then return (false, [])
#     return (true, dominators)